### FILE HANDLING ###

import os

# .txt file
txt_file = open(
    "./my_file.txt", "w+"
)  # Con r+ se abre el archivo para lectura y escritura
# Con w+ se abre el archivo para escritura y en caso de que no exista lo crea


txt_file.write(
    "Mi nombre es Nicolas\nMi apellido es Rodriguez\n24 anos\ny mi lenguaje es JavaScript\n"
)

# print(txt_file.read())
# print(txt_file.read(10))  # Lee los 10 primeros caracteres
# print(txt_file.readline())  # Lee una sola linea
# print(txt_file.readlines())  # Lee todas las lineas
txt_file.write("Este es un nuevo texto")
print(txt_file.read())

txt_file.close()

# os.remove("./my_file.txt")

# .json file
import json

# with open("./my_file.json", "w") as json_file:
#     json.dump(
#         {
#             "name": "Nicolas",
#             "last_name": "Rodriguez",
#             "age": 24,
#             "language": "JavaScript",
#         },
#         json_file,
#     )


json_file = open("./my_file.json", "w+")

json_test = {
    "name": "Nicolas",
    "last_name": "Rodriguez",
    "age": 24,
    "language": "JavaScript",
}

json.dump(json_test, json_file, indent=2)
# json.dump(json_test, json_file, indent=2) # Aca se agregaria un nuevo diccionario seguidamente de donde termino el puntero desde la accion anterior


json_file.close()

with open("./my_file.json") as my_other_json_file:
    json_data = json.load(my_other_json_file)
    print(json_data)

json_dict = json.load(open("./my_file.json"))
print(type(json_dict))
print(json_dict)

# .csv file
import csv

# Crear un archivo CSV y escribir datos
csv_file = open("./my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "last_name", "age", "language"])
csv_writer.writerow(["Nicolas", "Rodriguez", 24, "JavaScript"])
csv_writer.writerow(["Maria", "Garcia", 28, "Python"])
csv_writer.writerow(["Carlos", "Lopez", 32, "Java"])

csv_file.close()

# Leer un archivo CSV
with open("./my_file.csv", "r") as csv_read_file:
    csv_reader = csv.reader(csv_read_file)
    for row in csv_reader:
        print(row)

# Leer CSV como diccionario
with open("./my_file.csv", "r") as csv_dict_file:
    csv_dict_reader = csv.DictReader(csv_dict_file)
    for row in csv_dict_reader:
        print(f"Nombre: {row['name']}, Edad: {row['age']}, Lenguaje: {row['language']}")

# Escribir CSV usando diccionarios
data = [
    {"name": "Ana", "last_name": "Martinez", "age": 26, "language": "C++"},
    {"name": "Pedro", "last_name": "Sanchez", "age": 30, "language": "Go"},
]

with open("./my_file_dict.csv", "w", newline="") as csv_dict_write:
    fieldnames = ["name", "last_name", "age", "language"]
    csv_dict_writer = csv.DictWriter(csv_dict_write, fieldnames=fieldnames)

    csv_dict_writer.writeheader()
    csv_dict_writer.writerows(data)

# import csv

# csv_file = open("./my_file.csv", "w+")

# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(["name", "last_name", "age", "language"])
# csv_writer.writerow(["Nicolas", "Rodriguez", 24, "JavaScript"])

# csv_file.close

# .xlsx file

# import openpyxl

# workbook = openpyxl.Workbook()
# sheet = workbook.active

# sheet["A1"] = "Name"
# sheet["B1"] = "Last Name"
# sheet["C1"] = "Age"
# sheet["D1"] = "Language"

# sheet["A2"] = "Nicolas"
# sheet["B2"] = "Rodriguez"
# sheet["C2"] = 24
# sheet["D2"] = "JavaScript"

# workbook.save("./my_file.xlsx")

# .xml file

# import xml.etree.ElementTree as ET

# root = ET.Element("root")
# tree = ET.ElementTree(root)

# ET.SubElement(root, "name").text = "Nicolas"
# ET.SubElement(root, "last_name").text = "Rodriguez"
# ET.SubElement(root, "age").text = "24"
# ET.SubElement(root, "language").text = "JavaScript"

# tree.write("./my_file.xml")

# .pdf file

# from fpdf import FPDF

# pdf = FPDF()
# # pdf.add_page()
# # pdf.set_font("Arial", "B", 16)
# # pdf.cell(40, 10, "Hello World!")
# # pdf.output("./my_file.pdf")

# pdf.add_page()
# pdf.set_font("Arial", size=15)
# pdf.cell(200, 10, txt := "Nicolas Rodriguez", ln=True, align="C")
# pdf.ln(10)
# pdf.cell(200, 10, txt="24", ln=True, align="C")
# pdf.ln(10)
# pdf.cell(200, 10, txt="JavaScript", ln=True, align="C")
# pdf.output("./my_file.pdf")
