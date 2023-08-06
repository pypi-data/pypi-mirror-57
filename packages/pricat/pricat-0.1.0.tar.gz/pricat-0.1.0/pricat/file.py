#!/usr/bin/env python
# coding: utf-8

import json,sys, csv
import pandas as pd
import io,os.path
import re

##import numpy as np

def convert_header(header):
    MAPPINGS = [ ["SPECIAL_COMPOUNT", "SPECIAL_COMPOUND"],
                 ["W_REFERENZE_CODE", "X_REFERENCE_CODE"],
                 ["COUNTRY_ID", "COUNTRY_CODE"],
                 ["NV_VALID_FROM", "NV_VALID"]
    ]
    ## removing blank spaces at the beginning/end. and converto to uppercase
    new_row = header.strip().upper()
    ## converting one or more consecutive spaces (tabs, spaces,) with one _
    new_row = re.sub("\s+", "_", new_row)
    ## removing "strange" and not printable and characters
    new_row = re.sub("[^A-Z0-9\(\);_\+/]+","", new_row)
    ## renaming columns if...
    for  mapping in MAPPINGS:
        new_row = new_row.replace(mapping[0], mapping[1])

    return new_row

class File:
    TEMPLATES = [
            {"name": "B2",
             "rows": [convert_header("HDH;DOCUMENT_ID;DATE;CURRENCY;SUPPLIER_ILN;RECEIVER_ID;COUNTRY_ID;Ediwheel Version;C"),
                                    "HDS;0000000001;20190909;EUR;0000001303;113095;DE;B2;",
                                    convert_header("POH;POS;EAN;PROD_GRP_1;SUPPLIER_CODE;DESCRIPTION_1;DESCRIPTION_2;PROD_INFO;WDK_ANUB;WDK_BRAND;WDK_BRAND_TEXT;BRAND;BRAND_TEXT;PROD_GRP_2;GROUP_DESCRIPTION;WEIGHT;RIM_INCH;PROD_CYCLE;THIRD_PARTY;PL;TEL;EDI;ADHOC;PL_ID;URL_1;URL_2;URL_3;URL_4;URL_5;WIDTH_MM;WIDTH_INCH;ASPECT_RATIO;OVL_DIAMETER;CONSTRUCTION_1;CONSTRUCTION_2;USAGE;DEPTH;LI1;LI2;LI3(DWB);LI4(DWB);SP1;SP2;TL/TT;FLANK;PR;RFD;SIZE_PREFIX;COMM_MARK;RIM_MM;RUN_FLAT;SIDEWALL;DESIGN_1;DESIGN_2;PRODUCT_TYPE;VEHICLE_TYPE;COND_GRP;TAX_ID;TAX;SUGGESTED_PRICE;GROSS_PRICE;GP_VALID_FROM;NET_VALUE;NV_VALID;RECYCLING_FEE;NOISE_PERFORMANCE;NOISE_CLASS_TYPE;ROLLING_RESISTANCE;WET_GRIP;EC_VEHICLE_CLASS;EU_DIRECTIVE_NUMBER")
             ]
            },
            {"name": "B4",
             "rows": [convert_header("HDH;DOCUMENT_ID;DATE;CURRENCY;SUPPLIER_ILN;RECEIVER_ID;COUNTRY_CODE;EDIWHEEL_VERSION;C"),
                      "HDS;EW01A2;20190120;EUR;4019238000009;7201650;DE;B4.0;",
                      convert_header("POH;POS;EAN;PROD_GRP_1;SUPPLIER_CODE;DESCRIPTION_1;DESCRIPTION_2;PROD_INFO;RESERVED;M+S_MARK;3PMSF_MARK;BRAND;BRAND_TEXT;PROD_GRP_2;GROUP_DESCRIPTION;WEIGHT;RIM_INCH;PROD_CYCLE;THIRD_PARTY;PL;TEL;EDI;ADHOC;PL_ID;URL_1;URL_2;URL_3;URL_4;URL_5;WIDTH_MM;WIDTH_INCH;ASPECT_RATIO;OVL_DIAMETER;CONSTRUCTION_1;CONSTRUCTION_2;USAGE;DEPTH;LI1;LI2;LI3(DWB);LI4(DWB);SP1;SP2;TL/TT;FLANK;PR;RFD;SIZE_PREFIX;COMM_MARK;RIM_MM;RUN_FLAT;SIDEWALL;DESIGN_1;DESIGN_2;PRODUCT_TYPE;VEHICLE_TYPE;COND_GRP;TAX_ID;TAX;SUGGESTED_PRICE;GROSS_PRICE;GP_VALID_FROM;NET_VALUE;NV_VALID_FROM;RECYCLING_FEE;NOISE_PERFORMANCE;NOISE_CLASS_TYPE;ROLLING_RESISTANCE;WET_GRIP;EC_VEHICLE_CLASS;EU_DIRECTIVE_NUMBER;TRA_CODE;SEAL;SPECIAL_COMPOUND;DIRECTIONAL;ASYMETRIC;X_REFERENCE_CODE;MARKET_COMPLIANCE;WHEEL_POSITION;PRICE_REFERENCE_MATERIAL;RECOMMENDED_REPLACEMENT_ARTICLE;NON_GRADING_ELIGIBILITY;RFID;DESIGN_VARIANT")
             ]
            }
    ]
    def __init__(self, encoding="ISO-8859-1"):
        self.encoding = encoding
  
    def load_headers(self, filename, stream=None):
        if stream is None:
            stream_new =  open(filename, "r", encoding=self.encoding)
        else:
            stream_new = stream
        line1 = stream_new.readline()
        line2 = stream_new.readline()
        line3 = stream_new.readline()
        if stream is None:
            stream_new.close()
            
        return [convert_header(line1), line2, convert_header(line3)]

    def __compare_lines(self, line1, line3, expected_line1, expected_line3):
        result = {"status": "ko"}
    
        line1          = line1
        line3          = line3
        expected_line1 = expected_line1
        expected_line3 = expected_line3
    
        if expected_line1 in line1:
            result["status"] = "matching_header"
            if expected_line3 == line3:
                result["status"] = "ok"
            else:
                ## line3 not matching
                columns = line3.strip("\n").split(";")
                if '' in columns:
                    columns.remove('')
                expected_columns = expected_line3.strip("\n").split(";")
                result["line3_unexpected_columns"] = list(set(columns) - set(expected_columns))
                result["line3_missing_columns"] = list(set(expected_columns) - set(columns))
        else:
            ## line1 not matching
            columns = line1.strip("\n").split(";")
            expected_columns = expected_line1.strip("\n").split(";")
            result["line1_unexpected_columns"] = list(set(columns) - set(expected_columns))
            result["line1_missing_columns"] = list(set(expected_columns) - set(columns))
        return result

    def validate_files(self, dir):
        for filename in os.listdir(dir):
            if filename.endswith("csv"):
                result = self.validate_file(os.path.join(dir,filename))
                print(filename)
                print(result)

    def validate_file(self, filename):
        lines = self.load_headers(filename)
        return self.validate_headers(lines)

    def validate_headers(self, lines):
        results = []
        for template in self.TEMPLATES:
            result = self.__compare_lines(lines[0], lines[2], template["rows"][0], template["rows"][2])
            if result['status'] == 'ok':
                result['version'] = template["name"]
                header_info = self.__extract_info_from_header(lines)
                result.update(header_info)
                return result
            else:
                results.append(result)

        return {"status": "ko", "results": results}

    def __extract_field_from_headers(self, fieldname, headers):
        cols = headers[0].split(";")
        vals = headers[1].split(";")
        try:
            index = cols.index(fieldname)
            result = vals[index]
        except:
            result = "NOT_FOUND"
        return result

    def __extract_info_from_header(self, lines):
        country = self.__extract_field_from_headers("COUNTRY_CODE", lines)
        currency = self.__extract_field_from_headers("CURRENCY", lines)
        head_version = self.__extract_field_from_headers("EDIWHEEL_VERSION", lines)
        date = self.__extract_field_from_headers("DATE", lines)
        return {"COUNTRY": country, "CURRENCY": currency, "EDIWHEEL_VERSION": head_version, "DATE": date}

    def split_file(self, filename, target_path):
        headers = self.load_headers(filename)
        info = self.__extract_info_from_header(headers)

        basename = os.path.basename(filename).replace(".csv","")
        header_filename = os.path.join(target_path, basename + "-head.csv")
        list_filename = os.path.join(target_path, basename + "-full-list.csv")
        with open(header_filename, "w") as header_writer:
                header_writer.write(headers[0])
                header_writer.write(headers[1])
        with open(filename, encoding=self.encoding) as reader:
            reader.readline()
            reader.readline()
            reader.readline()
            with open(list_filename, "w") as list_writer:
                list_writer.write(headers[2])
                for line in reader:
                    list_writer.write(line)
                    return [header_filename, list_filename]

    def load_file(self, filename, sep=";", stream=None):
        if stream is None:
            stream =  open(filename, "r", encoding=self.encoding)
        headers =  self.load_headers(filename, stream=stream)
        info =  self.__extract_info_from_header(headers)
        lines = [headers[2]] + stream.readlines()
        new_stream=io.StringIO("\n".join(lines))
        alist = self.__load_csv(new_stream, sep=sep)
        return {"header": info, "list": alist}

    def __load_csv(self, filename, sep=";"):
        return pd.read_csv(filename, sep=sep)
    
    def parse(self, pricat, target_file=".", sep=";"):
        df = pricat["list"]
        df["COUNTRY"] = pricat["header"]["COUNTRY"]
        df["CURRENCY"] = pricat["header"]["CURRENCY"]
        df["DATE"] = pricat["header"]["DATE"]
        ## drop  columns
        df = df.drop(columns=["POS", "POH"])
        ## Selezionare dalla colonna “Brand” i second brand ed eliminarne tutte le righe ( ex: Bridgestone = Firestone).  
       # filter_brands = df["BRAND"].isin(['BS', 'FS'])
        
        ## Dalla colonna “Vehicle Type” cancellare quello che non è C0, L0, L4 e L5
        ##filter_vehicle_type = df["VEHICLE_TYPE"].isin(['C0', 'L0', 'L4', 'L5'])

        ##df[filter_brands & filter_vehicle_type]
    
        ## TODO
        ## Dalla Colonna Product Type cancella I valori superiori a 400. 
        ## '320', 'K', '200', '100', '300', '00f', '201', '00g'
    
        ## Cambia formato colonna “Ean” in formato numero senza decimali.  
        ##df["EAN"] = pd.to_numeric(df["EAN"])
        ##df["RIM_INCH"] = df["RIM_INCH"].astype(float)
        ## Da colonna “Supply Code”, solo per Continental,  creare una nuova colonna alla destra. Per i codici che iniziano con 15, fai un left a 7 cifre, mentre per gli altri left 6
     
        ## Da colonna “Product Info”, a destra creare tre colonne: “Oe Marking”, “Oe carmaker”, “Marking Brand Class”. Per compilare la prima e la seconda, fai una vlookup da file precedenti dalla colonna “Product Info”. Per compilare la colonna Marking Brand Class, utilizza la colonna Oe Carmaker. Incolla i valori e fai le seguenti modifiche:
        ## * a (*) 
        ## * MO a (*) (M0)*
        ## #N/A e 0 a " " 
    
        ## Creare colonna “Rim Band” a destra di colonna Rim (<=16, 17, >=18)
        ##df['RIM_BAND'] = df.apply(lambda row: None if type(row["RIM_INCH"]) == float and   np.isnan(row["RIM_INCH"]) else "<=16" if int(row["RIM_INCH"]) <= 16 else "17" if int(row["RIM_INCH"]) == 17 else ">=18" if int(row["RIM_INCH"]) >= 18 else "UNKNOWN",  axis=1)
        ## Da colonna SP1, trasformare tutto quello che è (Y) o ZR in Y. 
        
        ## Creare colonna “XL/std” a destra della colonna “RFD”. Compilarla in base alla colonna RFD. In particolare “Rfd” e “XL” à “XL” ,mentre ” “à “std” 
    
        ## Creare colonna “tech” e “r-f” a destra della colonna “Run_Flat”.
        ## Per determinare il contenuto delle colonne, è bene seguire  il seguente schema dei vari competitors, essendo le tecnologie chiamate in modo differente.  

        ## Seasonality:
     
        ## All Terrain:  fai vlookup da battistrada (colonna Design 1). Se viene N/a è il ruotino (solo Conti e Pirelli di solito, verificare perche non è una regola assoluta, nel caso cancella le righe). Incolla i valori e sostituisci gli 0 con “ “. 


        ## vehicle type : TODO: da mappare E0 M0, ...
        ##df['VEHICLE'] = df.apply(lambda row: "CAR" if row["VEHICLE_TYPE"] == "C0" else "SUV" if row["VEHICLE_TYPE"] in ["L4", "LS"] else "VAN" if row["VEHICLE_TYPE"] == "L0" else row["VEHICLE_TYPE"],  axis=1)

        df.to_csv(target_file, sep=sep, index=False)

if __name__ == "__main__":
    filename = sys.argv[1]
    files = split_source_file(filename)
    parse_list(files)
