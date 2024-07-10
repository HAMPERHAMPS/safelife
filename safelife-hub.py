from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET', 'POST'])
def proxy():
    try:
        url = request.args.get('url')
    
        if url:
            response = requests.get(url)
            return jsonify({
                'status_code': response.status_code,
                'content': response.text
            })

    except:
        return jsonify({
            'status_code': 1,
            'content': """<p style="color: red;">NYOOOOOoOooOOOo that site doesnt exist.</p>"""
        })
    

if __name__ == '__main__':
    app.run(debug=True)
