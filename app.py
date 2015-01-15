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

@app.route("/<password>"):
def index(password):
	true_password = ''
	with open("password.txt","r") as f:
		true_password += f.read().strip("\n")
	if password == true_password:
		all_items = Item.query.all()
		return render_template("index.html",items=all_items)
	else:
		return render_template("wrong.html")

@app.route("/add")
def add():
	new_item = request.form.get("new_item")
	item = Item(new_item)
	db.session.add(item)
	db.session.commit()
	all_items = Item.query.all()
	return render_template(index.html, itmes=all_items)

@app.route("/delete")
def delete():
	pass

@app.route("/update")
def update():
	pass