# app/__init__.py

from flask import Flask
# 1. Importe a biblioteca SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Lorena@2402'

# 2. Configure o caminho do banco de dados
#    Isto diz ao SQLAlchemy para criar um arquivo de banco de dados chamado 'meubanco.db'
#    na raiz do nosso projeto.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Opcional: desativa avisos

# 3. Crie a instância do banco de dados, associando-a à nossa aplicação
db = SQLAlchemy(app)

# A importação das rotas e modelos deve vir DEPOIS da inicialização do app e do db
from app import routes, models