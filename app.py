from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
db = SQLAlchemy(app)

class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	item = db.Column(db.String)

	def __init__(self,item):
		self.item = item

	def __repr(self):
		return '<Item %r>' % self.item

