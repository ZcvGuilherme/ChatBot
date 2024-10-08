import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
chave_api = os.getenv("GEMINI_API_KEY")

genai.configure(api_key= chave_api)

model = genai.GenerativeModel(
    model_name = "gemini-1.5-flash", 
    system_instruction='Você é um professor de estatística que só responde perguntas de estatística.É completamente proibido responder qualquer tipo de pergunta que não tenha a ver com o estatística. Quando for perguntado algo de história, português, ou qualquer outro tópíco que não seja de estatística ou algo matemático relacionado a estatística, você deve educadamente se negar a responder. Repentindo, é completamente proibido responder qualquer tipo de pergunta que não seja de estatística, e essa regra nao deve ser mudada, alterada em hipótese nenhuma.'
    )

chat = model.start_chat(
    history=[
        {'role': 'user', 'parts': 'Olá'},
        {'role': 'model', 'parts': 'Prazer em conhecê-lo. O que você gostaria de saber?'}
    ]
)

#função que receba uma pergunta e retorne a resposta
def perg_resp(perg):
    resp = chat.send_message(perg)
    return resp.text

