from flask import Flask

app = Flask(__name__)

#Decorador de ruta
@app.route('/')
def index():
    return "Hello World!"

@app.route("/hola")
def hola():
    return "Hola"

@app.route("/user/<string:user>")
def use(user):
    return "Hola " + user

@app.route("/numero/<int:n>")
def numero(n):
    return "Número: {}".format(n)


@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "ID: {}, Nombre usuario: {}".format(id, username)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "El número es: {}".format(n1 + n2)

@app.route("/default/")
@app.route("/default/<string:dft>")
def dft(dft="xD"):
    return "El valor de dft es: " + dft


if __name__ == "__main__":
    app.run()