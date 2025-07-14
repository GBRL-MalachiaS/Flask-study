from flask import render_template
from app import app


@app.route('/')
def ola_mundo():
    nome_usuario = "Maria"
    tecnologias = ["Flask", "Python", "HTML", "Jinja2"]
    return render_template('index.html', nome=nome_usuario, techs=tecnologias)


@app.route('/sobre')
def sobre():
    return '<h1>Sobre este projeto</h1>\n<p>Este é meu aprendizado de rotas e retornos de função dentro do flask</p>'

@app.route('/contato')
def contato():
    return '<h1>Informações Contato</h1>\n<p>Você pode entrar em contato pelo e-mail: ficticio@gmail.com'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'<h1>Olá, {nome}!</h1>\n<p>Bem-vindo ao meu primeiro app Flask!</p>'

@app.route('/perfil')
def perfil():
    usuario = {
        'nome': 'João',
        'cidade': 'São Paulo',
        'idade': 30,
        'email': 'Aleatório@gmail.com',
        'avatar': 'https://www.bairesdev.com/wp-content/uploads/2021/08/Flask-1.svg'
    }
    return render_template('perfil.html', usuario=usuario)

@app.route('/livros')
def livros():
    livros = [
        {'titulo': 'Flask para Iniciantes', 'autor': 'João Silva', 'ano': 2021},
        {'titulo': 'Aprendendo Python', 'autor': 'Maria Oliveira', 'ano': 2020},
        {'titulo': 'Desenvolvimento Web com Flask', 'autor': 'Carlos Souza', 'ano': 2022}
    ]
    return render_template('livros.html', livros=livros)