from flask import render_template, flash, redirect, url_for
from app.forms import FromContato
from app import app


@app.route('/')
def ola_mundo():
    nome_usuario = "Maria"
    tecnologias = ["Flask", "Python", "HTML", "Jinja2"]
    return render_template('index.html', nome=nome_usuario, techs=tecnologias)


@app.route('/sobre')
def sobre():
    return '<h1>Sobre este projeto</h1>\n<p>Este é meu aprendizado de rotas e retornos de função dentro do flask</p>'

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    form = FromContato()
    if form.validate_on_submit():
        nome_do_usuario = form.nome.data
        email_do_usuario = form.email.data
        flash(f'Contato enviado por {nome_do_usuario} com o email {email_do_usuario}!')
        return redirect(url_for('ola_mundo'))
    
    return render_template('contato.html', titulo='Entre em Contato', form=form)


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