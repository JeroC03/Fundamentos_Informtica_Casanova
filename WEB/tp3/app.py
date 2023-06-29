from flask import Flask, render_template, request, redirect, url_for, jsonify
from markupsafe import escape
# from flask_wtf.csrf import generate_csrf

app = Flask(__name__) 

productos = {
    1:{"numero": 1, "Producto": "Shampoo sólido", "Stock": 5, "Precio_unitario": 300},
    2:{"numero": 2, "Producto": "Crema de manos", "Stock": 6, "Precio_unitario": 600},
    3:{"numero": 3, "Producto": "Crema de pies", "Stock": 2, "Precio_unitario": 100}
}

@app.get("/")
def home():
    return render_template("home.html")

@app.route("/productos", methods=["GET"])
def obtener_productos():
    return render_template("productos.html", productos=productos.values())   

@app.route("/productos/<int:numero>")
def obtener_producto(numero):
    if numero in productos:
        producto = productos[numero]
        return render_template("producto.html", producto=producto)
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 404
    
@app.route("/productos/<int:numero>", methods=["POST"])
def eliminar_producto(numero):
    if numero in productos:
        del productos[numero]
        return redirect("/productos")
    else:
        return jsonify({"mensaje": "Producto no encontrado"}), 404