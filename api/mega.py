from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.debug =True
#adding the configuration
app.config["SQLALCHEMT_DATABASE_URL"] ='sqlite:///site.db'

#creating an sql achmey istamce

db=SQLAlchemy(app)

#model
class profile(db.model):
	id =db.Column(db.Integer,primary_key=True)
	firstname=db.Column(db,string(20), unique =False,nullable =False)
	lastname=db.Column(db,string(20), unique =False,nullable =False)
	age=db.Column(db.Integer ,nullable =False)
	def __repr__(self):
		return f"Name:{self.firstname},age:{self.age}"
	
	
if __name__ == '__main__':
	app.run()