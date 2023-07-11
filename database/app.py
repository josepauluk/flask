from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import os

# Ruta absoluta de la base de datos
dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
# app.app_context().push()

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))

# Decorador de ruta
@app.route('/')
def index():
    titulo = "Home!"
    lista = ["footer", "header", "info"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route("/insert/default")
def insert_default():
    new_post = Posts(title="Defaul Title")
    db.session.add(new_post)
    db.session.commit()

    return "The default post was created."

@app.route("/select/default")
def select_default():
    post = Posts.query.filter_by(id=1).first()

    print(post.title)

    return "Query done."

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    #app.run(debug=True, port=3000, host="0.0.0.0")