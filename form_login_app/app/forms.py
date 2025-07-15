from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


class FormLogin(FlaskForm):
    usuario = StringField('Usuário', validators=[
        DataRequired(message="Este Campo é Obrigatório")])
    senha = PasswordField('Senha', validators=[
        DataRequired(message="Este Campo é Obrigatório")])
    lembrar_me = BooleanField('Lembrar-me')
    enviar = SubmitField('Enviar')


class FormCadastro(FlaskForm):
    nome = StringField("Nome de Usuário", validators=[
        DataRequired(message="Campo obrigatório!"),
        Length(min=4, max=25, message="O nome de usuário deve ter entre 4 a 25 caracteres!")]) # type: ignore
    email = StringField("E-mail", validators=[DataRequired(message="Campo Obrigatório!")])
    senha = PasswordField("Senha", validators=[
        DataRequired(message="Campo Obrigatório!"),
        Length(min=8, message="A senha deve ter no minimo 8 caracteres")]) # type: ignore
    senha_confirmacao = PasswordField("Confirme sua senha", validators=[EqualTo('senha', message="As senhas devem ser identicas!")])
    enviar = SubmitField("Criar Conta")
