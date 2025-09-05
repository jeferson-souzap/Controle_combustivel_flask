from flask import Flask, render_template
from blueprints.cadastro import cadastros_bp

app = Flask(__name__)

# registra o blueprint
#app.register_blueprint(cadastros_bp, url_prefix="/cadastro")

@app.route("/")
def home():
    return render_template("home.html") 


@app.route("/cadastro_marcas")
def cadastro_marcas():
    return render_template("cadastro_marcas.html")


@app.route("/cadastro_modelos")
def cadastro_modelos():
    return render_template("cadastro_modelos.html")

@app.route("/cadastro_combustivel")
def cadastro_combustivel():
    return render_template("cadastro_combustivel.html")


@app.route('/cadastro_veiculos')
def cadastro_veiculos():
    return render_template("cadastro_veiculos.html")


if __name__ == "__main__":
    app.run(debug=True)
