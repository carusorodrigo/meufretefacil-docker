import os
from flask import Flask, render_template, request, jsonify
from src.models import db, FreightQuote # Importa o db e o modelo que você acabou de criar

# Configuração do Flask
aplicativo = Flask(__name__)

# Configuração do Banco de Dados
# O Render fornece a URL do banco de dados na variável de ambiente DATABASE_URL
# O SQLAlchemy precisa que o prefixo seja 'postgresql' e não 'postgres'
database_url = os.environ.get("DATABASE_URL")
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

aplicativo.config['SQLALCHEMY_DATABASE_URI'] = database_url
aplicativo.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados com o aplicativo
db.init_app(aplicativo)

# --- Rotas do Aplicativo ---

# Rota principal (Home)
@aplicativo.route('/')
def index():
    # O index.html que você editou será renderizado
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
        # Em caso de erro no DB, ainda retorna a cotação, mas loga o erro
        print(f"Erro ao salvar no banco de dados: {e}")
        db.session.rollback()

    return jsonify({
        "success": True,
        "quote_value": f"R$ {quote_value:.2f}",
        "message": "Cotação realizada com sucesso (simulação)."
    })

# --- Inicialização do Banco de Dados ---

# Cria as tabelas do banco de dados se elas não existirem
# Isso deve ser executado uma vez, idealmente no primeiro deploy
with aplicativo.app_context():
    db.create_all()

# O Gunicorn usará 'aplicativo' como o ponto de entrada
if __name__ == '__main__':
    # A porta é definida pelo Render na variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    aplicativo.run(host='0.0.0.0', port=port)
