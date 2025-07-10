from flask import render_template
from app import app


@app.route('/')
def ola_mundo():
    nome_usuario = "Maria"
    tecnologias = ["Flask", "Python", "HTML", "Jinja2"]
    return render_template('index.html', nome=nome_usuario, techs=tecnologias)
