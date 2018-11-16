'''
1.- Make a function for the code that loads the each rows of data you have in the ToDo.txt
 text file into a python Dictionary and adds it to a Python List.
2.-  Make a function for the code that displays the contents of the List to the user.
3.- Make a function that displays a menu of options and called the appropriate function dependent on the selected choice.
4.- Make a function for the code that saves the data from the table into the Todo.txt file when the program exits.
5.- Make a function that allows users to add or remove content in the Python List.
6.- Make a Class to hold the functions.
'''
##-------------------------------------------------#
# Title: Working with Functions and Classes
# Dev:   Luis De Marquez
# Date:  Nov  15, 2018
# ChangeLog: (Who, When, What)
#  First Version
#
#-------------------------------------------------#
#
## Data #############################################
# Global Variables
# FileName= ("C:\\_PythonClass\\Assignment06\\ToDo.txt") to load and save data
# lstDataTable = list Table to collect or collected data in the loop and build the dict Table in one row


FileName = ("C:\\_PythonClass\\Assignment06\\ToDo.txt")
lstDataTable = [] # Init Variable

## Input/0utput ####################################
#  Main class
class HouseTasks:

    @staticmethod
    # Function to load data from File
    # Argument v1 = filename to open in Read Mode
    # Argument v2 = list Table to collect data in the loop and build the dict Table in one row
    def loadTxtFile(v1, v2):
        # dictRow = A Row of Data used in for loops
        # strData = A Row of text data from the file
        # Initial Loop to unpact loadfile and build lstDataTable
        objFile = open(v1, "r")
        for line in objFile:
            line = line.rstrip('\n')
            strData = line.split(",")
            dictRow = {"Task": strData[0], "Priority": strData[1].strip("\n")}
            v2.append(dictRow)
            #
        objFile.close()
        #end of for loop, it gave me hassle Bruuuuuu
        return v2
    # end function/method

    @staticmethod
    # Function to display information in file ( ToDo.txt )
    # Argument v1 = list Table to collect data in the loop and build the dict Table in one row
    def showData(v1):
        print("******* The current tasks in saved : *******")
        for dictRow in v1:
            print(dictRow["Task"] + "(" + dictRow["Priority"] + ")")
        print("*******************************************")
    # end function/method

    @staticmethod
    # Function to add Data to Global Variable lstDataTable
    # Argument v1 = list Table to collect data in the loop and build the dict Table in one row
    def addData(v1):
        vtask = str(input("Please Enter the task?:  ")).strip()
        print("Task is: ", vtask)
        print("Please Priority in format high, med or low")
        vpriority = str(input("Please Enter Priority: ")).strip()
        dicNewTask = {"Task": vtask, "Priority": vpriority}
        v1.append(dicNewTask)
        return v1

    # end function/method

    @staticmethod
    # Function to remove Data of Glabal Variable lstDataTable
    # Argument v1 = list Table to collect data in the loop and build the dict Table in one row
    def removeData(v1):
        vtask = input("Which TASK would you like removed? - ")
        blnItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        # Loop to look into lstDataTable for strKey to remove
        while (intRowNumber < len(v1)):
            if (vtask == str(list(dict(v1[intRowNumber]).values())[0])):
                del v1[intRowNumber]
                blnItemRemoved = True
            # end if
            intRowNumber += 1
        # end for loop
        #
        # Final validation Task was deleted or Task not found
        if (blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")

    # end function/method

    @staticmethod
    def mainMenuItems():
        valueChoice = None
        print("""
        Menu of Options
        1) Show current data 
        2) Add a new task
        3) Remove an existing task
        4) Save Data to File
        5) Exit Program
        """)
        print()  # adding a new line
    # end function/method

    @staticmethod
    def saveDataItems(v1, v2):
        # User input to Save or NoT data (lstDataTable) to a File
        # Argument v1 = filename to open in Write Mode
        # Argument v2 = list Table to collect data in the loop and build the dict Table in one row
        strSaveData = str(input("Save data to file? (yY/nN): "))
        strSaveData = strSaveData.lower()
        objFile = open(v1, "w")
        if (strSaveData.lower() == "y"):
            for dictRow in v2:
                objFile.write(dictRow["Task"] + "," + dictRow["Priority"] + "\n")
            objFile.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
    # end function/method
#
# End class HouseTasks
#
## Data Processing #################################
#
HouseTasks.loadTxtFile(FileName, lstDataTable)
#HouseTasks.showData(lstDataTable)

while(True):
    HouseTasks.mainMenuItems()
    strChoice = str(input("Which option would you like to perform? [1 to 4 or 5 to Exit] - "))
    print()  # adding a new line
    #
    if (strChoice == '1'):  # - Show the current items in the table
        HouseTasks.showData(lstDataTable)
        continue
    #
    if (strChoice == '2'):  # - Option 2 Add a New Task and Priority
        HouseTasks.addData(lstDataTable)
        continue
    #
    if (strChoice == '3'): # - Option 3 Remove Entry using Task as Key
        HouseTasks.removeData(lstDataTable)
        continue
    #
    if (strChoice == '4'):  # - Option to save tasks to the ToDo.txt file
        HouseTasks.saveDataItems(FileName, lstDataTable)
        continue

    elif (strChoice == '5'):
        break  # and Exit the program

