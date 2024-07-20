from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://apiperu.dev/api/dni"
API_TOKEN = "5b0c0df849bd7e70ffde864d7e710cbaa01b1d2e4dca96f7ac6a962db5aa589f"

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
print("")
print("")
print("\t\t\t██╗    ██╗██╗██╗     ██████╗ ██████╗ ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗")
print("\t\t\t██║    ██║██║██║     ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝")
print("\t\t\t██║ █╗ ██║██║██║     ██║  ██║██████╔╝██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   ")
print("\t\t\t██║███╗██║██║██║     ██║  ██║██╔══██╗██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   ")
print("\t\t\t╚███╔███╔╝██║███████╗██████╔╝██║  ██║██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   ")
print("\t\t\t ╚══╝╚══╝ ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   ")
print("Sigueme: @WildesCave - @ProgrimWild")                                                                                               

if __name__ == '__main__':
    app.run(debug=True)

