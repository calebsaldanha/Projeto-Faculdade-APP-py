# Projeto_Extensão_Faculdade
Repositório destinado para o armazenamento do Projeto de extensão da Faculdade de Ciências da Computação. Matéria: Desenvolvimento Rápido de Aplicações em Python


# Controle de Estoque

Este é um projeto simples de Controle de Estoque desenvolvido com Flask, onde é possível adicionar produtos e registrar movimentações (entrada e saída) de estoque. A aplicação utiliza um banco de dados SQLite para armazenar as informações dos produtos e suas movimentações.

## Tecnologias Utilizadas

- Python
- Flask
- SQLAlchemy
- SQLite
- Bootstrap (para o design)

## Funcionalidades

- **Visualizar Estoque**: Mostra a lista de produtos e suas quantidades.
- **Adicionar Produto**: Permite adicionar novos produtos ao estoque.
- **Registrar Movimentação**: Possibilita registrar entradas e saídas de produtos do estoque.

## Estrutura do Projeto

```
/seu_projeto
│
├── app.py                 # Arquivo principal da aplicação
├── db.py                  # Configuração do banco de dados
├── models.py              # Modelos de dados
├── static                 # Diretório para arquivos estáticos (CSS, JS, etc.)
│   └── styles.css         # Estilos personalizados
└── templates              # Diretório para arquivos HTML
    ├── base.html         # Layout base
    ├── estoque.html      # Página do estoque
    ├── adicionar.html     # Página para adicionar produtos
    └── movimentacao.html  # Página para registrar movimentações
```

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu_usuario/seu_projeto.git
   cd seu_projeto
   ```

2. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
   ```

3. Instale as dependências:

   ```bash
   pip install Flask Flask-SQLAlchemy
   ```

4. Crie o banco de dados:

   Execute o arquivo `setup_db.py` para criar o banco de dados e as tabelas necessárias:

   ```bash
   python setup_db.py
   ```

5. Execute a aplicação:

   ```bash
   python app.py
   ```

   A aplicação estará disponível em `http://127.0.0.1:5000`.

## Como Contribuir

Sinta-se à vontade para contribuir com melhorias! Para isso:

1. Faça um fork do projeto.
2. Crie uma nova branch:
   ```bash
   git checkout -b minha-nova-contribuicao
   ```
3. Faça suas alterações e commit:
   ```bash
   git commit -m 'Adicionei uma nova funcionalidade'
   ```
4. Envie para o seu repositório:
   ```bash
   git push origin minha-nova-contribuicao
   ```
5. Abra um Pull Request.
