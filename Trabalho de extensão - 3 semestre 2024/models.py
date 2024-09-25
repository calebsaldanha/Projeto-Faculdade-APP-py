from db import db

# Tabela de resumo
class Resumo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    validacao_cremer = db.Column(db.String(100), nullable=False)
    periodo = db.Column(db.String(50), nullable=False)
    tipo_veiculo = db.Column(db.String(50), nullable=False)
    cte = db.Column(db.String(50), nullable=False)
    nf = db.Column(db.String(50), nullable=False)
    demais_nfs = db.Column(db.String(200), nullable=True)
    peso = db.Column(db.Float, nullable=False)
    m3 = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float, nullable=False)
    pallets = db.Column(db.Integer, nullable=False)
    valor_nf = db.Column(db.Float, nullable=False)
    dt = db.Column(db.String(50), nullable=False)
    servico = db.Column(db.String(100), nullable=False)
    destinatario = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'Resumo({self.validacao_cremer}, {self.periodo}, {self.destinatario})'

# Tabela de controle agregado
class ControleAgregado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(50), nullable=False)
    placa_cte = db.Column(db.String(20), nullable=False)
    frete_apk = db.Column(db.Float, nullable=False)
    frete_ag = db.Column(db.Float, nullable=True)
    motorista = db.Column(db.String(100), nullable=False)
    cliente = db.Column(db.String(100), nullable=False)
    romaneio = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'ControleAgregado({self.data}, {self.cliente})'
