from flask import Flask, render_template, request, redirect, url_for, flash
from db import db  # Importar a instância do banco de dados
from models import Resumo, ControleAgregado  # Importar os modelos
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estoque.db'
app.config['SECRET_KEY'] = '231605'
db.init_app(app)  # Inicializar o banco de dados

# Página inicial (exibe o resumo)
@app.route('/')
def resumo():
    resumos = Resumo.query.all()
    return render_template('resumo.html', resumos=resumos)

# Adicionar um novo resumo
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        # Capturando dados do formulário
        dados_resumo = {
            'validacao_cremer': request.form['validacao_cremer'],
            'periodo': request.form['periodo'],
            'tipo_veiculo': request.form['tipo_veiculo'],
            'cte': request.form['cte'],
            'nf': request.form['nf'],
            'demais_nfs': request.form['demais_nfs'],
            'peso': request.form['peso'],
            'm3': request.form['m3'],
            'volume': request.form['volume'],
            'pallets': request.form['pallets'],
            'valor_nf': request.form['valor_nf'],
            'dt': request.form['dt'],
            'servico': request.form['servico'],
            'destinatario': request.form['destinatario']
        }

        novo_resumo = Resumo(**dados_resumo)

        try:
            db.session.add(novo_resumo)
            db.session.commit()
            flash('Resumo adicionado com sucesso!', 'success')
            return redirect(url_for('resumo'))
        except Exception as e:
            flash(f'Erro ao adicionar resumo: {e}', 'danger')
    
    return render_template('adicionar.html')

# Adicionar um novo controle de agregado
@app.route('/adicionar_controle', methods=['GET', 'POST'])
def adicionar_controle():
    if request.method == 'POST':
        dados_controle = {
            'data': request.form['data'],
            'placa_cte': request.form['placa_cte'],
            'frete_apk': request.form['frete_apk'],
            'frete_ag': request.form['frete_ag'],
            'motorista': request.form['motorista'],
            'cliente': request.form['cliente'],
            'romaneio': request.form['romaneio']
        }

        novo_controle = ControleAgregado(**dados_controle)

        try:
            db.session.add(novo_controle)
            db.session.commit()
            flash('Controle adicionado com sucesso!', 'success')
            return redirect(url_for('controle_agregado'))
        except Exception as e:
            flash(f'Erro ao adicionar controle: {e}', 'danger')
    
    return render_template('adicionar_controle.html')

# Controle de agregado
@app.route('/controle_agregado', methods=['GET', 'POST'])
def controle_agregado():
    controles = ControleAgregado.query.all()
    return render_template('controle_agregado.html', controles=controles)

if __name__ == '__main__':
    app.run(debug=True)
