from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
# Isso garante que o Python encontre o módulo 'src'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importações absolutas, agora que a estrutura de pacotes está correta
#from src.models.user import db
#import src.models # Importa todos os modelos para que o SQLAlchemy os reconheça
#from src.routes.motorista import motorista_bp
#from src.routes.transportadora import transportadora_bp
#from src.routes.upload import upload_bp
#from src.routes.historico import historico_bp
#from src.routes.busca import busca_bp # Assumindo que existe um blueprint de busca

# Configuração do Flask
# O Flask agora deve encontrar os arquivos estáticos e de template corretamente
aplicativo = Flask(__name__, static_folder='static', template_folder='templates')
aplicativo.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///freteconnect.db'
aplicativo.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
aplicativo.config['UPLOAD_FOLDER'] = '/tmp' # Pasta temporária para uploads

# Inicializa o SQLAlchemy
# db.init_app(app)

# Registra os Blueprints
# aplicativo.register_blueprint(motorista_bp, url_prefix='/api')
# aplicativo.register_blueprint(transportadora_bp, url_prefix='/api')
# aplicativo.register_blueprint(upload_bp, url_prefix='/api')
# aplicativo.register_blueprint(historico_bp, url_prefix='/api')
# aplicativo.register_blueprint(busca_bp, url_prefix='/api') # Descomentar se o blueprint de busca for necessário

Rota principal para servir o frontend
@aplicativo.route('/')
def index():
return render_template('index.html')

# @aplicativo.route('/api/template-programacao', methods=['GET'])
# def baixar_template_programacao():
# Rota de template movida para upload_bp, mas mantendo a rota principal para compatibilidade ou teste
# from src.routes.upload import baixar_template_programacao as template_route
# return template_route()


