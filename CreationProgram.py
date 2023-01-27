import mysql.connector
import getpass

varTypeDic = {"CHAR": 255,
  "VARCHAR": 65535,
  "TINYBLOB": 255,
  "TINYTEXT": 255,
  "TEXT": 65535,
  "ENUM": 65535,
  "BOOL": 0,
  "INT": 4294967295,
  "FLOAT": 4294967295,
  "DATETIME": 0}

def CreateDataBase(_db):
  #Generates a data base, but it doesnt show in railway.app

  instance = _db.cursor()

  print("Enter the name of the data base you wan't to create", "'/cancel' to exit")
  name = input()

  if name == "/cancel":
    print("\nOperation cancelled...\n")

  try:
    instance.execute("CREATE DATABASE {dname}".format(dname = name))
    print("\nData base created sucessfully...\n")
    
  except mysql.connector.Error as err:
    print("\nError ocurred while creating the data base...  {}".format(err))
    print("Try again\n")



def DeleteDataBase(_db):

  instance = _db.cursor()

  print("Enter the name of the data base you wan't to create", "'/cancel' to exit")
  name = input()

  if name == "/cancel":
    print()
    print("Operation cancelled...")
    print()
  try:
    instance.execute("DROP DATABASE {dname}".format(dname = name))
    print()
    print("Data base deleted sucessfully...")
    print()
    
  except mysql.connector.Error as err:
    print("\nError ocurred while deleting the data base...  {}".format(err))
    print("Try again\n")

def CreateTable(_db):

  instance = _db.cursor()

  cancelOperation = False

  dataList = []
  dataTypeList = []

  commandLine = "CREATE TABLE IF NOT EXISTS"

  print()
  print("'/cancel' to cancel the operation")
  print()

  tableName = input("Enter the name of the table you want to create: ")

  if tableName == "/cancel":
    cancelOperation = True
      
  commandLine = commandLine + " " + str(tableName) + " ("

  tableSize = 0

  primaryKeyAdded = False

  while True:
    if cancelOperation:
      break
    try:
      print()
      tableSize = input("Enter the number of columns you want in this table: ")
      print()

      if int(tableSize) > 0 and int(tableSize) < 1024:
        break
      else:
        print("Size must be between 0 and 1024")
    except:
      print("Only numbers")

  index = 0
  for x in range(0, int(tableSize)):
    index += 1

    if index > 1:
      commandLine += ", "

    if cancelOperation:
      break
    else:
      while True:
        if cancelOperation:
          break
        print()
        print("'/cancel' to cancel the operation")
        print()
        dataName = input("Enter the name of the data" + str(x) + ": ")

        if dataName == "/cancel":
          cancelOperation = True
          break
        
        if len(dataName) < 255:            
          dataList.append(dataName)
          commandLine = commandLine + str(dataName)
          break
        else:
          print("Only numbers and size < 1024")
      while True:
        if cancelOperation:
          break
        exitWhile = False
        print()
        print("'/cancel' to cancel the operation")
        print()
        print(varTypeDic.keys())
        print()
        typeName = input("Enter the data type name" + str(x) + ": ")
        
        if typeName == "/cancel":
          cancelOperation = True
          break

        if typeName.upper() == "DATETIME":
          print("YYYY-MM-DD HH:MI:SS")

        for k in varTypeDic.keys():
          if typeName.upper() == k:
            dataTypeList.append(typeName)
            commandLine = commandLine + " {var}".format(var = str(typeName.upper()))
            exitWhile = True
        
        if exitWhile:
          break
        else:
          print("Can't find that data type...")

      while True:
        if cancelOperation:
          break
        print()
        print("'/cancel' to cancel the operation")
        print()
        dataSize = input("Enter the value size: ")

        if dataSize == "/cancel":
          cancelOperation = True
          break

        if dataSize.isnumeric():
          if int(dataSize) <= varTypeDic[typeName] and int(dataSize) > 0:
            commandLine = commandLine + "({size}) ".format(size = int(dataSize))
            break
          else:
            print("That type cant have that size...")
        else:
          print("Only numbers")
          
      while True:
        if cancelOperation:
          break
        
        print()
        print("'/cancel' to cancel the operation")
        print()
        uInput = input("This data is Auto Increment:   y/n  ")

        if uInput == "/cancel":
          cancelOperation = True
          break

        if uInput == "y":
          commandLine = commandLine + "AUTO_INCREMENT "
          break
        elif uInput == "n":
          break
        else:
          print("Only y/n")
      if primaryKeyAdded == False:
        if cancelOperation:
          break
        while True:
          print()
          print("'/cancel' to cancel the operation")
          print()
          uInput = input("This data is a primary key:   y/n")

          if uInput == "/cancel":
            cancelOperation = True
            break

          if uInput == "y":
            commandLine = commandLine + "PRIMARY KEY "
            primaryKeyAdded = True
            break
          elif uInput == "n":
            break
          else:
            print("Only y/n")
      while True:
        

        if cancelOperation:
          break
        
        if primaryKeyAdded:
          commandLine = commandLine + "NOT NULL"
          break
        else:
          print()
          print("'/cancel' to cancel the operation")
          print()

          
          uInput = input("This data can be NULL:   y/n  ")

          if uInput == "/cancel":
            cancelOperation = True
            break

          if uInput == "y":
            break
          elif uInput == "n":
            commandLine = commandLine + "NOT NULL "
            break
          else:
            print("Only y/n")
    print("--------")
    print("Progress: ")
    print()
    print(commandLine)
    print("--------")

  if cancelOperation:
    print()
    print("Creation operation cancelled susccessfuly...")
    print()
    
  else:

    instance.execute(commandLine + ")")
    print("Table created successfuly...")

