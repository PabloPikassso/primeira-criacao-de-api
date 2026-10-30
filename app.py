from flask import Flask, jsonify , request

app = Flask(__name__)
app.json.sort_keys = False

livros = [
    {
        'id' : 1,
        'titulo' : 'Berserk',
        'autor': 'Kentaru Miura'
    },

    {
        'id' : 2,
        'titulo' : 'The witcher',
        'autor':  'Velho gaga doido '
    }
]
#listar
@app.route('/livros',methods=['GET'])
def obter_berserk():
    return jsonify(livros)

#listar por id
@app.route('/livros/<int:id>',methods=['GET'])
def obter_berserk_por_id(id):
    for livro in livros:
        if livro['id'] == id:
            return jsonify(livro)
    return jsonify({'erro': 'livro não encontrado'}), 404


#atualizar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro['id'] == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#criar
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


#excluir
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice,livro in enumerate(livros):
        if livro['id'] == id:
            del livros[indice]

    return jsonify(livros)


app.run(port=5000,host='localhost',debug=True)