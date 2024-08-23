import os
import google.generativeai as genai
chave_api = 'AIzaSyC9dxA8gHoyVR_OgpyfRaHxdRNjTJUSyDI'
genai.configure(api_key= chave_api)
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {'role': 'user', 'parts': 'Hello'},
        {'role': 'model', 'parts': 'Great to meet you. What do you like to now?'}
    ]
)
while True:
    response = chat.send_message(input('Você: '))
    if response == 'end':
        break
    else:
        print(response.text)