from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/proxy', methods=['GET', 'POST'])
def proxy():
    url = request.args.get('url')
    if url:
        response = requests.get(url)
        return jsonify({
            'status_code': response.status_code,
            'content': response.text
        })
    return jsonify({
        'error': '1:nourl'
    })

if __name__ == '__main__':
    app.run(debug=True)
