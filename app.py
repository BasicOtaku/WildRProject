from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://apiperu.dev/api/dni"
API_TOKEN = "[AQUÍ_PONES_TU_API_KEY]"

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/consultar', methods=['POST'])
def consultar():
    dni = request.json['dni']
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_TOKEN}'
    }
    response = requests.post(API_URL, json={'dni': dni}, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
