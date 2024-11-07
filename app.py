from flask import Flask, render_template
import json

app = Flask(__name__)

# Carrega as embalagens de um arquivo JSON
with open('embalagens.json', 'r', encoding='utf-8') as f:
    embalagens = json.load(f)

def extrair_materiais_unicos(embalagens):
    """Extrai uma lista única de materiais das embalagens."""
    materiais_unicos = set()
    for embalagem in embalagens:
        for material in embalagem['materiais']:
            # Divide os materiais e remove espaços extras
            materiais_unicos.add(material.strip())
    return sorted(materiais_unicos)

@app.route('/')
def index():
    materiais_unicos = extrair_materiais_unicos(embalagens)
    return render_template('embalagem.html', embalagens=embalagens, materiais_unicos=materiais_unicos)

@app.route('/filtro/<material>')
def filtrar_por_material(material):
    # Filtra as embalagens que contêm o material selecionado em sua lista de materiais
    embalagens_filtradas = [
        embalagem for embalagem in embalagens if material in [m.strip() for m in embalagem['materiais']]
    ]
    materiais_unicos = extrair_materiais_unicos(embalagens)
    
    return render_template('embalagem.html', embalagens=embalagens_filtradas, materiais_unicos=materiais_unicos, material_selecionado=material)

if __name__ == '__main__':
    app.run(debug=True)
