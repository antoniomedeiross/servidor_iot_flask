from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temperatura.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Temperatura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperatura = db.Column(db.Float, nullable=False)
    data_hora = db.Column(db.DateTime, default=db.func.current_timestamp())


    def __repr__(self):
        return f"Temperatura {self.temperatura}>"
with app.app_context():
    db.create_all()


# Rotas
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/temperatura", methods=["POST"])
def temperatura_post():
    dados = request.get_json()
    temperatura = dados.get("temperatura")

    if temperatura:
        novaTemp = Temperatura(temperatura=float(temperatura))
        dataHora = novaTemp.data_hora
        db.session.add(novaTemp)
        db.session.commit()
        return jsonify({"mensagem":f"Temperatura:{temperatura}°C salva com sucesso!"}), 201
    else:
        return ({"erro": "Nenhuma temperatura fornecida."}),400

# Retora a temperatura GET
@app.route("/temperatura", methods=["GET"])
def temperatura_get():
    ultimaTemp = Temperatura.query.order_by(Temperatura.id.desc()).first()
    if ultimaTemp:
        return f"Última temperatura registrada: {ultimaTemp.temperatura}°C"
    else:
        return "Nenhuma temperatura registrada."

@app.route("/todas_temperaturas", methods=["GET"])
def todas_temperaturas():
    temperaturas = Temperatura.query.all()
    return render_template("todas_temperaturas.html", temperaturas=temperaturas)