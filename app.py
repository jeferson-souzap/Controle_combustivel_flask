from flask import Flask, render_template
from blueprints.cadastro import cadastros_bp

app = Flask(__name__)

# registra o blueprint
app.register_blueprint(cadastros_bp, url_prefix="/cadastro")

@app.route("/")
def home():
    return render_template("home.html") 

if __name__ == "__main__":
    app.run(debug=True)
