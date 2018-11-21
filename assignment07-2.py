'''
Create a simple example of how you would use Python "Pickling." Document the example in a Word document.
'''
##-------------------------------------------------#
# Title: assignment07-2  Part 2 worjing ith pythobn pickle
# Dev:   Luis De Marquez
# Date:  Nov  21, 2018
# ChangeLog: (Who, When, What)
#  First Version
#
#-------------------------------------------------#
#
## Data #############################################
# Global Variables
# data1 = first Array of data in Json format, 3 rows, Products
# data2 = second Array of data in Json format, 3 rows, Customer
#
# tableData1 = python list table multidimentional to store in memory (data1) to be saved later in a binary file
# tableData2 = python list table multidimentional to stote in memory (data2) to be saved later in a binary file
# Importnae Note:   in variables objfile1 and infile1,  they should not be declare in the same, creating issues
#                   loading and extracting data
# objfile1 = binary file open with 'wb' to be use for pickle.dump to save data into file
# infile1 = binary file open with 'rb' to be use for pickle.load to extract data from file
# unserialized_data1 = extract data1 array from binary file
# unserialized_data2 = extract data2 array from binary file
#
#
#
tableData1 = []
tableData2 = []
data1=[{
  "_id": {
    "$oid": "5968dd23fc13ae04d9000001"
  },
  "product_name": "sildenafil citrate",
  "supplier": "Wisozk Inc",
  "quantity": 261,
  "unit_cost": "$10.47"
}, {
  "_id": {
    "$oid": "5968dd23fc13ae04d9000002"
  },
  "product_name": "Mountain Juniperus ashei",
  "supplier": "Keebler-Hilpert",
  "quantity": 292,
  "unit_cost": "$8.74"
}, {
  "_id": {
    "$oid": "5968dd23fc13ae04d9000003"
  },
  "product_name": "Dextromathorphan HBr",
  "supplier": "Schmitt-Weissnat",
  "quantity": 211,
  "unit_cost": "$20.53"
}]
#
data2=[{
  "_id": {
     "$oid": "59761c23b30d971669fb42ff"
  },
      "isActive": "true",
      "age": 36,
      "name": "Dunlap Hubbard",
      "gender": "male",
      "company": "CEDWARD",
      "email": "dunlaphubbard@cedward.com",
      "phone": "+1 (890) 543-2508",
      "address": "169 Rutledge Street, Konterra, Northern Mariana Islands, 8551"
}, {
   "id": {
    "$oid": "59761c233d8d0f92a6b0570d"
   },
   "isActive": "true",
   "age": 24,
   "name": "Kirsten Sellers",
   "gender": "female",
   "company": "EMERGENT",
   "email": "kirstensellers@emergent.com",
   "phone": "+1 (831) 564-2190",
   "address": "886 Gallatin Place, Fannett, Arkansas, 4656"
}, {
   "id": {
      "$oid": "59761c23fcb6254b1a06dad5"
   },
      "isActive": "true",
      "age": 30,
      "name": "Acosta Robbins",
      "gender": "male",
      "company": "ORGANICA",
      "email": "acostarobbins@organica.com",
      "phone": "+1 (882) 441-3367",
      "address": "697 Linden Boulevard, Sattley, Idaho, 1035"
    }]
#
## Input/0utput ####################################
# import function pickle
import pickle
# simple for loop to transfer data1 array json format to python list tableData1
for line in data1:
    tableData1.append(line)
#
# simple for loop to transfer data2 array json format to python list tableData2
for line in data2:
    tableData2.append(line)
#
# printing python lists to verify data
print("Python list tableData1 ***********")
print(tableData1)
print()
print("Python list tableData2 ***********")
print(tableData2)
print()
#
## Data Processing #################################
# python pickle dump to a binary file
objfile1 =open("C:\\_PythonClass\\Assignment07\\test2.dat", 'wb')
pickle.dump(tableData1,objfile1)
pickle.dump(tableData2,objfile1)
# Important close binary file
objfile1.close()
#
# python pickle load to extrac data1 and data2 separate
infile1 =open("C:\\_PythonClass\\Assignment07\\test2.dat", 'rb')
unserialized_data1 = pickle.load(infile1)
unserialized_data2 = pickle.load(infile1)
# Important close binary file
infile1.close()
#
# printing python lists to verify data
print("Python total data1 Array from binary file ***********")
print("Unserialize data1: ", unserialized_data1  )
print()
print("Python total data2 Array from binary file ***********")
print("Unserialize data2: ", unserialized_data2  )
print()
#
# for loop to extract from unserialized_data1 each row
for row in unserialized_data1:
    print("Python rows in  data1 Array from binary file ***********")
    print("Data 1 Row: ", row )
#
print("*******************")
for row in unserialized_data2:
    print("Python rows in  data2 Array from binary file ***********")
    print("Data  Row: ", row)


