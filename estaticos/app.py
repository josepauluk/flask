from flask import Flask

app = Flask(__name__)

#Decorador de ruta
@app.route('/')
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True, port=3000, host="0.0.0.0")