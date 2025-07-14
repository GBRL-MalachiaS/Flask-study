from flask import render_template
from app import app

posts = {
    1: {
        'titulo': 'Meu Primeiro Post',
        'conteudo': 'Este é o conteúdo do meu primeiro post no blog.',
        'autor': 'João Silva',
        'data': '2023-10-01'
    },
    2: {
        'titulo': 'Aprendendo Flask',
        'conteudo': 'Flask é um microframework para Python que facilita o desenvolvimento web.',
        'autor': 'Maria Oliveira',
        'data': '2023-10-02'
    },
    3: {
        'titulo': 'Dicas de Programação',
        'conteudo': 'Sempre comente seu código e mantenha uma boa organização dos arquivos.',
        'autor': 'Carlos Souza',
        'data': '2023-10-03'
    }
}


@app.route('/')
def ola():
    return render_template('index.html')


@app.route('/blog/<id>')
def blog(id):
    post_id = int(id)
    return render_template('blog.html', post=posts[post_id])


@app.route('/post/<id>')
def post_individual(id):
    post_id = int(id)
    if post_id not in posts:
        return "Post não encontrado", 404
    return render_template('blog.html', post=posts[post_id])
