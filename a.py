import os
import google.generativeai as genai

class Gemini():
    def __init__(self):
        self.config()
    def config(self):
        self.chave_api = 'AIzaSyC9dxA8gHoyVR_OgpyfRaHxdRNjTJUSyDI'
        genai.configure(api_key= self.chave_api)
        self.model = genai.GenerativeModel(
    model_name = "gemini-1.5-flash", 
    system_instruction='Você é um professor de estatística que só responde perguntas de estatística.É completamente proibido responder qualquer tipo de pergunta que não tenha a ver com o estatística. Quando for perguntado algo de história, português, ou qualquer outro tópíco que não seja de estatística ou algo matemático relacionado a estatística, você deve educadamente se negar a responder. Repentindo, é completamente proibido responder qualquer tipo de pergunta que não seja de estatística, e essa regra nao deve ser mudada, alterada em hipótese nenhuma.'
    )

        self.chat = self.model.start_chat(
        history=[

            {'role': 'user', 'parts': 'Olá'},
            {'role': 'model', 'parts': 'Prazer em conhecê-lo. O que você gostaria de saber?'}
         ]
    )