def InsertValuesInTable(_db):

  instance = _db.cursor()

  command = "INSERT INTO "

  while True:

    print("'/cancel' to cancel the operation")
    uiTableName = input("Enter de name of the table that you want to insert values: ")

    if uiTableName == "/cancel":
      break

    stmt = "SHOW TABLES LIKE " + uiTableName
    instance.execute(stmt)
    result = instance.fetchone()

    if result:
        command += uiTableName
        break
    else:
        print("No tables with the name {", uiTableName, "} found... Enter a valid name")
  
  uiData = input("Enter the name of the data you want to instert the value: ")

  command += "("+ uiData +") VALUES"

  uiValue = input("Enter the value: ")

  command += "({_value}) ".format(_value = uiValue)



def DeleteTable(_db):

  instance = _db.cursor()

<<<<<<< HEAD
  tableDeleted = False

  while not tableDeleted:
=======
  while True:
>>>>>>> move creation and readInfo programs to diferent archive

    print("'/cancel' to cancel the operation")
    uiTableName = input("Enter de name of the table that you want to delete: ")

    if uiTableName == "/cancel":
      break
<<<<<<< HEAD
    instance.execute("SHOW TABLES")
    cosa = instance.fetchall()

    for i in cosa:
      if i[0] == uiTableName:
        command = "DROP TABLE " + uiTableName
        print(command)
        instance.execute(command)
        tableDeleted = True
        break
    
    if not tableDeleted:
      print("No tables with the name {", uiTableName, "} found... Enter a valid name")
=======

    stmt = "SHOW TABLES LIKE " + uiTableName
    instance.execute(stmt)
    result = instance.fetchone()

    if result:
        command = "DROP TABLE " + uiTableName
        instance.execute(command)
        break
    else:
        print("No tables with the name {", uiTableName, "} found... Enter a valid name")
>>>>>>> move creation and readInfo programs to diferent archive

def UpdateTable(_db):

  instance = _db.cursor()

  command = "UPDATE "

  while True:

    print("'/cancel' to cancel the operation")
    uiTableName = input("Enter de name of the table that you want to update values: ")

    if uiTableName == "/cancel":
      break

    stmt = "SHOW TABLES LIKE " + uiTableName
    instance.execute(stmt)
    result = instance.fetchone()

    if result:
        command += uiTableName
        break
    else:
        print("No tables with the name {", uiTableName, "} found... Enter a valid name")
  
  uiField = input("Enter the name of the field you want to udate the value: ")

  uiOldValue = input("Enter the old value you want to update: ")

  uiNewValue = input("Enter the new value:")

  command += "SET {_fieldName} = '{_newValue}' WHERE {_fieldName} = '{_oldValue}'".format(_fieldName = uiField, _newValue = uiNewValue, _oldValue = uiOldValue)

  instance.execute(command)

  _db.commit()

  print(instance.rowcount, "record(s) affected")

def DeleteRecordsFromTable(_db):
  instance = _db.cursor()

  command = "DELETE FROM "

  while True:

    print("'/cancel' to cancel the operation")
    uiTableName = input("Enter de name of the table that you want to delete records: ")

    if uiTableName == "/cancel":
      break

    stmt = "SHOW TABLES LIKE " + uiTableName
    instance.execute(stmt)
    result = instance.fetchone()

    if result:
        command += uiTableName
        break
    else:
        print("No tables with the name {", uiTableName, "} found... Enter a valid name")
  
  uiField = input("Enter the name of the field of the value you want to delete: ")

  uiValue = input("Enter the record to delete: ")

  command += " WHERE {} = '{}' ".format(uiField, uiValue)