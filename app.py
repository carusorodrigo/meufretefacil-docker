from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
# Isso garante que o Python encontre o módulo 'src'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importações absolutas, agora que a estrutura de pacotes está correta
from src.models.user import db
import src.models # Importa todos os modelos para que o SQLAlchemy os reconheça
from src.routes.motorista import motorista_bp
from src.routes.transportadora import transportadora_bp
from src.routes.upload import upload_bp
from src.routes.historico import historico_bp
from src.routes.busca import busca_bp # Assumindo que existe um blueprint de busca

# Configuração do Flask
# O Flask agora deve encontrar os arquivos estáticos e de template corretamente
app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///freteconnect.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = '/tmp' # Pasta temporária para uploads

# Inicializa o SQLAlchemy
db.init_app(app)

# Registra os Blueprints
app.register_blueprint(motorista_bp, url_prefix='/api')
app.register_blueprint(transportadora_bp, url_prefix='/api')
app.register_blueprint(upload_bp, url_prefix='/api')
app.register_blueprint(historico_bp, url_prefix='/api')
# app.register_blueprint(busca_bp, url_prefix='/api') # Descomentar se o blueprint de busca for necessário

# Rota principal para servir o frontend
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/template-programacao', methods=['GET'])
def baixar_template_programacao():
    # Rota de template movida para upload_bp, mas mantendo a rota principal para compatibilidade ou teste
    from src.routes.upload import baixar_template_programacao as template_route
    return template_route()

if __name__ == '__main__':
    with app.app_context():
        # Cria o banco de dados e tabelas se não existirem
        db.create_all()
    import sys
    port = 5000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Porta inválida. Usando a porta padrão 5000.")
    app.run(debug=True, host='0.0.0.0', port=port)
