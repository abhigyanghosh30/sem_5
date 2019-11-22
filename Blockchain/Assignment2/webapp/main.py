from flask import Flask, session, render_template, request, redirect, url_for, Response, json, g, flash
from flask_sqlalchemy import SQLAlchemy
from Models import db
import os
import string 
import secrets 

app = Flask(__name__)
app.secret_key = os.urandom(67)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stock.db'

@app.route('/<address>')
def register(address):
	new_seed = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(10)) #generates a 10 character long random string  
	player = Player( address=address,randomseed=new_seed)
	db.session.add(player)
	db.session.commit()


if __name__ == "__main__":
    db.init_app(app=app)
    db.create_all(app=app)
    app.run(debug=True)
