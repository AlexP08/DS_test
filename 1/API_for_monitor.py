from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/alert', methods=['POST'])
def receive_alert():
    data = request.get_json()
    message = data.get('message')
    if message:
        print(f'Received alert: {message}')
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'error': 'Invalid request data'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)