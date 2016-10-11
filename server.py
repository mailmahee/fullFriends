import time
from flask import Flask, render_template, request, redirect,session
from mysqlconnection import MySQLConnection
app = Flask(__name__)
mysql = MySQLConnector(app,'myFriends')

@app.route('/')
def index():
    return render_template("index.html")

app.run(debug=True)
