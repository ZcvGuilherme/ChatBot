import os
import google.generativeai as genai
chave_api = 'AIzaSyC9dxA8gHoyVR_OgpyfRaHxdRNjTJUSyDI'
genai.configure(api_key= chave_api)
model = genai.GenerativeModel("gemini-1.5-flash")

while True:
  pergunta = input('Sua perguntas (Insira sair para parar) \n -> ')
  if pergunta == 'sair':
    print('Até mais')
    break

  response = model.generate_content(pergunta)
  print(response.text)
