from db import db
from datetime import datetime

# Tabela de produtos
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self):
        return f'Produto({self.nome}, {self.quantidade})'

# Tabela de movimentações de estoque (entrada e saída)
class Movimentacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    tipo = db.Column(db.String(10), nullable=False)  # entrada ou saída
    quantidade = db.Column(db.Integer, nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)

    produto = db.relationship('Produto', backref='movimentacoes', lazy=True)

    def __repr__(self):
        return f'Movimentacao({self.tipo}, {self.quantidade}, {self.data})'
