
# run.py

# Importa a instância 'app' de dentro do nosso pacote 'app'.
from app import app

# Inicia o servidor, exatamente como antes.
if __name__ == '__main__':
    app.run(debug=True)