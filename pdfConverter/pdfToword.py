
import pdfplumber
import json
import re
pdf_path = r"C:\Users\farha\Downloads\file.pdf"
json_output_file = "parsed_output.json"

def extract_info(page):
    lines = page.extract_text().split('\n')
    data = {}
    Another_dict={}
    section = None
    i=0
    for line in lines:
        # print(line)
        
        if re.match(r'^\d+\.', line):
            section = line.strip()
            if i>5:
                section=section.replace("14.", "ADDITIONAL INFORMATION: ")    
            section=section.replace("1.", "REACTION INFORMATION: ")
            section=section.replace("14.", "SUSPECT DRUG(S) INFORMATION: ")
            section=section.replace("15.", "SUSPECT DRUG(S) INFORMATION: ")
            section=section.replace("17.", "SUSPECT DRUG(S) INFORMATION: ")
            section=section.replace("18.", "SUSPECT DRUG(S) INFORMATION: ")
            section=section.replace("22.", "CONCOMITANT DRUG(S) AND HISTORY: ")
            section=section.replace("23.", "ADDITIONAL INFORMATION: ")
            i+=1

            
            data[section] = []
            

        elif section is not None:

            data[section].append(line.strip())
        
    

    return data




parsed_data = {}

with pdfplumber.open(pdf_path) as pdf:
    
        for page in pdf.pages:
                    
            page_data = extract_info(page)
                 
            parsed_data.update(page_data)
    
        

# Convert the parsed data dictionary to a JSON string
json_string = json.dumps(parsed_data, indent=4)

# Save the JSON data to a file
with open(json_output_file, "w", encoding="utf-8") as json_file:
    json_file.write(json_string)










