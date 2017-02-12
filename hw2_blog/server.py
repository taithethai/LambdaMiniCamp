from flask import Flask, render_template, jsonify;

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/birthday')
def birthday():
	return '3 Jan 1981'

@app.route('/greeting/<name>')
def greeting(name):
	return 'Hello '+ name

@app.route('/sum/<a>/<b>')
def sum(a,b):
	return str(int(a)+int(b))

@app.route('/multiply/<a>/<b>')
def multiply(a,b):
	return str(int(a)*int(b))

@app.route('/subtract/<a>/<b>')
def subtract(a,b):
	return str(int(a)-int(b))

@app.route('/favoritefoods')
def favoritefoods():
	foodList = [
	'pad thai', 'cottage pie'
	]
	return jsonify(foodList)

@app.route('/dylan')
def dylan():
	return app.send_static_file('dylan.html')

