import mysql.connector

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

mydb = FastConnection()

print("\nContected to:", mydb)

mycursor = mydb.cursor()

def CreateTables():
    
  mycursor.execute('''CREATE TABLE IF NOT EXISTS Players (ID INT(8) AUTO_INCREMENT PRIMARY KEY NOT NULL, 
  ID_Inventory INT(8) NOT NULL, Nickname VARCHAR(25) NOT NULL, LVL INT(4) NOT NULL, Kills INT(12) NOT NULL, 
  Deaths INT(12) NOT NULL, KD FLOAT(6), Fav_Weapon INT(3) NOT NULL, 
  Time_Played VARCHAR(30) NOT NULL, Kill_Streak INT(3) NOT NULL, 
  WD FLOAT(3) NOT NULL, HS INT(12) NOT NULL)''')

  mycursor.execute('''CREATE TABLE IF NOT EXISTS Weapons (ID INT(8) AUTO_INCREMENT PRIMARY KEY NOT NULL, 
  Name VARCHAR(42) NOT NULL, Type VARCHAR(42) NOT NULL, Damage Float(3) NOT NULL, 
  Date_Imp DATETIME NOT NULL)''')

  mycursor.execute('''CREATE TABLE IF NOT EXISTS Inventory (ID INT(8) AUTO_INCREMENT PRIMARY KEY NOT NULL, 
  ID_Player INT(8) NOT NULL, Cash FLOAT(12) NOT NULL, Supplies INT(4) NOT NULL, 
  Supplies_Opened INT(6) NOT NULL, Weapon INT(8) NOT NULL)''')

  mycursor.execute('''CREATE TABLE IF NOT EXISTS Classes (ID INT(2) AUTO_INCREMENT PRIMARY KEY NOT NULL, 
  ID_Primary INT(8) NOT NULL, ID_Secondary INT(8) NOT NULL, ID_Perk INT(3) NOT NULL)''')

  mycursor.execute('''CREATE TABLE IF NOT EXISTS Supplies (ID INT(8) AUTO_INCREMENT PRIMARY KEY NOT NULL, 
  Price FLOAT(2) NOT NULL, Type VARCHAR(12))''')

  mycursor.execute('''CREATE TABLE IF NOT EXISTS Ranking (Position INT(8) PRIMARY KEY NOT NULL, 
  ID_Player INT(8) NOT NULL, Name VARCHAR(20))''')

  print("Tables created successfully")

def InsertValues():

  mycursor.execute('''INSERT INTO Players (ID, ID_Inventory, Nickname, LVL, Kills, Deaths, KD, Fav_Weapon, Time_Played, Kill_Streak, WD, HS)
  VALUES (NULL, 1, 'Clint Eastwood', 35, 1243, 400, 3.1, 0, '12:52:29', 32, 5.1, 422);''')
  mycursor.execute('''INSERT INTO Players (ID, ID_Inventory, Nickname, LVL, Kills, Deaths, KD, Fav_Weapon, Time_Played, Kill_Streak, WD, HS)
  VALUES (NULL, 2, 'Dutch Schaefer', 24, 200, 0, 200, 2, '3:22:59', 15, 20, 45);''')

  mycursor.execute('''INSERT INTO Supplies (ID, Price, Type)
  VALUES (0, 9.50, 'Legendary');''')
  mycursor.execute('''INSERT INTO Supplies (ID, Price, Type)
  VALUES (0, 4.99, 'Rare');''')
  mycursor.execute('''INSERT INTO Supplies (ID, Price, Type)
  VALUES (0, 2.99, 'Common');''')

  mycursor.execute('''INSERT INTO Weapons (ID, Name, Type, Damage, Date_Imp)
  VALUES (NULL, 'Winchester Model 1873', 'lever-action rifle', '99', '2023-09-15 14:30:00');''')
  mycursor.execute('''INSERT INTO Weapons (ID, Name, Type, Damage, Date_Imp)
  VALUES (NULL, 'Wyatt Earp 1881', 'Doube barreled shutgun','80', '2023-09-15 14:30:00');''')

  mycursor.execute('''INSERT INTO Ranking (Position, ID_Player, Name)
  VALUES (1, 1, 'Clint Eastwood');''')
  mycursor.execute('''INSERT INTO Ranking (Position, ID_Player, Name)
  VALUES (2, 2, 'Dutch Schaefer');''')

  mycursor.execute('''INSERT INTO Classes (ID, ID_Primary, ID_Secondary, ID_Perk)
  VALUES (NULL, 1, 4, 3);''')
  mycursor.execute('''INSERT INTO Classes (ID, ID_Primary, ID_Secondary, ID_Perk)
  VALUES (NULL, 2, 1, 5);''')

  mycursor.execute('''INSERT INTO Inventory (ID, ID_Player, Cash, Supplies, Supplies_Opened, Weapon)
  VALUES (NULL, 1, 58, 2, 12, 5);''')
  mycursor.execute('''INSERT INTO Inventory (ID, ID_Player, Cash, Supplies, Supplies_Opened, Weapon)
  VALUES (NULL, 2, 5, 0, 15, 4);''')

  print("Values inserted successfully")

#CreateTables()

#InsertValues()
