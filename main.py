import os
import google.generativeai as genai


chave_api = 'AIzaSyC9dxA8gHoyVR_OgpyfRaHxdRNjTJUSyDI'
genai.configure(api_key= chave_api)
model = genai.GenerativeModel(
    model_name = "gemini-1.5-flash", 
    system_instruction= 'Você é um professor de estatística que só responde perguntas de estatística e não deve responder perguntas fora desse contexto.')
chat = model.start_chat(
    history=[
        {'role': 'user', 'parts': 'Olá'},
        {'role': 'model', 'parts': 'Prazer em conhecê-lo. O que você gostaria de saber?'}
    ]
)

while True:
    pergunta = input('Você: ')
    response = chat.send_message(pergunta)
    if pergunta == 'fim':
        print(f'Prof. IA: {response.text}')
        break
    else:
        print(f'Prof. IA: {response.text}')