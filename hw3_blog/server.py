from flask import Flask, render_template, request, jsonify
import sqlite3
# import sys

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/enternew')
def food():
	return render_template('food.html')

@app.route('/addfood', methods = ['POST'])
def addfood():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	try:
		name = request.form['name']
		calories = request.form["calories"]
		cuisine = request.form["cuisine"]
		is_vegetarian = request.form["is_vegetarian"]
		is_gluten_free = request.form["is_gluten_free"]
		cursor.execute('INSERT INTO foods (name, calories, cuisine, is_vegetarian, is_gluten_free) VALUES (?,?,?,?,?)', (name, calories, cuisine, is_vegetarian, is_gluten_free))
		connection.commit()
		message = "Record successfully added"
	except:
		connection.rollback()
		message = sys.exc_info()#"error in insert operation"#
	finally:
		return render_template('result.html', message = message)
		connection.close()

@app.route('/favorite')
def favorite():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()	
	cursor.execute('SELECT * FROM foods WHERE name="mango"')
	return jsonify(cursor.fetchone())
	connection.close()

@app.route('/search', methods=['GET'])
def search():
	# return request.args.get('name')
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()	
	names = (request.args.get('name'),)
	cursor.execute('SELECT * FROM foods WHERE name=?',names)
	return jsonify(cursor.fetchone())
	connection.close()

@app.route('/drop')
def dropTable():
		connection = sqlite3.connect('database.db')
		cursor = connection.cursor()
		cursor.execute('''DROP TABLE foods''')
		connection.commit()
		connection.close()
		return('HI')