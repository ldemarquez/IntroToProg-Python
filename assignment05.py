'''
 List of Tasks

1.	Create a text file called Todo.txt using the following data:
Clean House,low
Pay Bills,high
File ToDo.txt has been created in directory C:\_PythonClass\Assignment05
'''
'''
2.	When the program starts, load each row of data from the ToDo.txt text file into a Python dictionary.
(The data will be stored like a row in a table.)
Tip: You can use a for loop to read a single line of text from the file and then place the data into a
 new dictionary object.
3.	After you get the data in a Python dictionary, 
Add the new dictionary “row” into a Python list object (now the data will be managed as a table).
4.	Display the contents of the List to the user.
5.	Allow the user to Add or Remove tasks from the list using numbered choices. Something like this would work:
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
6.	Save the data from the table into the Todo.txt file when the program exits.
'''
#-------------------------------------------------#
# Title: <assignment05.py>
# Dev:   <Luis De Marquez>
# Date:  <Nov 10 20018>
# Desc: <Assignment Module 05 >
# ChangeLog: (V1)
#
#-------------------------------------------------#
#
#-- Data --#
#
# variables and constans
# loadFile = ToDO.txt # OS file, location C:\_PythonClass\Assignment05
# lstDataTable = list Table to collect data in the loop and build the dict Table in one row
# dictRow = A Row of Data used in for loops
# strData = A Row of text data from the file
# strChoice = User Options Main Menu
# strTask = User Enter Task
# strPriority = User Enter priority
# dicNewTask = a Row of data User entered ( Task and Priority )
# strKeyToRemove = User enter Task to be removed
# strSaveData = User enter input to Save y/n
#
#-- Processing --#
# Task 1 Create Manually File ToDo.txt outside of this program
# Task 2 & 3 Load file ToDO.txt and get data in Python dictionary and manage by python list table
# Task 4    Display the contents of the List to the user.
# Task 5:   Allow the user to Add or Remove tasks from the list using numbered choices.
# Task 6:   Save the data from the table into the Todo.txt file when the program exits
#           Exit from Program without saving
#
######################################
# Task 2 & 3
#
#loadFile = ToDo.txt
loadFile =open("C:\\_PythonClass\\Assignment05\\ToDo.txt", "r")
lstDataTable=[]
# Initial Loop to unpact loadfile and build lstDataTable
for line in loadFile:
    line = line.rstrip('\n')
    strData = line.split(",")
    dictRow = {"Task": strData[0], "Priority": strData[1].strip("\n")}
    lstDataTable.append(dictRow)
loadFile.close()
#
#
#Task 4
print(" List of Initial Tasks and Priorities in file ToDo.txt")
for dictRow in lstDataTable:
    print(dictRow["Task"] + "(" + dictRow["Priority"] + ")")
    print("*******************************************")
#
# Task 5:   Allow the user to Add or Remove tasks from the list using numbered choices.
# Task 6:   Save the data from the table into the Todo.txt file when the program exits
while(True):

    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4 or 5 to Exit] - "))
    print()#adding a new line
    #Option 1 Show Current Data
    if (strChoice.strip() == '1'):
        print("******* The current items ToDo are: *******")
        for row in lstDataTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
    #
    #Option 2 Add a New Task and Priority
    elif (strChoice.strip() == '2'):
        strTask = str(input("Please Enter the task?:  ")).strip()
        print("Task is: ", strTask)
        print("Please Priority in format high, med or low")
        strPriority = str(input("Please Enter Priority: ")).strip()
        dicNewTask = {"Task": strTask, "Priority": strPriority}
        lstDataTable.append(dicNewTask)
        print("Current Data in table:")
        for dictRow in lstDataTable:
            print(dictRow["Task"] + "(" + dictRow["Priority"] + ")")
            print("*******************************************")
            continue #Continue to Main Menu
    #End of Option 2
    #
    #Option 3 Remove Entry using Task as Key
    elif (strChoice.strip() == '3'):
        # User to enter Row Key Field Task to Delete
        strKeyToRemove = input("Which TASK would you like removed? - ")
        blnItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        # Loop to look into lstDataTable for strKey to remove
        while (intRowNumber < len(lstDataTable)):
            if (strKeyToRemove == str(list(dict(lstDataTable[intRowNumber]).values())[0])):
                del lstDataTable[intRowNumber]
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
        #
        # Print the list of Tasks
        print("******* The current items ToDo are: *******")
        for dictRow in lstDataTable:
            print(dictRow["Task"] + "(" + dictRow["Priority"] + ")")
            print("*******************************************")
            continue #Continue to Main Menu
    #
    #Option to save tasks to the ToDo.txt
    elif (strChoice.strip() == '4'):
        for dictRow in lstDataTable:
            print(dictRow["Task"] + "(" + dictRow["Priority"] + ")")
            print("*******************************************")
        #User input to Save or NoT data (lstDataTable) to a File
        strSaveData = str(input("Save data to file? (yY/nN): "))
        strSaveData = strSaveData.lower()
        if (strSaveData.lower() == "y"):
            loadFile = open("C:\\_PythonClass\\Assignment05\\ToDo.txt", "w")
            for dictRow in lstDataTable:
                loadFile.write(dictRow["Task"] + "," + dictRow["Priority"] + "\n")
            loadFile.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
            continue  # to show the menu
            #
    #Option 5 to exit or break the program
    if (strChoice.strip() == '5'):
        print("!!! Exit Program without saving data !!! ")
        break


