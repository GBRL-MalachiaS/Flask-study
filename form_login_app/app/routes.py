from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import FormLogin

usuarios = {
    "gabriel": "minhasenha"
}


@app.route('/', methods=['GET', 'POST'])
def login():
    form = FormLogin()

    if form.validate_on_submit():

        login = form.usuario.data
        senha = form.senha.data

        if login in usuarios:
            if usuarios[login.lower()] == senha:
                flash(
                    f'Login solicitado para o usuário {form.usuario.data}, Lembrar-me={form.lembrar_me.data}')
                return render_template('index.html')
            else:
                flash("Usuário ou senha inválidos!")
                return render_template("login.html", form=form)

    return render_template('login.html', titulo='Login', form=form)
