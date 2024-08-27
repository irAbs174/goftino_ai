from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from app.core.conf import *

# Define flask app
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define index route
@app.route('/', methods=['get'])
def index():
    return "<p style='text-align: center;'>irAbs174 ;)</p>"

# Define the webhook route
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    # Print the received data
    print("Received data:")
    print(data)
    
    # Respond with a JSON object (optional)
    return jsonify({'status': 'success', 'received': data})