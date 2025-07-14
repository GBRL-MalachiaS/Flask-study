from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class FormLogin(FlaskForm):
    usuario = StringField('Usuário', validators=[DataRequired(message="Este Campo é Obrigatório")])
    senha = PasswordField('Senha', validators=[DataRequired(message="Este Campo é Obrigatório")])
    enviar = SubmitField('Enviar')
