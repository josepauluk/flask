from flask import Flask, render_template

app = Flask(__name__)

#Decorador de ruta
@app.route('/')
def index():
    titulo = "Home!"
    lista = ["footer", "header", "info"]
    return render_template("index.html", titulo=titulo, lista=lista)

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True, port=3000, host="0.0.0.0")