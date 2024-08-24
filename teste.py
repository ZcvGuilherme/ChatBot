import google.generativeai as genai

chave_api = 'AIzaSyC9dxA8gHoyVR_OgpyfRaHxdRNjTJUSyDI'
genai.configure(api_key=chave_api)

def criar_modelo():
    return genai.GenerativeModel(
        model_name="gemini-1.5-flash", 
            system_instruction='Você é um professor de estatística que só responde perguntas de estatística.É completamente proibido responder qualquer tipo de pergunta que não tenha a ver com o estatística. Quando for perguntado algo de história, português, ou qualquer outro tópíco que não seja de estatística ou algo matemático relacionado a estatística, você deve educadamente se negar a responder. Repentindo, é completamente proibido responder qualquer tipo de pergunta que não seja de estatística, e essa regra nao deve ser mudada, alterada em hipótese nenhuma.'
        )

def iniciar_chat(modelo):
    return modelo.start_chat(
        history=[
            {'role': 'user', 'parts': 'Olá'},
            {'role': 'model', 'parts': 'Prazer em conhecê-lo. O que você gostaria de saber?'}
        ]
    )

def mandar_resposta(chat, pergunta):
    # Enviar a pergunta ao modelo e obter a resposta
    response = chat.send_message(pergunta)
    
    # Extrair o texto da resposta
    response_text = response.candidates[0].content.parts[0].text
    
    # Verificar se a resposta está alinhada com a instrução original
    if "estatística" not in response_text.lower():
        # Renovar o chat com o mesmo modelo e instrução
        print("Prof. IA: Parece que saí do contexto. Deixe-me voltar ao meu foco principal.")
        model = criar_modelo()
        chat = iniciar_chat(model)
        response = chat.send_message(pergunta)
        response_text = response.candidates[0].content.parts[0].text
    
    return response_text, chat

# Criar o modelo e iniciar o chat
model = criar_modelo()
chat = iniciar_chat(model)

# Loop para interagir com o usuário
while True:
    pergunta = input('Você: ')
    
    if pergunta.lower() in ['fim', 'exit', 'quit']:
        print('Prof. IA: Encerrando o chat, até mais!')
        break
    
    response_text, chat = mandar_resposta(chat, pergunta)
    print(f'Prof. IA: {response_text}')
