from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__) 

@app.get("/") # esto es la pagina principal
def home():
    return render_template("home.html")

@app.get("/resultados")
def resultados():
    return render_template("resultados.html")

@app.get("/plan_2023")
def plan2023():
    return render_template("plan_2023.html")