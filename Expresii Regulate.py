import re

with open('./data.txt') as file:
    text = file.read()

pattern = re.compile(r'^-?\d+(,\d+)*(\.\d+(e\d+)?)?$')

format_ora = re.findall('[0-2][0-3]:[0-5][0-9]', text)
format_data = re.findall(r'\d{0,2}/[a-z]{3}/\d{2,4}', text)
numere = re.findall(r'-?[^\d:/\b]\d*[\,\.]*\d+e?\d*', text)
majuscula = re.findall(r'\b\s[A-Z]+[A-Za-z]+', text)

# print(format_ora)
# print(format_data)
# print(majuscula)
print(numere)

# matches = pattern.finditer(text)
# for match in matches:
#     print(match)
