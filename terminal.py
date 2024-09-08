import os
import google.generativeai as genai
from rich.console import Console
from rich.markdown import Markdown
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
console = Console()
# Loop principal do chat
while True:
    pergunta = input("Você: ")
    if pergunta == 'fim':
        print(f"Prof. IA: Encerrando o chat, até a próxima!")
        break

    try:
        response = chat.send_message(pergunta)
        mark_response = Markdown(response.text)
        console.print(mark_response)
        # print(f"Prof. IA: {response.text}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")