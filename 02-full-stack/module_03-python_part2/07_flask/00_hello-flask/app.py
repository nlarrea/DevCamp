from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# crea una nueva instancia de flask y lo guarda dentro de la variable 'app'
app = Flask(__name__)

# creamos una 'route'
@app.route('/')
def hello():
    return "Hey Flask"


if __name__ == "__main__":
    app.run(debug=True)