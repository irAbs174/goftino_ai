from flask import (Blueprint,
    request, jsonify, render_template
    )
from .core.conf import (GOFTINO_BASE_URL,
    GOFTINO_API_KEY, OPEN_AI_BASE_URL, OPEN_AI_API_KEY
    )
from .models import (db, Operator)
import requests

# Define BluePrint Decorator
main = Blueprint('main', __name__)

# Define index route
@main.route('/', methods=['get'])
def index():
    return render_template('index.html')

@main.route('/operators/list', methods=['post'])
def get_operators_list():
    headers = {
        'Content-Type': 'application/json',
        'goftino-key': GOFTINO_API_KEY
    }
    requests.get(f'{GOFTINO_API_KEY}/operators').json()
    return jsonify({'status': 200, 'data': [{operator.name if operator.name else None} for operator in Operator.query.all()]})

# Define the webhook route
@main.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    
    # Print the received data
    print("Received data:")
    print(data)
    
    # Respond with a JSON object (optional)
    return jsonify({'status': 'success', 'received': data})