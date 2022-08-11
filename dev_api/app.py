from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {'nome': 'Fulano',
     'habilidade': ['Python', 'Flask']
     },
    {'nome': 'Beltrano',
     'habilidade': ['Python', 'Django']
     }
]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT'])
def desenvolvedor(id):
    if request.method == 'GET':
        desenvolvedor = desenvolvedores[id]
        print(desenvolvedor)
        return jsonify(desenvolvedor)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)


if __name__ == '__main__':
    app.run(debug=True)
