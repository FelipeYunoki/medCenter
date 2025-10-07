from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do MySQL (ajuste o user, password, host)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:suaSenha@localhost/medcenter'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Agendamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))
    especialidade = db.Column(db.String(50))
    mensagem = db.Column(db.Text)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agendar', methods=['POST'])
def agendar():
    nome = request.form['nome']
    telefone = request.form['telefone']
    email = request.form['email']
    especialidade = request.form['especialidade']
    mensagem = request.form['mensagem']

    novo = Agendamento(nome=nome, telefone=telefone, email=email, especialidade=especialidade, mensagem=mensagem)
    db.session.add(novo)
    db.session.commit()

    return redirect('/') 

if __name__ == '__main__':
    app.run(debug=True)
