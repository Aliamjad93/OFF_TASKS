# Import the necessary libraries
import pdfplumber
import json
import re

# Define the path to the PDF file and the output JSON file
pdf_path = r"C:\Users\farha\Downloads\file.pdf"
json_output_file = "parsed_output.json"

# Define a function to extract information from a page
def extract_info(page):
    # Split the page's text into lines
    lines = page.extract_text().split('\n')
    
    # Initialize dictionaries to store the extracted data
    data = {}
    Another_dict = {}
    
    # Initialize a variable to track the current section
    section = None
    i = 0
    
    # Loop through each line in the page's text
    for line in lines:
        # Check if the line matches a pattern for a section number
        if re.match(r'^\d+\.', line):
            # Update the section based on the line's content, with some replacements
            section = line.strip()
            if i > 5:
                section = section.replace("14.", "ADDITIONAL INFORMATION: ")
            section = section.replace("1.", "REACTION INFORMATION: ")
            section = section.replace("14.", "SUSPECT DRUG(S) INFORMATION: ")
            section = section.replace("15.", "SUSPECT DRUG(S) INFORMATION: ")
            section = section.replace("17.", "SUSPECT DRUG(S) INFORMATION: ")
            section = section.replace("18.", "SUSPECT DRUG(S) INFORMATION: ")
            section = section.replace("22.", "CONCOMITANT DRUG(S) AND HISTORY: ")
            section = section.replace("23.", "ADDITIONAL INFORMATION: ")
            i += 1
            
            # Initialize an empty list for the section's data
            data[section] = []
            
        # If the section is not None, add the line to the section's data
        elif section is not None:
            data[section].append(line.strip())
    
    return data

# Initialize a dictionary to store the parsed data
parsed_data = {}

# Open the PDF using pdfplumber
with pdfplumber.open(pdf_path) as pdf:
    # Loop through each page in the PDF
    for page in pdf.pages:
        # Extract information from the page using the defined function
        page_data = extract_info(page)
        
        # Update the parsed_data dictionary with the extracted page data
        parsed_data.update(page_data)

# Convert the parsed data dictionary to a JSON string with indentation
json_string = json.dumps(parsed_data, indent=4)

# Save the JSON data to the specified output file
with open(json_output_file, "w", encoding="utf-8") as json_file:
    json_file.write(json_string)
