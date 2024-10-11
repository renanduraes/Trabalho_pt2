from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Página de contatos
@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

# Rota API para buscar os contatos por estado
@app.route('/api/contatos/<estado>', methods=['GET'])
def get_contatos(estado):
    data = { 'AC': {
                "instituicao": 'Corpo de Bombeiros do Acre',
                "telefone": '193',
                "area": 'Combate a incêndios, salvamentos e emergências.',
                "historia": 'O Corpo de Bombeiros do Acre foi fundado em 1972 e atua em diversas operações de salvamento.'
            },
            'AL': {
                "instituicao": 'Polícia Militar de Alagoas',
                "telefone": '190',
                "area": 'Segurança pública e policiamento.',
                "historia": 'Fundada em 1835, a Polícia Militar de Alagoas é uma das mais antigas instituições de segurança do estado.'
            },
            'AM': {
                "instituicao": 'Defesa Civil do Amazonas',
                "telefone": '199',
                "area": 'Prevenção e gestão de desastres naturais.',
                "historia": 'A Defesa Civil do Amazonas atua em áreas de risco e no controle de emergências ambientais desde 1987.'
            }}
    
    if data:
        response = data[estado]
        return jsonify(response)
    else:
        return jsonify({'error': 'Contatos não encontrados para este estado.'}), 404


@app.route('/add', methods=['POST'])
def add_contact():
    data = request.get_json()
    estado = data.get("estado")
    instituicao = data.get("instituicao")
    telefone = data.get("telefone")
    area = data.get("area")
    historia = data.get("historia")

    # Lógica para salvar o contato (aqui você pode inserir no banco de dados ou processar os dados conforme necessário)

    return jsonify({"message": "Contato enviado com sucesso mas ainda estamos sem banco de dados para salvar seus dados"}),200

if __name__ == '__main__':
    app.run(debug=True)
