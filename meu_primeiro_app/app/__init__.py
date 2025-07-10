# app/__init__.py

from flask import Flask

# 1. Cria a instância da aplicação Flask
#    Agora, a variável 'app' pertence ao pacote 'app'.
app = Flask(__name__)

# 2. Importa as rotas DEPOIS da criação da instância do app
#    Isso é crucial para evitar "importações circulares". O arquivo routes.py
#    precisará importar a variável 'app' que acabamos de criar aqui.
from app import routes
