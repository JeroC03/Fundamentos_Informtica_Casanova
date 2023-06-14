from flask import Flask, render_template
from markupsafe import escape

prendas = [
    {"id":1,"tipo": "pantalon", "talle": 42}, 
    {"id":2,"tipo": "pantalon", "talle": 56}
]

app = Flask(__name__) 

@app.get("/") # esto es la pagina principal
def home():
    return render_template("home.html")

@app.get("/prendas")
def get_all_prendas():
    return f'<p>Mostrando todas las prendas</p>'

@app.get("/prendas/<id>")
def get_prenda(id):
    return f"<p>Mostrando la prenda {escape(id)}</p>"