from flask import Blueprint, request, jsonify
from .models import db, User

main = Blueprint('main', __name__)

# Define index route
@main.route('/', methods=['get'])
def index():
    return "<p style='text-align: center;'>irAbs174 ;)</p>"

# Define the webhook route
@main.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    # Print the received data
    print("Received data:")
    print(data)
    
    # Respond with a JSON object (optional)
    return jsonify({'status': 'success', 'received': data})