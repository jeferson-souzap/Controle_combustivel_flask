from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from database.db import criar_banco_dados
from database.cadastro_combustivel import (
    Cadastrar_combustivel_db, Listar_combustivel_db,
    Atualizar_combustivel, Deletar_combustivel
)
from database.crud_marcas import listar_marcas, cadastrar_marca, atualizar_marca, deletar_marca
from database.crud_modelos import (
    listar_modelos, listar_modelos_por_marca,
    cadastrar_modelo, atualizar_modelo, deletar_modelo
)
from database.crud_veiculos import (
    listar_veiculos, cadastrar_veiculo, atualizar_veiculo, deletar_veiculo
)
from database.crud_motoristas import (
    listar_motoristas, cadastrar_motorista, atualizar_motorista, deletar_motorista
)
from database.crud_rotas import (
    listar_rotas, cadastrar_rota, atualizar_rota, deletar_rota
)
from database.crud_postos import (
    listar_postos, cadastrar_posto, atualizar_posto, deletar_posto,
    listar_historico_preco, registrar_preco, deletar_historico_preco
)
from database.crud_movimentacoes import (
    listar_movimentacoes, cadastrar_movimentacao, deletar_movimentacao, stats_dashboard
)

app = Flask(__name__)
app.secret_key = "frota_secret_2024"

criar_banco_dados()


# ── Dashboard ────────────────────────────────────────────────────────────────

@app.route("/")
def home():
    stats = stats_dashboard()
    return render_template("home.html", stats=stats)


# ── Combustível ──────────────────────────────────────────────────────────────

@app.route("/cadastro_combustivel", methods=["GET", "POST"])
def cadastro_combustivel():
    if request.method == "POST":
        nome  = request.form["nomeCombustivel"]
        preco = request.form["precoCombustivel"]
        ok, msg = Cadastrar_combustivel_db(nome, preco)
        flash(msg, "success" if ok else "danger")
        return redirect(url_for("cadastro_combustivel"))

    combustiveis = Listar_combustivel_db()
    return render_template("cadastro_combustivel.html", combustiveis=combustiveis)


@app.route("/edit_combustivel/<int:cid>", methods=["POST"])
def edit_combustivel(cid):
    ok, msg = Atualizar_combustivel(
        cid,
        request.form["nomeCombustivel"],
        request.form["precoCombustivel"]
    )
    flash(msg, "success" if ok else "danger")
    return redirect(url_for("cadastro_combustivel"))


@app.route("/delete_combustivel/<int:cid>")
def delete_combustivel(cid):
    ok = Deletar_combustivel(cid)
    flash("Combustível removido." if ok else "Erro ao remover.", "success" if ok else "danger")
    return redirect(url_for("cadastro_combustivel"))


# ── Marcas ───────────────────────────────────────────────────────────────────

@app.route("/cadastro_marcas", methods=["GET", "POST"])
def cadastro_marcas():
    if request.method == "POST":
        ok, msg = cadastrar_marca(request.form["nomeMarca"])
        flash(msg, "success" if ok else "danger")
        return redirect(url_for("cadastro_marcas"))

    return render_template("cadastro_marcas.html", marcas=listar_marcas())


@app.route("/edit_marca/<int:mid>", methods=["POST"])
def edit_marca(mid):
    ok, msg = atualizar_marca(mid, request.form["nomeMarca"])
    flash(msg, "success" if ok else "danger")
    return redirect(url_for("cadastro_marcas"))


@app.route("/delete_marca/<int:mid>")
def delete_marca(mid):
    ok, msg = deletar_marca(mid)
    flash(msg, "success" if ok else "danger")
    return redirect(url_for("cadastro_marcas"))


# ── Modelos ──────────────────────────────────────────────────────────────────

@app.route("/cadastro_modelos", methods=["GET", "POST"])
def cadastro_modelos():
    if request.method == "POST":
        ok, msg = cadastrar_modelo(request.form["nomeModelo"], request.form["marcaModelo"])
        flash(msg, "success" if ok else "danger")
        return redirect(url_for("cadastro_modelos"))

    return render_template("cadastro_modelos.html",
                           modelos=listar_modelos(), marcas=listar_marcas())


@app.route("/edit_modelo/<int:mid>", methods=["POST"])
def edit_modelo(mid):
    ok, msg = atualizar_modelo(mid, request.form["nomeModelo"], request.form["marcaModelo"])
    flash(msg, "success" if ok else "danger")
    return redirect(url_for("cadastro_modelos"))


