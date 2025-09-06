from flask import Flask, render_template, request, redirect, url_for, flash


from database.cadastro_combustivel import Cadastrar_combustivel_db

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



@app.route("/cadastro_combustivel", methods=["GET", "POST"])
def cadastro_combustivel():
    if request.method == "GET":
        return render_template("cadastro_combustivel.html")
    
    if request.method == "POST":
        nomeCombustivel = request.form["nomeCombustivel"]
        precoCombustivel = request.form['precoCombustivel']

        sucesso, msg = Cadastrar_combustivel_db(nomeCombustivel, precoCombustivel)

        if sucesso:
            flash(msg, "success")
        else:
            flash(msg, "danger")

        return redirect(url_for("cadastro_combustivel"))


@app.route('/cadastro_veiculos')
def cadastro_veiculos():
    return render_template("cadastro_veiculos.html")


@app.route('/cadastro_motorista')
def cadastro_motorista():
    return render_template("cadastro_motorista.html")

@app.route('/movimentacoes')
def movimentacoes():
    return render_template("movimentacoes.html")



if __name__ == "__main__":
    app.run(debug=True)
