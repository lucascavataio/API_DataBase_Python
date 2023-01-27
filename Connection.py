import mysql.connector
import getpass
import ReadInfoProgram
import CreationProgram
import UsersProgram

commands = {0: "Show commands", 1: "Start 'creation' program", 2: "Start 'read and search' program", 3: "Start 'User' program"}
inputCreationPosibilities = {0: "Exit Creation program", 1: "Create Data Base", 2: "Delete Data Base", 3: "Crate Table",4:"Insert Values Into Table", 5:"Delete Table", 6:"Update Table", 7:"Remove Record From Table"}
inputReadInfoPosibilities = {0: "Exit Read and Search program", 1: "Show Data Bases", 2: "Show Tables", 3: "Show Table Info"}

inputUsersPosibilities = {0: "Exit User program", 1: "Show Created Roles", 2: "Show Users", 3: "Create User", 4: "Delete User", 5: "Modify User", 6: "Create Role", 7: "Delete Role", 8: "Modify Role" , 9: "Change User"}


userPermissions = {"admin": "admin115", "writer": "writer71", "reader": "reader25"}

user = ""

permissions = ""

permissionPassword = ""

userPassword = ""

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

HOST=""
USERNAME=""
PASSWORD=""
DATABASE=""

def FastConnection():
  return mysql.connector.connect(

    host=HOST,

    user=USERNAME,

    password=PASSWORD,

    database= DATABASE
    )

def ConnectToDataBase():

  print("\nStarting program")

  while True:

    print("\nEnter the information\n")

    uiHost = input("Host: ") 
    uiUser = input("User: ") 
    uiPassword = getpass.getpass("Password: ") 

    try:
      return mysql.connector.connect(

      host=uiHost,

      user=uiUser,

      password=uiPassword
      )
    except mysql.connector.Error as err:
      print("\nSomething went wrong: {}".format(err))
      print("Check the information you are entering...\n")

  


mydb = ConnectToDataBase()
#mydb = FastConnection()

print("\nContected to:", mydb)

mycursor = mydb.cursor()

class CommandsProgram():
  def ShowCommands():
    print("\nCommands: \n")

    for c in commands:
      print(str(c) + ":", commands[c])

  def ShowCreationCommands():
      print("\nCreation Commands: \n")
    
      for ic in inputCreationPosibilities:
        print(str(ic) + ":", inputCreationPosibilities[ic])

  def ShowReadInfoCommands():
    print("\nRead Info Commands: \n")

    for ir in inputReadInfoPosibilities:
        print(str(ir) + ":", inputReadInfoPosibilities[ir])

  def ShowUserCommands():
    print("\nUser Program Commands: \n")

    for u in inputUsersPosibilities:
        print(str(u) + ":", inputUsersPosibilities[u])

  
def CreationProgramIdle():
  exit = False
  while exit == False:
    CommandsProgram.ShowCreationCommands()

    uInput = input("Input: ")

    if uInput.isnumeric():
      if int(uInput) == 0:
        exit = True
      elif int(uInput) == 1 and UsersProgram.users[UsersProgram.currentUser].role.createTables:
        CreationProgram.CreateDataBase(mydb)
      elif int(uInput) == 2 and UsersProgram.users[UsersProgram.currentUser].role.deleteTables:
        CreationProgram.DeleteDataBase(mydb)
      elif int(uInput) == 3 and UsersProgram.users[UsersProgram.currentUser].role.createTables:
        CreationProgram.CreateTable(mydb)
      elif int(uInput) == 4 and UsersProgram.users[UsersProgram.currentUser].role.modifyTables:
        CreationProgram.InsertValuesInTable(mydb)
      elif int(uInput) == 5 and UsersProgram.users[UsersProgram.currentUser].role.deleteTables:
        CreationProgram.DeleteTable(mydb)
      elif  int(uInput) == 6 and UsersProgram.users[UsersProgram.currentUser].role.modifyTables:
        CreationProgram.UpdateTable(mydb)
      elif  int(uInput) == 7 and UsersProgram.users[UsersProgram.currentUser].role.modifyTables:
        CreationProgram.DeleteRecordsFromTable(mydb)
      else:
        print()
        print("That command doesen't exist or you don't have permission...")
        print()
    else:
      print()
      print("That command doesen't exist... Check if your input is numeric")
      print()
      break

def ReadInfoProgramIdle():
  exit = False
  while exit == False:
    CommandsProgram.ShowReadInfoCommands()

    uInput = input("Input: ")

    if uInput != "":
      if int(uInput) == 0:
        exit = True
      elif int(uInput) == 1 and UsersProgram.users[UsersProgram.currentUser].role.selectTables:
        ReadInfoProgram.ShowDataBases(mydb)
      elif int(uInput) == 2 and UsersProgram.users[UsersProgram.currentUser].role.selectTables:
        ReadInfoProgram.ShowTables(mydb)
      elif int(uInput) == 3 and UsersProgram.users[UsersProgram.currentUser].role.selectTables:
        ReadInfoProgram.ShowAllDataFromTable(mydb)
      else:
        print()
        print("That command doesen't exist or you don't have permission...")
        print()
    else:
      print()
      print("That command doesen't exist... Check if your input is numeric")
      print()

def UsersProgramIdle():
  exit = False
  while exit == False:
    CommandsProgram.ShowUserCommands()

    uInput = input("Input: ")

    if uInput != "":
      if int(uInput) == 0:
        exit = True
      elif int(uInput) == 1:
        UsersProgram.ShowCreatedRoles()

      elif int(uInput) == 2:
        UsersProgram.ShowUsers()

      elif int(uInput) == 3 and UsersProgram.users[UsersProgram.currentUser].role.createUsers:
        UsersProgram.CreateUser()
      elif int(uInput) == 4 and UsersProgram.users[UsersProgram.currentUser].role.deleteUsers:
        UsersProgram.DeleteUser()
      elif int(uInput) == 5 and UsersProgram.users[UsersProgram.currentUser].role.modifyUsers:
        UsersProgram.ModifyUser()
      elif int(uInput) == 6 and UsersProgram.users[UsersProgram.currentUser].role.createUsers:
        UsersProgram.CreateRole()
      elif int(uInput) == 7 and UsersProgram.users[UsersProgram.currentUser].role.createUsers:
        UsersProgram.DeleteRole()
      elif int(uInput) == 8 and UsersProgram.users[UsersProgram.currentUser].role.createUsers:
        UsersProgram.ModifyRole()
      elif int(uInput) == 9:
        UsersProgram.ChangeUser
      else:
        print()
        print("That command doesen't exist or you don't have permission...")
        print()
    else:
      print()
      print("That command doesen't exist... Check if your input is numeric")
      print()

def ProgramIdle():
  while True:
    CommandsProgram.ShowCommands()

    idleInput = input("Input: ")

    if idleInput.isnumeric():
      if int(idleInput) in commands:
        if int(idleInput) == 1:
          CreationProgramIdle()
        elif int(idleInput) == 2:
          ReadInfoProgramIdle()
        elif int(idleInput) == 3:
          UsersProgramIdle()
        else:
          CommandsProgram.ShowCommands()
      else:
        print("\nThat command doesen't exist...\n")
    else:
      print()
      print("Only numeric input...")
      print()

ProgramIdle()