@app.route("/delete_modelo/<int:mid>")
def delete_modelo(mid):
    ok, msg = deletar_modelo(mid)
    flash(msg, "success" if ok else "danger")
    return redirect(url_for("cadastro_modelos"))


# ── Veículos ─────────────────────────────────────────────────────────────────

@app.route("/cadastro_veiculos", methods=["GET", "POST"])
def cadastro_veiculos():
    if request.method == "POST":
        ok, msg = cadastrar_veiculo(
            fk_marca_id      = request.form["marcaVeiculo"],
            fk_modelo_id     = request.form["modeloVeiculo"],
            fk_combustivel_id= request.form["combustivelVeiculo"],
            consumo_km_litro = request.form["consumoVeiculo"],
            capacidade_tanque= request.form["tanqueVeiculo"],
            ano              = request.form["anoVeiculo"],
            placa            = request.form["placaVeiculo"],
            status           = request.form["statusVeiculo"],
        )
        flash(msg, "success" if ok else "danger")
        return redirect(url_for("cadastro_veiculos"))

    return render_template("cadastro_veiculos.html",
                           veiculos=listar_veiculos(),
                           marcas=listar_marcas(),
                           combustiveis=Listar_combustivel_db())


@app.route("/edit_veiculo/<int:vid>", methods=["POST"])
def edit_veiculo(vid):
    ok, msg = atualizar_veiculo(
        veiculo_id       = vid,
        fk_marca_id      = request.form["marcaVeiculo"],
        fk_modelo_id     = request.form["modeloVeiculo"],
        fk_combustivel_id= request.form["combustivelVeiculo"],
        consumo_km_litro = request.form["consumoVeiculo"],
        capacidade_tanque= request.form["tanqueVeiculo"],
        ano              = request.form["anoVeiculo"],
        placa            = request.form["placaVeiculo"],
        status           = request.form["statusVeiculo"],
    )
    flash(msg, "success" if ok else "danger")
    return redirect(url_for("cadastro_veiculos"))


@app.route("/delete_veiculo/<int:vid>")
def delete_veiculo(vid):
    ok, msg = deletar_veiculo(vid)
    flash(msg, "success" if ok else "danger")
    return redirect(url_for("cadastro_veiculos"))


# ── Motoristas ───────────────────────────────────────────────────────────────

@app.route("/cadastro_motorista", methods=["GET", "POST"])
def cadastro_motorista():
    if request.method == "POST":
        ok, msg = cadastrar_motorista(
            nome                 = request.form["nomeMotorista"],
            cpf                  = request.form["cpfMotorista"],
            habilitacao_categoria= request.form["cnhMotorista"],
            telefone             = request.form.get("telefoneMotorista", ""),
            email                = request.form.get("emailMotorista", ""),
        )
        flash(msg, "success" if ok else "danger")
        return redirect(url_for("cadastro_motorista"))

    return render_template("cadastro_motorista.html", motoristas=listar_motoristas())


@app.route("/edit_motorista/<int:mid>", methods=["POST"])
def edit_motorista(mid):
    ok, msg = atualizar_motorista(
        motorista_id         = mid,
        nome                 = request.form["nomeMotorista"],
        cpf                  = request.form["cpfMotorista"],
        habilitacao_categoria= request.form["cnhMotorista"],
        telefone             = request.form.get("telefoneMotorista", ""),
        email                = request.form.get("emailMotorista", ""),
        status               = request.form.get("statusMotorista", "Ativo"),
    )
    flash(msg, "success" if ok else "danger")
    return redirect(url_for("cadastro_motorista"))


@app.route("/delete_motorista/<int:mid>")
def delete_motorista(mid):
    ok, msg = deletar_motorista(mid)
    flash(msg, "success" if ok else "danger")
    return redirect(url_for("cadastro_motorista"))


# ── Rotas ─────────────────────────────────────────────────────────────────────

@app.route("/cadastro_rotas", methods=["GET", "POST"])
def cadastro_rotas():
    if request.method == "POST":
        ok, msg = cadastrar_rota(
            nome        = request.form["nomeRota"],
            origem      = request.form["origemRota"],
            destino     = request.form["destinoRota"],
            distancia_km= request.form.get("distanciaRota", ""),
            descricao   = request.form.get("descricaoRota", ""),
        )
        flash(msg, "success" if ok else "danger")
        return redirect(url_for("cadastro_rotas"))

    return render_template("cadastro_rotas.html", rotas=listar_rotas())


