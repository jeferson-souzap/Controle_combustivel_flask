from flask import Blueprint, render_template, request, redirect, url_for


cadastros_bp = Blueprint("cadastro", __name__, template_folder="../templates")

@cadastros_bp.route("/")
def index():    
    return render_template("cadastro.html")
