import mysql.connector

def ShowDataBases(_db):

    instance = _db.cursor()

    try:
      instance.execute("SHOW DATABASES")
      print("--------")
      for x in instance:
        print(x)
      print("--------")
      
    except mysql.connector.Error as err:
      print("\nError ocurred while getting the data base...  {}".format(err))
      print("Try again\n")
    

    

def ShowTables(_db):
    instance = _db.cursor()

    try:
      instance.execute("SHOW TABLES;")
 
      myresult = instance.fetchall()

      print("--------")
      for x in myresult:
        print(x)
      print("--------")
      
    except mysql.connector.Error as err:
      print("\nError ocurred while getting the tables of the data base...  {}".format(err))
      print("Try again\n")
  
def ShowAllDataFromTable(_db):
    while True:

      uiTableName = input("Enter de name of the table: ")

<<<<<<< HEAD
      instance = _db.cursor()

      try:
        command = "SELECT * FROM " + uiTableName
        instance.execute(command)

        myresult = instance.fetchall()

        for x in myresult:
          print(x)

        break
        
      except mysql.connector.Error as err:
        print("No tables with the name {", uiTableName, "} found... Enter a valid name")
        break
=======
      stmt = "SHOW TABLES LIKE " + uiTableName

      instance = _db.cursor()
      instance.execute(stmt)
      result = instance.fetchone()

      if result:
        try:
          command = "SELECT * FROM " + uiTableName
          instance.execute(command)

          myresult = instance.fetchall()

          for x in myresult:
            print(x)

          break
          
        except mysql.connector.Error as err:
          print("\nError ocurred during this operation...  {}".format(err))
          print("Try again\n")
          break
      else:
          print("No tables with the name {", uiTableName, "} found... Enter a valid name")
>>>>>>> move creation and readInfo programs to diferent archive
