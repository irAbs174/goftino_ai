from flask import Flask, request, jsonify

app = Flask(__name__)

# Define the webhook route
@app.route('/webhook', methods=['POST'])
def webhook():
    # Get the JSON data from the request
    data = request.json
    
    # Print the received data
    print("Received data:")
    print(data)
    
    # Respond with a JSON object (optional)
    return jsonify({'status': 'success', 'received': data})

if __name__ == '__main__':
    # Run the Flask app on a specific port
    app.run(host='0.0.0.0', port=5000)
