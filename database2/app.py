from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
 
import os
 
BASE_DIR = os.path.dirname(__file__)
DB_FILE = os.path.join(BASE_DIR, "development.sqlite3")
DB_URI = "sqlite:///" + DB_FILE
SECRET_KEY = "123"
 
app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config["SECRET_KEY"] = SECRET_KEY
db = SQLAlchemy(app)
 
class Log(db.Model):
    __tablename__ = "logs"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)  
 
@app.route("/")
def index():
    return "Index." 

