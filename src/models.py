from flask_sqlalchemy import SQLAlchemy

# Inicializa o objeto SQLAlchemy
db = SQLAlchemy()

# Define o modelo de dados para a cotação de frete
class FreightQuote(db.Model):
    # Tabela no banco de dados
    __tablename__ = 'freight_quotes'

    # Colunas
    id = db.Column(db.Integer, primary_key=True)
    origin_cep = db.Column(db.String(9), nullable=False)
    destination_cep = db.Column(db.String(9), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    quote_value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<FreightQuote {self.id} - R${self.quote_value}>"

# Este arquivo é necessário para que o Python reconheça 'src' como um pacote
# Você pode criar um arquivo vazio chamado src/__init__.py, mas para simplificar,
# vamos apenas usar o models.py por enquanto.
