import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Configurações
VONAGE_API_KEY = os.getenv("d3c87fec")
VONAGE_API_SECRET = os.getenv("dzbADujfgBvY5xIY")
VONAGE_WHATSAPP_NUMBER = os.getenv("+14157386102")
GEMINI_API_KEY = os.getenv("AIzaSyC9dxA8gHoyVR_OgpyfRaHxdRNjTJUSyDI")

def send_message(to_number, message_text):
    url = "https://messages-sandbox.nexmo.com/v1/messages"
    headers = {
        "Authorization": f"Basic {VONAGE_API_KEY}:{VONAGE_API_SECRET}",
        "Content-Type": "application/json"
        "Accept: application/json"
    }
    data = {
        "from": {"type": "whatsapp", "number": VONAGE_WHATSAPP_NUMBER},
        "to": {"type": "whatsapp", "number": to_number},
        "message": {
            "content": {
                "type": "text",
                "text": message_text
            }
        }
    }
    response = requests.post(url, json=data, headers=headers)
    print(f"Resposta do Vonage: {response.status_code} - {response.text}")

def query_gemini(message_text):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }
    data = {"query": message_text}
    response = requests.post(url, json=data, headers=headers)
    return response.json().get('response', 'Desculpe, não entendi sua mensagem.')

@app.route('/webhook', methods=['POST'])
def inbound_message():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Invalid JSON"}), 400
        
        print(f"Dados recebidos: {data}")
        print(f"Tipo de data: {type(data)}")

        # Verificar se data é um dicionário
        if isinstance(data, dict):
            # Ajustar acesso aos dados
            user_number = data.get('from', 'Número não encontrado')
            message_text = data.get('text', 'Texto não encontrado')
            
            print(f"Mensagem recebida de {user_number}: {message_text}")
            
            # Consulta o Gemini
            reply = query_gemini(message_text)
            
            # Envia a resposta de volta ao usuário
            send_message(user_number, reply)
            
            return jsonify({"status": "received"}), 200
        else:
            return jsonify({"error": "Expected JSON object"}), 400
        
    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"error": "Internal Server Error"}), 500
if __name__ == '__main__':
    app.run(port=5000)
