import os
from flask import Flask, request, jsonify
import requests
from base64 import b64encode
from dotenv import load_dotenv  # Importa a biblioteca para carregar variáveis de ambiente do arquivo .env

# Carregar variáveis de ambiente
load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

app = Flask(__name__)

# Configurações
Vonage_Api_Key = os.getenv("VONAGE_API_KEY")  # Usa os nomes das variáveis de ambiente definidas no arquivo .env
Vonage_Api_Secret = os.getenv("VONAGE_API_SECRET")
Vonage_Zap_Number = os.getenv("VONAGE_WHATSAPP_NUMBER")
Gemini_Api_Key = os.getenv("GEMINI_API_KEY")

# Debug das variáveis de ambiente
print(f"VONAGE_API_KEY: {Vonage_Api_Key}")
print(f"VONAGE_API_SECRET: {Vonage_Api_Secret}")
print(f"VONAGE_WHATSAPP_NUMBER: {Vonage_Zap_Number}")
print(f"GEMINI_API_KEY: {Gemini_Api_Key}")
print()

# Gerar o token de autenticação para Vonage
auth_token = b64encode(f"{Vonage_Api_Key}:{Vonage_Api_Secret}".encode()).decode()  # Codifica as credenciais em Base64

def send_message(to_number, message_text):
    url = "https://messages-sandbox.nexmo.com/v1/messages"
    headers = {
        "Authorization": f"Basic {auth_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    data = {
        "from": Vonage_Zap_Number,
        "to": f"+{to_number}",
        "channel": "Whatsapp",
        "message_type": "text",
        "text": message_text
    }
    response = requests.post(url, json=data, headers=headers)
    print(f"Resposta do Vonage: {response.status_code} - {response.text}")

def query_gemini(message_text):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={Gemini_Api_Key}"
    headers = {
        "Content-Type": "application/json"
    }
    data = {"query": message_text}
    response = requests.post(url, json=data, headers=headers)
    response_json = response.json()
    print(f"Resposta do Gemini: {response_json}")  # Adicione esta linha para ver a resposta completa
    return response_json.get('response', 'Desculpe, não entendi sua mensagem.')

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
            message_text = data.get('text', 'Texto não encontrado')  # Acessa o texto da mensagem
            
            print(f"Mensagem recebida de {user_number}: {message_text}\n")
            
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
    app.run(port=5000)  # Inicia o servidor Flask na porta 5000
