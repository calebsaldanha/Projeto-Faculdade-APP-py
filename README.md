# Controle de Estoque de Transporte - Projeto de Extensão

## Descrição do Projeto

Este projeto foi desenvolvido como parte da disciplina de Desenvolvimento Rápido de Aplicações em Python para um curso de extensão universitária. O objetivo é criar uma aplicação web para controle de estoque e agregados em operações de transporte e logística, utilizando **Flask** e **SQLite**.

O sistema permite:
- Adicionar e visualizar resumos de entregas de produtos.
- Registrar e gerenciar o controle de agregados, incluindo veículos, motoristas e fretes.

## Funcionalidades

1. **Resumo de Transporte**:
   - Registro de entregas e operações de transporte, com detalhes como peso, volume, tipo de veículo, nota fiscal, e destinatário.
   - Exibição dos resumos registrados em uma tabela no dashboard da aplicação.

2. **Controle de Agregado**:
   - Registro de dados dos agregados, como placa do veículo, motorista, cliente e valores de frete.
   - Visualização de todos os controles de agregados na aplicação.

3. **Interface amigável**:
   - Sistema de templates utilizando **Jinja2** para facilitar a adição e a visualização dos registros.
   - Mensagens de sucesso ou erro em tempo real com o **Flask Flash**.

4. **Banco de Dados**:
   - Armazenamento dos dados de resumos e controle de agregados em um banco de dados SQLite.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para o desenvolvimento da aplicação.
- **Flask**: Framework utilizado para criar a aplicação web.
- **SQLite**: Banco de dados leve utilizado para armazenar as informações.
- **Jinja2**: Template engine para gerar as páginas HTML dinamicamente.
- **HTML/CSS**: Frontend básico para a interface de usuário.
- **Bootstrap**: Framework CSS para facilitar a estilização da interface.

## Estrutura do Projeto

```bash
├── app.py                # Arquivo principal da aplicação Flask
├── db.py                 # Configuração do banco de dados
├── models.py             # Definição dos modelos de banco de dados (Resumo e ControleAgregado)
├── templates/            # Páginas HTML renderizadas
│   ├── base.html         # Template base para o layout
│   ├── resumo.html       # Página que exibe o resumo de entregas
│   ├── adicionar.html    # Página para adicionar novos resumos
│   ├── adicionar_controle.html # Página para adicionar novos controles de agregados
│   ├── controle_agregado.html  # Página que exibe os controles de agregados
├── static/               # Arquivos estáticos (CSS, JS, etc.)
│   └── styles.css        # Arquivo de estilos CSS
└── estoque.db            # Banco de dados SQLite (gerado automaticamente)
```

## Como Executar o Projeto

### Pré-requisitos
- Python 3.x
- pip

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/calebsaldanha/controle-estoque-transporte.git
   ```
   
2. Navegue até o diretório do projeto:
   ```bash
   cd controle-estoque-transporte
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicialize o banco de dados (caso ainda não tenha sido criado):
   ```bash
   python db.py
   ```

5. Execute a aplicação:
   ```bash
   python app.py
   ```

6. Acesse a aplicação no seu navegador:
   ```
   http://127.0.0.1:5000/
   ```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar **pull requests** ou abrir **issues** para relatar bugs ou sugerir melhorias.

