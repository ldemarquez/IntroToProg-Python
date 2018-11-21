'''
Create a simple example of how you would use Python "Exception Handling."

'''
##-------------------------------------------------#
# Title: assignment07-1  Part 2 worjing ith pythobn pickle
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
# tableData1Label = label for python list tabledata1
# tableData1Labe2 = label for python list tabledata2
# Importnae Note:   in variables objfile1 and infile1,  they should not be declare in the same, creating issues
#                   loading and extracting data
# objfile1 = binary file open with 'wb' to be use for pickle.dump to save data into file
# infile1 = binary file open with 'rb' to be use for pickle.load to extract data from file
#
fileName = ("C:\\_PythonClass\\Assignment07\\test1.dat")
tableData1 = []
tableData2 = []
tableData1Label = ("Data1")
tableData2Label = ("Data2")
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
#
# class tableData to load data arrays json format into Python list
# class tableDataLoad:
class tableDataLoad:
    #
    # Function to load data array in to multidementional Python list by row
    # Argument v1 = data array in json format
    # Argument v2 = Python list Table

    try:
        def F_tableDataLoad(v1, v2):
            for line in v1:
                v2.append(line)
            #
    except Exception as e:
        print("There was a error!")
        print("pythons error info: ")
        print(e)
        #End of Method
#
# class for printing messages
class print_Message:
    @staticmethod
    # Function to pitnt an empty line
    def lineEmpty():
        print()

    # End of Method
    #
    # Function to print header of report and python tableData
    # Argument v1 = data array in json format loaded in python list
    # Argument v2 = data array Label
    def print_tableData(v1, v2):
        print("Python list", v2, "***********")
        print()
        print(v1)
    # End of Method
#
# class to pickle.dump and pickle.load
class SerializeFile:
    # Funtion to pickle dump tableData python list to bin file
    # Argument v1 = tableData
    # Argument v2 = Binary File to open 'wb' Variable defien global objfile1
    # Argument v3 = data array Label
    try:
        def SerializeData(v1, v2, v3):
            pickle.dump(v1, v2,)
            print(v3, " has been Serialize to file: ", v2)
            #
    except Exception as e:
        print("There was a error!")
        print("pythons error info: ")
        print(e)
        # End of Method
    #
    # Funtion to pickle load data array from bin file
    # # Argument v1 = tableData
    # Argument v2 = Binary File to open 'rb' Variable define global infile1
    # Argument v3 = data array Label
    #
    try:
        def UnserializeData(v1, v2, v3):
            v1 = pickle.load(v2)
            print("Python total data Array from binary file ***********")
            print("Unserialize data: ", v3)
            print()
            for row in v1:
                print("Python rows in  data Array", v3, "from binary file ***********")
                print("Data Row: ", row)
                print()
            # End of Method
    except Exception as e:
        print("There was a error!")
        print("pythons error info: ")
        print(e)
#
## Data Processing #################################
# # Step 1 .  transfer data1 array json format to python list tableData1
# syntax class.method(arguments)
try:
    tableDataLoad.F_tableDataLoad(data1, tableData1)
    #
    print_Message.lineEmpty()
    tableDataLoad.F_tableDataLoad(data2, tableData2)
    print_Message.lineEmpty()
    #
    # Step 2    printing python lists to verify data has been dumped
    # syntax class.method(arguments)
    print_Message.print_tableData(tableData1, tableData1Label)
    print_Message.lineEmpty()
    print_Message.print_tableData(tableData2, tableData2Label)
    # Step 3    python pickle dump to a binary file
    # syntax class.method(arguments)
    # Global variable, code will be improve to make a function to capture to pass this variable
    objfile1 =open("C:\\_PythonClass\\Assignment07\\test1.dat", 'wb')
    #
    SerializeFile.SerializeData(tableData1, objfile1, tableData1Label)
    print_Message.lineEmpty()
    SerializeFile.SerializeData(tableData2, objfile1, tableData2Label)
    print_Message.lineEmpty()
    #closing File 'wb'
    objfile1.close()
    #
    # Step 4    python pickle load to extract data
    # syntax class.method(arguments)
    # Global variable, code will be improve to make a function to capture to pass this variable
    infile1 =open("C:\\_PythonClass\\Assignment07\\test1.dat", 'rb')
    SerializeFile.UnserializeData(tableData1, infile1, tableData1Label)
    print_Message.lineEmpty()
    SerializeFile.UnserializeData(tableData2, infile1, tableData2Label)
    print_Message.lineEmpty()
    #closing file 'rb'
    infile1.close()
except Exception as e:
    print("There was a error!")
    print("pythons error info: ")
    print(e)



