# Importando os módulos necessários do Flask
from flask import Flask, render_template
import json

# Criando a instância do aplicativo Flask
app = Flask(__name__)

# Carrega as embalagens de um arquivo JSON (embalagens.json) que contém as informações das embalagens
with open('embalagens.json', 'r', encoding='utf-8') as f:
    embalagens = json.load(f)


# Função para extrair uma lista única de materiais de todas as embalagens
def extrair_materiais_unicos(embalagens):
    """
    Esta função percorre todas as embalagens, extrai os materiais de cada uma delas,
    remove duplicatas (usando um set) e retorna uma lista de materiais únicos e ordenados.
    """
    materiais_unicos = set()  # Usando set para garantir que os materiais sejam únicos
    for embalagem in embalagens:
        for material in embalagem['materiais']:  # Itera sobre a lista de materiais de cada embalagem
            materiais_unicos.add(material.strip())  # Adiciona o material, removendo espaços extras
    return sorted(materiais_unicos)  # Retorna a lista ordenada de materiais únicos


# Rota principal que exibe a lista de embalagens
@app.route('/')
def index():
    """
    A função `index` é a rota principal da aplicação.
    Aqui, chamamos a função `extrair_materiais_unicos` para obter a lista de materiais únicos e
    passamos as embalagens e os materiais para o template HTML.
    """
    # Chama a função para obter os materiais únicos
    materiais_unicos = extrair_materiais_unicos(embalagens)
    # Exibe o template HTML com as embalagens e os materiais
    return render_template('embalagem.html', embalagens=embalagens, materiais_unicos=materiais_unicos)


# Rota para filtrar as embalagens por material
@app.route('/filtro/<material>')
def filtrar_por_material(material):
    """
    A função `filtrar_por_material` filtra as embalagens para mostrar apenas aquelas que
    contêm o material selecionado. O material é passado via URL.
    """
    # Filtra as embalagens que contêm o material selecionado na lista de materiais
    embalagens_filtradas = [
        embalagem for embalagem in embalagens if material in [m.strip() for m in embalagem['materiais']]
    ]
    # Chama a função para obter a lista de materiais únicos para o filtro
    materiais_unicos = extrair_materiais_unicos(embalagens)
    # Exibe o template com as embalagens filtradas e o material selecionado
    return render_template('embalagem.html', embalagens=embalagens_filtradas, materiais_unicos=materiais_unicos, material_selecionado=material)


# Rota para exibir os detalhes de uma embalagem específica
@app.route('/detalhes/<int:id>')
def detalhes(id):
    """
    A função `detalhes` é responsável por mostrar os detalhes de uma embalagem específica.
    O id da embalagem é passado pela URL e procuramos a embalagem correspondente no arquivo JSON.
    """
    # Procura pela embalagem com o id fornecido na URL
    embalagem = next((item for item in embalagens if item['id'] == id), None)
    if embalagem:
        # Se a embalagem for encontrada, exibe o template de detalhes com os dados da embalagem
        return render_template('detalhes.html', embalagem=embalagem)
    else:
        # Se a embalagem não for encontrada, exibe uma mensagem de erro
        return "Embalagem não encontrada", 404


# Inicia o servidor Flask no modo de desenvolvimento
if __name__ == '__main__':
    app.run(debug=True)
