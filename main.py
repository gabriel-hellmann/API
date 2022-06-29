from flask import Flask, jsonify, render_template
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<data>')
def tempo(data):
    hoje = datetime.date.today()
    aniversario = datetime.date(int(data[6:10]),     
int(data[3:5]), int(data[:2]))


    qtd_dias = hoje - aniversario
    qtd_dias = qtd_dias.days

    return jsonify({'Quantidade de dias': qtd_dias})


app.run(host='0.0.0.0')