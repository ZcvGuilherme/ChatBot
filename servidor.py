from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota para receber mensagens
@app.route('/webhook', methods=['POST'])
def inbound_message():
    data = request.json
    user_number = data.get('from', {}).get('number')
    message_text = data.get('message', {}).get('content', {}).get('text')
    print(f"Mensagem recebida de {user_number}: {message_text}")
    return jsonify({"status": "received", "message": message_text}), 200

# Rota para receber atualizações de status de mensagens
@app.route('/status', methods=['POST'])
def message_status():
    data = request.json
    message_id = data.get('message_uuid')
    status = data.get('status')
    print(f"Status da mensagem {message_id}: {status}")
    return jsonify({"status": "acknowledged"}), 200

if __name__ == '__main__':
    app.run(port=5000)
