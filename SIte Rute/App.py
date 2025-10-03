from flask import Flask, render_template
import mysql.connector

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'ggg'  # Chave secreta para a sessão do Flask

# Configuração do MySQL
DATABASE = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Substitua pela sua senha, se houver
    'database': 'test'  # Nome do banco de dados
}

# Função para conectar ao banco de dados MySQL
def connect_db():
    try:
        return mysql.connector.connect(**DATABASE)
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None






@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

