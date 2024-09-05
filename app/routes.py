from flask import (
    Blueprint, request,
    jsonify, render_template
    )
from .core.conf import (
    GOFTINO_BASE_URL, GOFTINO_API_KEY,
    OPEN_AI_BASE_URL, OPEN_AI_API_KEY
    )
from .ml.base_model import DynamicModel as DM
from .chat import Message
from .models import (db, Setting, Operator,
    Visit, User, Chat, Message
    )
import requests

# Define BluePrint Decorator
main = Blueprint('main', __name__)

# Define index route
@main.route('/', methods=['get'])
def index():
    return render_template('index.html')

@main.route('/chat_storage', methods=['POST'])
def chat_storage():
    try:
        data = request.json
        return jsonify({
            'status': 200,
            'message': data
        })
    except Exception as e:
        return jsonify({
            'status': 500,
            'message': f'An error occurred: {str(e)}'
        }), 500

@main.route('/app_state', methods=['POST'])
def change_app_state():
    try:
        setting = Setting.query.first()

        if not setting:
            init = Setting(state=True)
            db.session.add(init)
            db.session.commit()

            return jsonify({
                'status': 200,
                'message': 'State initialized to On'
            })

        else:
            setting.state = not setting.state
            db.session.commit()

            return jsonify({
                'status': 200,
                'message': f'State changed to {"on" if setting.state else "Off"}'
            })

    except Exception as e:
        return jsonify({
            'status': 500,
            'message': f'An error occurred: {str(e)}'
        }), 500

@main.route('/get_operators_list', methods=['POST'])   
def get_operators_list():
    headers = {
        'Content-Type': 'application/json',
        'goftino-key': GOFTINO_API_KEY
    }

    try:
        response = requests.get(f'{GOFTINO_BASE_URL}/operators', headers=headers)
        response.raise_for_status()
        data = response.json()['data']['operators']
        existing_operators = {op.operator_id: op for op in Operator.query.all()}
        new_operators = []
        for operator in data:
            operator_id = operator['operator_id']
            if operator_id in existing_operators:
                existing_operator = existing_operators[operator_id]
                existing_operator.is_online = operator['is_online']
            else:
                new_operator = Operator(
                    operator_id=operator_id,
                    name=operator['name'],
                    avatar=operator['avatar'],
                    email=operator['email'],
                    is_online=operator['is_online']
                )
                new_operators.append(new_operator)

        if new_operators:
            db.session.bulk_save_objects(new_operators)

        db.session.commit()
        message = "Successfully updated/added operators"

    except requests.exceptions.RequestException as e:
        # Handle errors in the external API request
        db.session.rollback()
        message = f"Failed to fetch operators: {str(e)}"
        return jsonify({'status': 500, 'message': message}), 500

    return jsonify({
        'status': 200,
        'message': message
    })

# Define the webhook route
@main.route('/webhook', methods=['POST'])
def webhook():
    d = request.json
    try:
        status = 200
        event = d['event']
        data = d['data']
    except:
        status = 403
        data = 'bad request'
    return jsonify({'status': status, 'received': data})