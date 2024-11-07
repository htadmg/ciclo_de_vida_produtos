from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)
with open('embalagens.json', 'r', encoding='utf-8') as f:
    embalagens = json.load(f)

@app.route('/')
def index():
    materiais_unicos = set()
    for embalagem in embalagens:
        for material in embalagem['materiais']:
            materiais = [m.strip() for m in material.split(',')]
            for m in materiais:
                materiais_unicos.add(m)
    
    # Convertendo o conjunto de volta para uma lista para passar para o template
    materiais_unicos = list(materiais_unicos)
    
    return render_template('embalagem.html', embalagens=embalagens, materiais_unicos=materiais_unicos)


if __name__ == '__main__':
    app.run(debug=True)
