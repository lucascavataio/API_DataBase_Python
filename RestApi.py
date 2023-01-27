from flask import Flask, request, jsonify

from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL HOST'] = "http://127.0.0.1:5000"
app.config["MYSQL USER"] = "lucascavataio"
app.config["MYSQL PASSWORD"] = "JonBonJovi123"
app.config["MYSQL DB"] = "Westfield"

mysql = MySQL(app)

userList = [{"name": "John Mayer"}, {"name": "Slash"}]

@app.route("/")

def GetHTML_MAIN():

    cursor = mysql.connection.cursor()

    return "<h1>Hello world!</h1> <img src='https://www.tooltyp.com/wp-content/uploads/2014/10/1900x920-8-beneficios-de-usar-imagenes-en-nuestros-sitios-web.jpg' alt=''> "

@app.route("/newroute")

def GetHTML_NewRoute():

    cursor = mysql.connection.cursor()

    return "<h1>NewPage</h1> <img src='https://www.tooltyp.com/wp-content/uploads/2014/10/1900x920-8-beneficios-de-usar-imagenes-en-nuestros-sitios-web.jpg' alt=''>"

@app.route("/user/<id>",methods=["POST","GET"])
def HandleUserInfo(id):

    cursor = mysql.connection.cursor()

    if int(id) > len(userList) - 1 or int(id) < 0:
        return "<h1>That user doesn't exist</h1>"

    if(request.method == "GET"):
        return userList[int(id)]
    else:
        newUser = {"name": request.json['name']}
        userList.append(newUser)
        return userList[int(len(userList) - 1)]

@app.route("/user",methods=["POST","GET"])
def HandleUsers():

    cursor = mysql.connection.cursor()

    if(request.method == "GET"):
        return userList
    else:
        newUser = {"name": request.json['name']}
        userList.append(newUser)
        return userList

if __name__ == "__main__":
    app.run(debug = True)
