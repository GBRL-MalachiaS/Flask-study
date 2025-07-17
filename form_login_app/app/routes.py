from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import FormLogin, FormCadastro
from app.models import Usuario
from app import db


@app.route('/', methods=['GET', 'POST'])
def login():
    form = FormLogin()
    if form.validate_on_submit():
        # 1. Busca no banco de dados por um usuário com o nome fornecido
        usuario = Usuario.query.filter_by(nome=form.usuario.data).first()

        # 2. Verifica se o usuário existe E se a senha está correta
        if usuario is None or not usuario.check_password(form.senha.data):
            flash('Nome de usuário ou senha inválidos!', 'danger')
            return redirect(url_for('login'))

        # Se o usuário e a senha estiverem corretos:
        flash(f'Login bem-sucedido para o usuário {usuario.nome}!', 'success')
        return redirect(url_for('logado'))

    return render_template('login.html', titulo='Login', form=form)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = FormCadastro()
    if form.validate_on_submit():
        # 2. Cria uma instância do nosso modelo Usuario com os dados do formulário
        novo_usuario = Usuario(nome=form.nome.data, email=form.email.data)
        # 3. Usa nosso novo método para definir a senha de forma segura
        novo_usuario.set_password(form.senha.data)

        # 4. Adiciona o novo usuário à "sessão" do banco de dados
        db.session.add(novo_usuario)
        # 5. "Comita" (salva) as mudanças no banco de dados
        db.session.commit()

        flash('Cadastro realizado com sucesso! Por favor, faça o login.', 'success')
        return redirect(url_for('login'))

    return render_template('cadastro.html', titulo='Cadastro', form=form)


@app.route('/logado')
def logado():
    return render_template('index.html')
