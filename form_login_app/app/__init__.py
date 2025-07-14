from flask import Flask 


app = Flask(__name__)

app.config['SECRET_KEY']= 'Lorena@2402'

from app import routes