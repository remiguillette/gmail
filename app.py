import os
from flask import Flask, send_from_directory, render_template, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from PIL import Image
import io
import base64
import cairosvg

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__, static_folder='client/public')
app.secret_key = os.environ.get("SESSION_SECRET")
CORS(app)

# Configure the SQLAlchemy part of the app
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///database.db")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Initialize SQLAlchemy with the app
db.init_app(app)

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_file(path):
    return send_from_directory(app.static_folder, path)

@app.route('/saver', methods=['POST'])
def saver():
    try:
        image_data = request.files['image'].read()
        image = Image.open(io.BytesIO(image_data))

        # Set DPI for high-resolution output.  Adjust as needed.
        image = image.convert("RGB")
        image.save("temp.png", dpi=(2000,2000))


        svg_data = cairosvg.svg2png(url="temp.png") #This line might need adjustment depending on your cairosvg version and file handling
        os.remove("temp.png")

        encoded_svg = base64.b64encode(svg_data).decode('utf-8')
        return jsonify({'svg': encoded_svg})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


with app.app_context():
    import models  # noqa: F401
    db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)