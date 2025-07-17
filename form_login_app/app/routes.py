from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import FormLogin, FormCadastro

usuarios = {
    1: {
        'Nome': 'Gabriel',
        'Senha': 'Lorena@2402.',
        'e-mail': 'gbl.malachias@gmail.com'
    }
}


@app.route('/', methods=['GET','POST'])
def login():
    form = FormLogin()

    if form.validate_on_submit():

        login = form.usuario.data
        senha = form.senha.data

        for id, usuario in usuarios.items():
            if usuario['Nome'] == login and usuario['Senha'] == senha:
                flash('Login foi validado! ')
                return redirect({url_for('/logado')})

        flash('Usuario invalido!')
        return render_template('login.html', titulo='Login', form=form)
    return render_template('login.html', titulo='Login', form=form)


@app.route('/cadastro', methods=['GET','POST'])
def cadastro():
    form = FormCadastro()

    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        senha = form.senha.data
        senha_confirmacao = form.senha_confirmacao.data

        for id, usuario in usuarios.items():

            if nome == usuario['Nome']:
                flash('Usuário já possui cadastro')
                return render_template('cadastro.html', titulo='Cadastro', form=form)
        
        if senha == senha_confirmacao:
            usuarios.update({
                len(usuarios):{
                    'Nome':nome,
                    'E-mail':email,
                    'Senha':senha
                }})
            flash(f'Usuário {nome} foi cadastrado! ')
            return redirect(url_for('logado'))
        else:
            flash('Senha não batem!')
            

    return render_template('cadastro.html', titulo='Cadastro', form=form)


@app.route('/logado')
def logado():
    return render_template('index.html')
