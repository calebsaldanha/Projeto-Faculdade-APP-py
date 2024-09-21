from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from db import db  # Importar a instância do banco de dados
from models import Produto, Movimentacao  # Importar os modelos

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estoque.db'
app.config['SECRET_KEY'] = '231605'
db.init_app(app)  # Inicializar o banco de dados

# Página inicial (exibe o estoque)
@app.route('/')
def estoque():
    produtos = Produto.query.all()
    return render_template('estoque.html', produtos=produtos)

# Adicionar um novo produto
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        quantidade = int(request.form['quantidade'])
        novo_produto = Produto(nome=nome, quantidade=quantidade)
        
        try:
            db.session.add(novo_produto)
            db.session.commit()
            flash('Produto adicionado com sucesso!', 'success')
            return redirect(url_for('estoque'))
        except:
            flash('Erro ao adicionar produto.', 'danger')
    
    return render_template('adicionar.html')

# Registrar movimentação (entrada ou saída de estoque)
@app.route('/movimentacao', methods=['GET', 'POST'])
def movimentacao():
    produtos = Produto.query.all()
    
    if request.method == 'POST':
        produto_id = request.form['produto']
        tipo = request.form['tipo']
        quantidade = int(request.form['quantidade'])
        produto = Produto.query.get(produto_id)
        
        if tipo == 'entrada':
            produto.quantidade += quantidade
        elif tipo == 'saida' and produto.quantidade >= quantidade:
            produto.quantidade -= quantidade
        else:
            flash('Quantidade insuficiente no estoque!', 'danger')
            return redirect(url_for('movimentacao'))
        
        nova_movimentacao = Movimentacao(produto_id=produto_id, tipo=tipo, quantidade=quantidade)
        
        try:
            db.session.add(nova_movimentacao)
            db.session.commit()
            flash('Movimentação registrada com sucesso!', 'success')
            return redirect(url_for('estoque'))
        except:
            flash('Erro ao registrar movimentação.', 'danger')
    
    return render_template('movimentacao.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)
