import os
from flask import Flask, render_template, request, jsonify
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from src.models import db, FreightQuote

# Configuração do Flask
aplicativo = Flask(__name__)

# Configuração do Banco de Dados
database_url = os.environ.get("DATABASE_URL")
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

aplicativo.config['SQLALCHEMY_DATABASE_URI'] = database_url
aplicativo.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
aplicativo.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'uma-chave-secreta-padrao-muito-segura') # Chave secreta para o Flask-Admin

# Inicializa o banco de dados com o aplicativo
db.init_app(aplicativo)

# --- Configuração do Painel de Administração (Flask-Admin) ---
admin = Admin(aplicativo, name='Meu Frete Fácil Admin', template_mode='bootstrap3')

# Adiciona o modelo de cotação de frete ao painel de administração
admin.add_view(ModelView(FreightQuote, db.session, name='Cotações de Frete'))

# --- Rotas do Aplicativo ---

# Rota principal (Home)
@aplicativo.route('/')
def index():
    return render_template('index.html')

# Rota de cotação de frete (simulada)
@aplicativo.route('/quote', methods=['POST'])
def quote_freight():
    data = request.get_json()
    
    # Validação básica
    if not all(k in data for k in ("origin_cep", "destination_cep", "weight")):
        return jsonify({"error": "Dados incompletos"}), 400

    # Simulação de cálculo de frete
    try:
        weight = float(data['weight'])
        # Lógica de simulação: R$ 10 + R$ 5 por kg
        quote_value = 10.00 + (weight * 5.00)
    except ValueError:
        return jsonify({"error": "Peso inválido"}), 400

    # Salva a cotação no banco de dados
    try:
        new_quote = FreightQuote(
            origin_cep=data['origin_cep'],
            destination_cep=data['destination_cep'],
            weight=weight,
            quote_value=quote_value
        )
        db.session.add(new_quote)
        db.session.commit()
    except Exception as e:
        print(f"Erro ao salvar no banco de dados: {e}")
        db.session.rollback()

    return jsonify({
        "success": True,
        "quote_value": f"R$ {quote_value:.2f}",
        "message": "Cotação realizada com sucesso (simulação)."
    })

# --- Inicialização do Banco de Dados ---

with aplicativo.app_context():
    db.create_all()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    aplicativo.run(host='0.0.0.0', port=port)
