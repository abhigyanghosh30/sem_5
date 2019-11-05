from flask import Flask, session, render_template, request, redirect, url_for, Response, json, g, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.urandom(67)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stock.db'

@app.route('/')
@app.route('/login')
def login():
	return render_template('login.html')