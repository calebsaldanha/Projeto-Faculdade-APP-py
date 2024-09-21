# Projeto de Extensão Faculdade
Repositório destinado para o armazenamento do Projeto de extensão da Faculdade de Ciências da Computação. Matéria: Desenvolvimento Rápido de Aplicações em Python


# Controle de Estoque - Projeto de Extensão

Este projeto foi desenvolvido como parte do trabalho de extensão na disciplina de Desenvolvimento Rápido de Aplicações em Python. O objetivo principal é criar uma aplicação funcional de Controle de Estoque, permitindo a gestão eficiente de produtos e suas movimentações. Esta iniciativa busca aplicar os conhecimentos adquiridos ao longo do curso e contribuir com uma solução prática para a área de gestão de estoques.

## Motivação

A gestão de estoque é uma parte crítica em diversas áreas, desde pequenas empresas até grandes indústrias. Um controle inadequado pode levar a perdas financeiras e à insatisfação dos clientes. Este projeto visa:

- **Praticidade**: Oferecer uma ferramenta simples e intuitiva para gerenciar produtos.
- **Aprimoramento das Habilidades**: Permitir a aplicação de conceitos de programação, bancos de dados e desenvolvimento web.
- **Contribuição**: Apresentar uma solução que pode ser ampliada e utilizada por pessoas que desejam gerenciar seu estoque de maneira eficiente.

## Tecnologias Utilizadas

- **Python**
- **Flask**: Para o desenvolvimento web.
- **SQLAlchemy**: Para a manipulação do banco de dados.
- **SQLite**: Como banco de dados local.
- **Bootstrap**: Para estilização da interface.

## Funcionalidades

- **Visualizar Estoque**: Exibição de produtos e suas quantidades atuais.
- **Adicionar Produto**: Opção para adicionar novos produtos ao estoque.
- **Registrar Movimentação**: Permite registrar entradas e saídas de produtos do estoque.

## Estrutura do Projeto

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
