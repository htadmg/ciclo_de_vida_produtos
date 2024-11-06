from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)
with open('embalagens.json', 'r', encoding='utf-8') as f:
    embalagens = json.load(f)

@app.route('/')
def index():
    return render_template("embalagem.html", embalagens=embalagens)

if __name__ == '__main__':
    app.run(debug=True)
