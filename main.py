import json

from flask import Flask, send_file, jsonify

app = Flask(__name__)

livros = [{
    "nome":"Relampago marquinhos",
    "editora":"num sei cathcau"

},{
    "nome":"teste de morte",
    "editora":"Eoem"
},{
    "nome":"Cansei ja",
    "editora":"Quero oportunidade, mas nao estudo"
},{
    "nome":"casino clandestino",
    "editora":"venda de imoveis e jogo do bicho"
}]
#
@app.route("/buscarlivros")
def get():
    return jsonify(livros=livros)

@app.route("/inserirlivroeditora=<editora>nome=<nome>")
def post(editora, nome):
    for livro in livros:
        for key,value in livro.items():
            if key == nome and value == editora:
                return {"message":"Este livro ja esta cadastrado"}, 409

    obj = {nome: editora}
    livros.append(obj)
    print(livros)
    return "<h1>Funcionou!</h1>", 200

"""@app.route("/eusou<nome>")
def hello(nome):
    return f'<h1>Hellooo, {nome}</h1>'"""

@app.route("/favicon.ico")
def enviaFavIco():
    return send_file('./assets/icons8-gato.gif', mimetype='image/gif')


if __name__ == "__main__":
    app.run()
