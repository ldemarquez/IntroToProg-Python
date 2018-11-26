'''
Assignment08
From existing code create a new Python script with one or more classes
'''
## -- Data --
# Global Variables
FileHandle = ("C:\\_PythonClass\\Assignment08\\Products.txt") #File Handle
#
## -- Processing --
# Class Reference
    # -------------------------------------#
    # Desc: Class to Write Product
    # Dev: Luis De Marquez
    # Date: Nov 16 2016
    # ChangeLog: (When,Who,What)
    # -------------------------------------#
    #

    # --Constructor--
    # Attributes
    # --Properties--
    #
    # Method
    # Argument v1 is File Handle
class WriteProduct:
    # --Fields--
    strUserInput = None  # A string which holds user input
    try:
        def UserInput(File):
            print("Type in a Product Id, Name, and Price you want to add to the file")
            print("(Enter 'Exit' to quit!)")
            while (True):
                strUserInput = input("Enter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
                if (strUserInput.lower() == "exit"):
                    break
                else:
                    File.write(strUserInput + "\n")
    except Exception as e:
        print("Error: " + str(e))
    #end of method
#
# Class Reference
    # -------------------------------------#
    # Desc: Class to Read all data in File
    # Dev: Luis De Marquez
    # Date: Nov 16 2016
    # ChangeLog: (When,Who,What)
    # -------------------------------------#
    #
    # --Fields--
    #
    #
    # Method
    # Argument v1 is File Handle
class ReadAllFileData:
    try:
        def ReadFile(File, Message="Contents of File"):
            print(Message)
            File.seek(0)
            print(File.read())
    except Exception as e:
        print("Error: " + str(e))


#I/O
objFile = open(FileHandle, "r+")
ReadAllFileData.ReadFile(objFile, "Here is the current data:")
WriteProduct.UserInput(objFile)
ReadAllFileData.ReadFile(objFile, "Here is this data was saved:")
objFile.close()


