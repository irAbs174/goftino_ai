from flask import Flask, request, jsonify

app = Flask(__name__)

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