from flask import (
    Blueprint, request,
    jsonify, render_template
    )
from .core.conf import (
    GOFTINO_BASE_URL, GOFTINO_API_KEY,
    OPEN_AI_BASE_URL, OPEN_AI_API_KEY
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
    response = requests.get(f'{GOFTINO_BASE_URL}/operators', headers=headers)
    if response.status_code == 200:
        data = response.json()
        for operator in data['data']['operators']:
            exsist_operator = Operator.query.filter_by(operator_id=operator['operator_id']).first()
            if not exsist_operator:
                new_operator = Operator(
                    operator_id=operator['operator_id'],
                    name=operator['name'],
                    avatar=operator['avatar'],
                    email=operator['email'],
                    is_online=operator['is_online']
                )
                db.session.add(new_operator)
            else:
                exsist_operator.is_online = operator['is_online']
        
        message = "Succcessfuly Updated/added operators"
    else:
        message = "Failed to fetch operators"

    db.session.commit()
    return jsonify({
        'status': response.status_code,
        'message': message
    })

# Define the webhook route
@main.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    return jsonify({'status': 'success', 'received': data})