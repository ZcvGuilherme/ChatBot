import markdown2
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import main

class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Config_Tela()
        self.Criar_Widgets()
    
    def Config_Tela(self):
        self.setWindowTitle('ChatMárcio')
        self.setGeometry(100, 100, 500, 600)
        self.setMinimumSize(500, 600)
        self.setMaximumSize(500, 600)
        
    def Criar_Widgets(self):
        # Definindo o widget central e o layout principal
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        
        # Criando a área de exibição de mensagens
        self.chat_area = QScrollArea(self)
        self.chat_area.setWidgetResizable(True)
        self.chat_area.setStyleSheet("background-color: LightCyan;")
        self.chat_area.setMaximumSize(500, 600)
        self.layout.addWidget(self.chat_area)
        
        # Widget que vai conter as mensagens
        self.chat_widget = QWidget()
        self.chat_widget.setMaximumWidth(450)
        self.chat_layout = QVBoxLayout(self.chat_widget)
        self.chat_widget.setStyleSheet('''
            QWidget {
                    border: 1px solid gray
                    border-radius: 10px; 
                                       }
''')
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
            # Estilizando e exibindo a mensagem do usuário
            user_message_label = QLabel(f"Você: {user_message}")
            user_message_label.setStyleSheet('''
                QLabel {
                    border: 1px solid gray;
                    border-radius: 10px;
                    background-color: #DCF8C6;
                    color: black;
                    padding: 10px;
                    margin: 5px;
                }
            ''')
            self.chat_layout.addWidget(user_message_label, alignment=Qt.AlignRight)
            
            # Aqui você chamaria a função do chatbot para obter a resposta
            resposta = main.perg_resp(user_message)  # Substituir por `main.perg_resp(user_message)`
            
            # Estilizando e exibindo a mensagem do chatbot e convertendo a resposta para HTML usando Markdown

            html_output = markdown2.markdown(f"Chatbot: {resposta}")
            bot_message_label = QLabel(html_output)
            bot_message_label.setStyleSheet('''
                QLabel {
                    border: 1px solid black;
                    border-radius: 10px;
                    background-color: #F4A460;
                    color: black;
                    padding: 10px;
                    margin: 5px;
                }
            ''')
            self.chat_layout.addWidget(bot_message_label, alignment=Qt.AlignLeft)
            
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
