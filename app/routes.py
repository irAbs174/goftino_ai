from flask import (
    Blueprint, request,
    jsonify, render_template
    )
from .core.conf import (
    GOFTINO_BASE_URL, GOFTINO_API_KEY,
    OPEN_AI_BASE_URL, OPEN_AI_API_KEY
    )
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
    

# Define the webhook route
@main.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    requests.post(f'http://0.0.0.0:8000/{data["user_id"]}')
    return jsonify({'status': 200, 'received': data})