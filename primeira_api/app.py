from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/<int:id>')  # a tipagem evita erros
def pessoas(id):
    soma = 1 + id
    return jsonify({'id': id,
                    'nome': 'Bernardo',
                    'profissao': 'fudido'
                    })


# @app.route('/soma/<int:valor1>/<int:valor2>/')
# def soma(valor1, valor2):
#    return jsonify({'soma': valor1 + valor2})

@app.route('/soma', methods=['POST', 'GET'])
def soma():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['valores'])
    elif request.method == 'GET':
        total = 1
    return jsonify({'soma': total})


if __name__ == '__main__':
    app.run(debug=True)
