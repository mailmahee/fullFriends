import time
from flask import Flask, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    return render_template("index.html",friends=friends)
@app.route('/friends', methods=['POST'])
def add():
    print request.form['first_name']
    print request.form['last_name']
    print request.form['occupation']
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    data = {'first_name': request.form['first_name'],'last_name':  request.form['last_name'],'occupation': request.form['occupation']}
    mysql.query_db(query, data)
    return redirect('/')


@app.route('/update/edit/', methods=['GET'])
def update():
    identity = request.args.get('friend_id')
    action = request.args.get('action')
    query = "SELECT * FROM friends WHERE id = :id"
    data = {'id': identity}
    friend = mysql.query_db(query, data)
    return render_template('update.html', friend = friend,action = action)


@app.route('/friends/<id>', methods=['POST'])
def execUpdate(id):

    if request.form['action'] == 'update':
        query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :friend_id"
        data = {'first_name': request.form['first_name'], 'last_name':  request.form['last_name'], 'occupation': request.form['occupation'], 'friend_id':id}
    else:
        query = "DELETE FROM friends WHERE id = :id"
        data = {'id':id}


    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
