from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def serve():
    return send_from_directory('attached_assets', 'business-card (2).svg')

@app.route('/<path:path>')
def static_file(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)