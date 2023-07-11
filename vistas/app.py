from flask import Flask, render_template

app = Flask(__name__)

#Decorador de ruta
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True, port=3000, host="0.0.0.0")