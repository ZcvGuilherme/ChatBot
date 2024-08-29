import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Config_Tela()
        self.Criar_Widgets()
    
    def Config_Tela(self):
        self.setWindowTitle('ChatMárcio')
        self.setGeometry(100, 100, 500, 600)
        self.setMinimumSize(500, 600)

    def Criar_Widgets(self):
        # Definindo o widget central e o layout principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        # Criando a área de exibição de mensagens
        self.chat_area = QScrollArea(self)
        self.chat_area.setWidgetResizable(True)
        self.chat_area.setStyleSheet("background-color: LightCyan;")
        self.layout.addWidget(self.chat_area)
        
        # Widget que vai conter as mensagens
        self.chat_widget = QWidget()
        self.chat_layout = QVBoxLayout(self.chat_widget)
        self.chat_layout.setAlignment(Qt.AlignTop)  # Alinha as mensagens no topo
        self.chat_area.setWidget(self.chat_widget)
        
        # Criando o campo de entrada de texto
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Digite sua pergunta...")
        self.input_field.setStyleSheet('''
            QLineEdit {
                border: 1px solid gray;
                border-radius: 10px;
                font: bold 17px;
                padding: 10px;
                background-color: #ffffff;
            }            
        ''')
        self.layout.addWidget(self.input_field)
        
        # Criando o botão de enviar
        self.send_button = QPushButton("Enviar", self)
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setStyleSheet('''
            QPushButton {
                border: 2px solid #3CB371;
                background-color: #2E8B57;
                color: white;
                font: 15px;
                border-radius: 10px;
                padding: 10px 20px;
            }
            QPushButton:hover {
                background-color: #45a049;
                border: 2px solid #45a049;
            }
            QPushButton:pressed {
                background-color: #3CB371;
            }
        ''')
        self.layout.addWidget(self.send_button)
    
    def send_message(self):
        # Obtendo o texto do campo de entrada
        user_message = self.input_field.text().strip()
        
        if user_message:
            # Criando a "caixinha" da mensagem do usuário
            user_message_widget = QWidget()
            user_message_layout = QHBoxLayout(user_message_widget)
            user_message_layout.setContentsMargins(10, 5, 10, 5)
            
            # Estilizando a mensagem
            user_message_label = QLabel(f"Você: {user_message}")
            user_message_label.setStyleSheet("""
                QLabel {
                    background-color: #DCF8C6;
                    color: black;
                    padding: 10px;
                    border-radius: 10px;
                }
            """)
            user_message_layout.addWidget(user_message_label)
            self.chat_layout.addWidget(user_message_widget)
            
            # Aqui você chamaria a função do chatbot para obter a resposta
            resposta = "Exemplo de resposta do chatbot."  # Substituir por `main.perg_resp(user_message)`
            
            # Criando a "caixinha" da mensagem do chatbot
            bot_message_widget = QWidget()
            bot_message_layout = QHBoxLayout(bot_message_widget)
            bot_message_layout.setContentsMargins(10, 5, 10, 5)
            
            # Estilizando a mensagem do chatbot
            bot_message_label = QLabel(f"Chatbot: {resposta}")
            bot_message_label.setStyleSheet("""
                QLabel {
                    background-color: #FFFFFF;
                    color: black;
                    padding: 10px;
                    border-radius: 10px;
                }
            """)
            bot_message_layout.addWidget(bot_message_label)
            self.chat_layout.addWidget(bot_message_widget)
            
            # Limpando o campo de entrada
            self.input_field.clear()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.send_button.click()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())
