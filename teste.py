import os
import google.generativeai as genai
chave_api = 'AIzaSyC9dxA8gHoyVR_OgpyfRaHxdRNjTJUSyDI'
genai.configure(api_key= chave_api)
model = genai.GenerativeModel(
    model_name = "gemini-1.5-flash", 
    system_instruction= 'Você é um professor de estatística que só responde perguntas de estatística.')

response = model.generate_content(input('vc: '))
print(response.text)