@app.route("/edit_rota/<int:rid>", methods=["POST"])
def edit_rota(rid):
    ok, msg = atualizar_rota(
        rota_id     = rid,
        nome        = request.form["nomeRota"],
        origem      = request.form["origemRota"],
        destino     = request.form["destinoRota"],
        distancia_km= request.form.get("distanciaRota", ""),
        descricao   = request.form.get("descricaoRota", ""),
    )
    flash(msg, "success" if ok else "danger")
    return redirect(url_for("cadastro_rotas"))


@app.route("/delete_rota/<int:rid>")
def delete_rota(rid):
    ok, msg = deletar_rota(rid)
    flash(msg, "success" if ok else "danger")
    return redirect(url_for("cadastro_rotas"))


# ── Postos ────────────────────────────────────────────────────────────────────

@app.route("/cadastro_postos", methods=["GET", "POST"])
def cadastro_postos():
    if request.method == "POST":
        ok, msg = cadastrar_posto(
            nome    = request.form["nomePosto"],
            endereco= request.form.get("enderecoPosto", ""),
            cidade  = request.form.get("cidadePosto", ""),
            estado  = request.form.get("estadoPosto", ""),
        )
        flash(msg, "success" if ok else "danger")
        return redirect(url_for("cadastro_postos"))

    return render_template("cadastro_postos.html",
                           postos=listar_postos(),
                           historico=listar_historico_preco(),
                           combustiveis=Listar_combustivel_db())


@app.route("/edit_posto/<int:pid>", methods=["POST"])
def edit_posto(pid):
    ok, msg = atualizar_posto(
        posto_id= pid,
        nome    = request.form["nomePosto"],
        endereco= request.form.get("enderecoPosto", ""),
        cidade  = request.form.get("cidadePosto", ""),
        estado  = request.form.get("estadoPosto", ""),
    )
    flash(msg, "success" if ok else "danger")
    return redirect(url_for("cadastro_postos"))


@app.route("/delete_posto/<int:pid>")
def delete_posto(pid):
    ok, msg = deletar_posto(pid)
    flash(msg, "success" if ok else "danger")
    return redirect(url_for("cadastro_postos"))


@app.route("/registrar_preco", methods=["POST"])
def add_historico_preco():
    ok, msg = registrar_preco(
        fk_posto_id      = request.form["postoPreco"],
        fk_combustivel_id= request.form["combustivelPreco"],
        preco_litro      = request.form["precoLitro"],
        data_coleta      = request.form["dataPreco"],
    )
    flash(msg, "success" if ok else "danger")
    return redirect(url_for("cadastro_postos"))


@app.route("/delete_preco/<int:hid>")
def delete_preco(hid):
    ok, msg = deletar_historico_preco(hid)
    flash(msg, "success" if ok else "danger")
    return redirect(url_for("cadastro_postos"))


# ── Movimentações ─────────────────────────────────────────────────────────────

@app.route("/movimentacoes", methods=["GET", "POST"])
def movimentacoes():
    if request.method == "POST":
        abasteceu = 1 if request.form.get("abasteceu") == "on" else 0
        ok, msg = cadastrar_movimentacao(
            fk_veiculo_id   = request.form["veiculoMovimentacao"],
            fk_motorista_id = request.form["motoristaMovimentacao"],
            data_movimento  = request.form["dataMovimentacao"],
            km_inicial      = request.form.get("kmInicialMovimentacao") or None,
            km_final        = request.form.get("kmFinalMovimentacao") or None,
            abasteceu       = abasteceu,
            litros          = request.form.get("litrosMovimentacao") or None,
            valor           = request.form.get("valorMovimentacao") or None,
            fk_rota_id      = request.form.get("rotaMovimentacao") or None,
            fk_posto_id     = request.form.get("postoMovimentacao") or None,
            nivel_tanque    = request.form.get("nivelTanque") or None,
            observacao      = request.form.get("observacaoMovimentacao") or None,
        )
        flash(msg, "success" if ok else "danger")
        return redirect(url_for("movimentacoes"))

    return render_template("movimentacoes.html",
                           movimentacoes=listar_movimentacoes(),
                           veiculos=listar_veiculos(),
                           motoristas=listar_motoristas(),
                           rotas=listar_rotas(),
                           postos=listar_postos())


@app.route("/delete_movimentacao/<int:mid>")
def delete_movimentacao(mid):
    ok, msg = deletar_movimentacao(mid)
    flash(msg, "success" if ok else "danger")
    return redirect(url_for("movimentacoes"))


# ── API JSON para dropdowns dinâmicos ─────────────────────────────────────────

@app.route("/api/modelos")
def api_modelos():
    marca_id = request.args.get("marca_id")
    if marca_id:
        return jsonify(listar_modelos_por_marca(marca_id))
    return jsonify(listar_modelos())


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
