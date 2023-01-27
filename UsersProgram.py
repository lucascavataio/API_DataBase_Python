import mysql.connector
import getpass

currentUser = 0

roleOptions = {0: "Admin",
1: "Writer",
2: "Reader",
3: "Create new role"}

rolePerms = ["Select Tables",
"Create Tables",
"Delete Tables",
"Modify Tables",
"Create Users",
"Delete Users",
"Modify Users"]

class User():
  def __init__(self, _name, _pasword, _role):
    self.userName = _name
    self.userPasword = _pasword
    self.role = _role

class Role():
  def __init__(self,_roleName, _selectTables, _crateTables, _deleteTables, _modifyTables, _createUsers, _deleteUsers, _modifyUsers):
    self.roleName = _roleName
    self.selectTables = _selectTables
    self.createTables = _crateTables
    self.deleteTables = _deleteTables
    self.modifyTables = _modifyTables
    self.createUsers = _createUsers
    self.deleteUsers = _deleteUsers
    self.modifyUsers = _modifyUsers


users = [User("Default", "default", Role("Admin", True, True, True, True, True, True, True))]

rols = [Role("Admin", True, True, True, True, True, True, True), Role("Writer", True, False, False, True, False, False, False), Role("Reader", True, False, False, False, False, False, False)]


def ShowCreatedRoles():
    print("ROLS:")
    for idx, r in enumerate(rols):
        print(str(idx) + ":", r.roleName)

def ShowUsers():
    print("USERS:")
    for idx, u in enumerate(users):
        print(str(idx) + ":", u.userName, "ROLE:", u.role.roleName)

    print("\nCurrent user: ", users[currentUser].userName)

def CreateUser():
  userName = input("Name: ")

  userPasword = getpass.getpass("Password: ")

  ShowCreatedRoles()

  while True:

    userInput = int(input("Select an option: "))

    if userInput == 3:
      users.append(User(userName, userPasword,  CreateRole()))
      ShowUsers()
      
      break
    elif userInput != 3 and userInput < len(rols) and userInput >= 0: 

      users.append(User(userName, userPasword, rols[userInput]))

      ShowUsers()
      break

    else:
      print("That option does't exist...")

def DeleteUser():
  ShowUsers()

  userInput = input("Select role to delete: ")

  if int(userInput) < len(users) - 1 or int(userInput) > len(users) - 1:
    print("That user doesn't exist...")
    DeleteUser()
  else:
    users.pop(int(userInput))
  
  ShowUsers()

def ModifyUser():
  ShowUsers()

  UserInput = input("Select the user you want to modify: ")

  if int(UserInput) < len(users) - 1 or int(UserInput) > len(users) - 1:
    print("That user doesn't exist...")
    ModifyUser()
  else:
    users[UserInput].userName = input("New name: ")

  ShowUsers()
    

def CreateRole():

  perms = []

  roleName = input("Role name: ")

  for p in rolePerms:
    userInput = input(":    Y/N")

    if userInput.lower() == "y":
        userInput = True
    else:
        userInput = False

    perms.append(userInput)

  rols.append(Role(roleName, perms[0], perms[1], perms[2], perms[3], perms[4], perms[5], perms[6]))

  return Role(roleName, perms[0], perms[1], perms[2], perms[3], perms[4], perms[5], perms[6])


def DeleteRole():

  ShowCreatedRoles()

  userInput = input("Select role you want to delete: ")

  if int(userInput) < len(rols) - 1 or int(userInput) > len(rols) - 1:
    print("That role doesn't exist...")
    DeleteRole()
  else:
    rols.pop(int(userInput))

  ShowCreatedRoles()

def ModifyRole():

  ShowCreatedRoles()

  UserInput = input("Role to change: ")

  if int(UserInput) < len(rols) - 1 or int(UserInput) > len(rols) - 1:
    print("That role doesn't exist...")
    ModifyRole()
  else:

    perms = []

    roleName = input("Role name: ")

    for p in rolePerms:
        userInput = input(":    Y/N")

        if userInput.lower() == "y":
            userInput = True
        else:
            userInput = False

        perms.append(userInput)

    rols[int(userInput)].roleName = roleName
    
    rols[int(userInput)].selectTables = perms[0]
    rols[int(userInput)].createTables = perms[1]
    rols[int(userInput)].deleteTables = perms[2]
    rols[int(userInput)].modifyTables = perms[3]
    rols[int(userInput)].createUsers = perms[4]
    rols[int(userInput)].deleteUsers = perms[5]
    rols[int(userInput)].modifyUsers = perms[6]

  ShowCreatedRoles()

def ChangeUser():
  global currentUser

  ShowUsers()

  userInput = input("Select user: ")

  userPasword = getpass.getpass("Password: ")

  if int(userInput) < len(users) - 1 or int(userInput) > len(users) - 1:
    print("That user doesn't exist...")
    ChangeUser()
  else:

    if userPasword == users[currentUser].userPassword:
        currentUser = int(userInput)
    else:
        print("Incorrect password...")

        ChangeUser()
        