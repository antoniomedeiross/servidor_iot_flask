from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temperatura.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()
SENHA = os.getenv("SENHA")
class Temperatura(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperatura = db.Column(db.Float, nullable=False)
    data_hora = db.Column(db.DateTime, default=db.func.current_timestamp())


    def __repr__(self):
        return f"Temperatura {self.temperatura}>°C @ {self.data_hora}"
with app.app_context():
    db.create_all()


# Rotas
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/temperatura", methods=["POST"])
def temperatura_post():
    token = request.headers.get("Authorization")
    if token != SENHA:
        return ({"erro": "Acesso não autorizado."}), 401
    else:
        dados = request.get_json()
        temperatura = dados.get("temperatura")

        if temperatura:
            try:
                novaTemp = Temperatura(temperatura=float(temperatura))
            except:
                return ({"erro": "temperatura inválida."})
            db.session.add(novaTemp)
            db.session.commit()
            return jsonify({"mensagem":f"Temperatura:{temperatura}°C salva com sucesso!",
                            "data/hora": novaTemp.data_hora.isoformat()}), 201
        else:
            return ({"erro": "Nenhuma temperatura fornecida."}),400

# Retora a temperatura GET
@app.route("/temperatura", methods=["GET"])
def temperatura_get():
    ultimaTemp = Temperatura.query.order_by(Temperatura.id.desc()).first()
    if ultimaTemp:
        return render_template("ultima_temperatura.html", temperatura= ultimaTemp.temperatura)
    else:
        return "Nenhuma temperatura registrada."

@app.route("/todas_temperaturas", methods=["GET"])
def todas_temperaturas():
    temperaturas = Temperatura.query.all()
    return render_template("todas_temperaturas.html", temperaturas=temperaturas)