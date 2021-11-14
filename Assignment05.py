# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# CLi,11.11.21,Added code to complete assignment 5
# CLi,11.13.21,Modified code to better adhere to separation of concerns
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None
strFile = '/Users/Home/Documents/_PythonClass/Assignment05/ToDoList.txt' # An object that represents a file
strData = ''  # A row of text data from the file
strTask = ''  # A variable for tasks
intPriority = 0 # A variable for priorities
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = """    
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """         # A menu of user options
strChoice = ''  # A capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, 'r')
strData = objFile.readlines()
# print(strData)  # viewing the format of the data saved in strData variable
for row in strData:
    p, t = row.split(', ')
    dicRow = {'Priority':int(p), 'Task':t.strip()}
    lstTable.append(dicRow)
# print(lstTable)  # testing if dictionary inside of table was created
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print('Priority' + ' | ' + 'Task')
        for row in lstTable:
            print(str(row['Priority']) + ', ' + row['Task'])
            # print(type(row))  # testing the data type of each row within the table
            continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        try:
            strTask = str(input('Enter a task: '))
            intPriority = int(input('Enter its priority: '))
            lstTable.append({'Task': strTask.capitalize(), 'Priority': intPriority})
            # print(lstTable)   # testing if new row was added
            print('New row added!')
        except:
            print('The priority of a task must be a number.')
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strTask = str(input('What task would you like to remove? '))
        for row in lstTable:
            if row['Task'].lower() == strTask.lower():
                lstTable.remove(row)
                print('Row removed')
            else:
                print('Row not found')
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, 'w')
        for row in lstTable:
            objFile.write(str(row['Priority']) + ', ' + row['Task'] + '\n')
        objFile.close()
        print('Data saved!')
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Exiting program')
        break  # and Exit the program

    else:
        print('Please only enter a number 1 to 5!')