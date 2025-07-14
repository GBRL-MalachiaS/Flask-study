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
                flash("Login Realizado")
                return render_template('index.html')
            else:
                flash("Login Invalido! ")
                return render_template("login.html", form=form)

    return render_template('login.html', titulo='Login', form=form)
