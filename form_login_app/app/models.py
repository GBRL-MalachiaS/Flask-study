# app/models.py

# Importa a instância 'db' que criamos no __init__.py
from app import db
# 1. Importe as funções de hash da biblioteca werkzeug (que já vem com o Flask)
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(db.Model):
    """Representa a tabela de usuários no banco de dados."""
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    # NUNCA salvamos a senha em texto puro!
    senha_hash = db.Column(db.String(128))

    def set_password(self, senha):
        """Recebe uma senha em texto puro e a armazena como um hash."""
        self.senha_hash = generate_password_hash(senha)

    def check_password(self, senha):
        """Recebe uma senha em texto puro e retorna True se ela corresponder ao hash armazenado."""
        return check_password_hash(self.senha_hash, senha)

    def __repr__(self):
        # O __repr__ nos dá uma representação útil do objeto ao debugá-lo.
        return f'<Usuario {self.nome}>'
