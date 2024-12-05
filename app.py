from flask import Flask, request, jsonify

app = Flask(__name__)

# LinkedIn Webhook Verification Endpoint
@app.route('/webhook', methods=['GET', 'POST'])
def linkedin_webhook():
    if request.method == 'GET':
        # Respond to LinkedIn's challenge for verification
        challenge = request.args.get('challenge')
        return jsonify({'challenge': challenge})
    elif request.method == 'POST':
        # Handle LinkedIn events
        event_data = request.json
        print(f"Received event: {event_data}")
        return jsonify({'status': 'success'})

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
