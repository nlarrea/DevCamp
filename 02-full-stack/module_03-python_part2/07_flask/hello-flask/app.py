from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# crea instancia de flask y la guarda dentro de variable
app = Flask(__name__)

# le decimos a flask dónde está la base de datos
basedir = os.path.abspath(os.path.dirname(__file__))

# le pasamos el directorio al que queremos que vaya
# y le decimos que se llama 'app.sqlite'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")

# creamos un objeto base de datos
db = SQLAlchemy(app)        # instanciar objeto de SQLAlchemy
ma = Marshmallow(app)       # instanciar objeto de Marshmallow

# creamos el esquema de la tabla (heredera de db.Model)
class Guide(db.Model):
    # añadimos una columna de tipo int, y decimos que es 'primary key'
    # primary_key=True -> hará que cada Guide tenga su propio ID y que cada ID incremente automáticamente
    id = db.Column(db.Integer, primary_key=True)
    # creamos 2 columnas más de tipo str y limitamos si cantidad de chars a 100 y 144
    title = db.Column(db.String(100), unique=False)
    content = db.Column(db.String(144), unique=False)

    def __init__(self, title, content):
        self.title = title
        self.content = content


class GuideSchema(ma.Schema):
    class Meta:
        # indicamos los campos a los que queremos acceder dentro de una tupla
        fields = ("title", "content")


guide_schema = GuideSchema()                # para trabajar con un solo 'guide'
guides_schema = GuideSchema(many=True)      # para trabajar con múltiples 'guide'


# endpoint to create a new guide -> POST
@app.route("/guide", methods=["POST"])      # indicamos el verbo POST -> para añadir un guide
def add_guide():
    # obtener datos de json y guardarlos en variables
    title = request.json["title"]
    content = request.json["content"]

    new_guide = Guide(title, content)       # nueva isntancia de Guide

    # comunicarse con la data base -> añadir el guide al db
    db.session.add(new_guide)
    db.session.commit()

    # asegurarse de que funciona el código
    guide = Guide.query.get(new_guide.id)   # para obtener el guide que hemos instanciado
    return guide_schema.jsonify(guide)      # nos lo muestra


# endpoint to query all guides
@app.route("/guides", methods=["GET"])
def get_guides():
    all_guides = Guide.query.all()              # devuelve todos los guide del sistema (app)
    result = guides_schema.dump(all_guides)     # trabajaremos con el esquema de múltiples guide

    return jsonify(result)


# endpoint for querying single guide
@app.route("/guide/<id>", methods=["GET"])
def get_guide(id):      # la función necesita que le pasemos el ID del 'guide' que queremos
    # pedimos que obtenga el elemento con el ID que se le haya pasado
    guide = Guide.query.get(id)

    return guide_schema.jsonify(guide)


# endpoint for updating a guide
@app.route("/guide/<id>", methods=["PUT"])
def guide_update(id):
    guide = Guide.query.get(id)         # indicamos qué elemento queremos modificar

    # obtenemos los datos escritos para modificar el elemento
    title = request.json["title"]
    content = request.json["content"]

    # modificamos el elemento
    guide.title = title
    guide.content = content

    # guardamos los cambios
    db.session.commit()

    return guide_schema.jsonify(guide)  # devuelve el elemento modificado


# endpoint for deleting a record
@app.route("/guide/<id>", methods=["DELETE"])
def guide_delete(id):
    guide = Guide.query.get(id)

    db.session.delete(guide)
    db.session.commit()

    return "Guide was successfully deleted!"


if __name__ == "__main__":
    app.run(debug=True)