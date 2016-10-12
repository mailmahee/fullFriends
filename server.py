import time
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'secret'
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    return render_template("index.html",friends=friends)
@app.route('/add', methods=['POST'])
def add():
    print request.form['first_name']
    print request.form['last_name']
    print request.form['occupation']
    print request.form['email']
    print request.form['created_at']

def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    data = {'first_name': request.form['first_name'],'last_name':  request.form['last_name'],'occupation': request.form['occupation']}
    mysql.query_db(query, data)
    return redirect('/')
@app.route('/delete', methods=['POST'])
def deleteRecord():
    return render_template('delete.html')
@app.route('/execdelete')
def execDelete():
    mysql.query_db("DELETE FROM friends WHERE id = session['id']")
    return redirect('/')
@app.route('/update')
def updateRecord():
    return render_template('update.html')
@app.route('/execupdate')
def execUpdate():
    return redirect('/')

app.run(debug=True)
