import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QTextCursor, QFont
from PyQt5.QtCore import Qt
import google.generativeai as genai

# Configuração da API da I.A.
chave_api = 'AIzaSyC9dxA8gHoyVR_OgpyfRaHxdRNjTJUSyDI'
genai.configure(api_key=chave_api)

def criar_modelo():
    return genai.GenerativeModel(
        model_name="gemini-1.5-flash", 
        system_instruction='Você é um professor de estatística que só responde perguntas de estatística e não deve responder perguntas fora desse contexto.'
    )

def iniciar_chat(modelo):
    return modelo.start_chat()

class ChatBotApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.model = criar_modelo()
        self.chat = iniciar_chat(self.model)

        self.setWindowTitle("Chat com IA")
        self.setGeometry(100, 100, 500, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Caixa de texto para histórico com bordas arredondadas e fonte maior
        self.historico = QTextEdit(self)
        self.historico.setReadOnly(True)
        self.historico.setFont(QFont('Arial', 12))
        self.historico.setStyleSheet("""
            QTextEdit {
                border: 1px solid gray;
                border-radius: 10px;
                padding: 10px;
                background-color: #f5f5f5;
            }
        """)
        self.layout.addWidget(self.historico)

        # Caixa de entrada de texto
        self.entrada = QLineEdit(self)
        self.entrada.setFont(QFont('Arial', 14))
        self.entrada.setStyleSheet("""
            QLineEdit {
                border: 1px solid gray;
                border-radius: 10px;
                padding: 10px;
                background-color: #ffffff;
            }
        """)
        self.layout.addWidget(self.entrada)

        # Botão de envio
        self.botao_enviar = QPushButton("Enviar", self)
        self.botao_enviar.setFont(QFont('Arial', 12))
        self.botao_enviar.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.botao_enviar.clicked.connect(self.enviar_pergunta)
        self.layout.addWidget(self.botao_enviar)

    def enviar_pergunta(self):
        pergunta = self.entrada.text()
        if pergunta.lower() in ['fim', 'exit', 'quit']:
            sys.exit()

        resposta = self.chat.send_message(pergunta)
        response_text = resposta.candidates[0].content.parts[0].text

        # Estilo para texto do usuário (direita) e da IA (esquerda)
        self.historico.setAlignment(Qt.AlignRight)
        self.historico.append(f"Você: {pergunta}")
        self.historico.setAlignment(Qt.AlignLeft)
        self.historico.append(f"IA: {response_text}\n")
        
        # Movendo o cursor para o fim para rolar automaticamente
        self.historico.moveCursor(QTextCursor.End)
        self.entrada.clear()

# Inicia a aplicação
app = QApplication(sys.argv)
janela = ChatBotApp()
janela.show()
sys.exit(app.exec_())
