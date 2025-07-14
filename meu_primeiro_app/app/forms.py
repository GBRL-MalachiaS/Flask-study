from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class FromContato(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=120)])
    assunto = StringField('Assunto', validators=[DataRequired(), Length(min=2, max=100)])
    mensagem = StringField('Mensagem', validators=[DataRequired(), Length(min=10, max=500)])
    enviar = SubmitField('Enviar')