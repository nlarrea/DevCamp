from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# crea una nueva instancia de flask y lo guarda dentro de la variable 'app'
app = Flask(__name__)

# le decimos a flask dónde está la base de datos
basedir = os.path.abspath(os.path.dirname(__file__))
# le pasamos el directorio al que queremos que vaya, y le decimos que se llama 'app.sqlite'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")
# creamos un objeto de base de datos
db = SQLAlchemy(app)        # instanciar objeto de SQLAlchemy
ma = Marshmallow(app)       # instanciar objeto de Marshmallow

# creamos el esquema de la tabla (heredera de db.Model)
class Guide(db.Model):
    # añadimos una columna de tipo integer, y decirmos que es una primary key
    # primary_key=True -> hará que cada Guide tenga su propio ID, y cada ID incrementa automáticamente
    id = db.Column(db.Integer, primary_key=True)
    # creamos 2 columnas más de tipo string y limitamos su cantidad de chars a 100 y 144
    title = db.Column(db.String(100), unique=False)
    content = db.Column(db.String(144), unique=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content


class GuideSchema(ma.Schema):
    class Meta:
        # indicamos los 'fields' a los que queremos acceder dentro de una tupla
        fields = ("title", "content")


guide_schema = GuideSchema()            # para trabajar con 'single guide'
guides_schema = GuideSchema(many=True)  # para trabajar con 'multiple guides'

# endpoint to create a new guide
@app.route("/guide", methods=["POST"])  # creamos un guide con el verbo POST
def add_guide():
    title = request.json['title']       # obtener dato de json y guardarlo en variable
    content = request.json['content']

    new_guide = Guide(title, content)   # nueva isntancia de Guide

    # comunicarse con la data base
    db.session.add(new_guide)           # añadir el guide al db
    db.session.commit()

    # asegurarnos de que funciona el código
    guide = Guide.query.get(new_guide.id)
    
    return guide_schema.jsonify(guide)

# endpoint to query all guides
@app.route("/guides", methods=["GET"])
def get_guides():
    all_guides = Guide.query.all()              # devuelve todos los Guide del sistema (app)
    result = guides_schema.dump(all_guides)     # trabajaremos con el schema de múltiples

    return jsonify(result)

# endpoint for querying single guide
@app.route("/guide/<id>", methods=["GET"])
def get_guide(id):          # la función necesita que le pasemos el ID del 'guide'
    # pedimos que obtenga el elemento con el ID que se le haya pasado
    guide = Guide.query.get(id)

    return guide_schema.jsonify(guide)


if __name__ == "__main__":
    app.run(debug=True)