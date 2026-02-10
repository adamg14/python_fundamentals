import csv

with open('code/files/example.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f"the csv headers are: {', '.join(row)}")
            line_count += 1
        else:
            print(f"""
            {row[0]} lives in {row[1]}, {row[2]}. Their favourite coding language is {row[3]}
            """)
            line_count += 1
    print(f"The number of lines in the csv file is: {line_count} (including the header)")


# reading xlsx (excel) files
# import xlrd
# excel_book = xlrd.open_workbook('code/files/sample.xls')
# print(excel_book.nsheets)
# print(excel_book.sheet_names)

# reading xml files
import xml.etree.ElementTree as ET

tree = ET.parse('code/files/example_person.xml')
print(tree)
root = tree.getroot()
print(f"Root Tag: {root.tag}")
print(f"Root Attribute: {root.attrib}")
for child in root:
    if child.tag == 'skills':
        skills = [skill.text for skill in child.findall('skill')]
        print(f"field: skills")
        print(f"value: {skills}")
    else:    
        print(f'field: {child.tag}')
        print(f"value: {child.text}")
    
