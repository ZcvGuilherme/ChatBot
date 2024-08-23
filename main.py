import os
import google.generativeai as genai
chave_api = 'AIzaSyC9dxA8gHoyVR_OgpyfRaHxdRNjTJUSyDI'
genai.configure(api_key= chave_api)
model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat(
    history=[
        {'role': 'user', 'parts': 'Olá'},
        {'role': 'model', 'parts': 'Prazer em conhecê-lo. O que você gostaria de saber?'}
    ]
)
while True:
    response = chat.send_message(input('Você: '))
    if response == 'fim':
        print('Até mais!')
        break
    else:
        print(response.text)