import markdown2
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import main
'''
Explicação do setStyleSheet (Aplicável a Qualquer Widget)

    background-color: Define a cor de fundo do widget. Isso pode ser aplicado a qualquer widget, como botões (QPushButton), campos de texto (QLineEdit), áreas de texto (QTextEdit), etc.

    color: Define a cor do texto exibido dentro do widget. Isso é útil para botões, campos de entrada de texto, labels (QLabel), e qualquer outro widget que contenha texto.

    font-family: Define a família de fontes usada no texto do widget. Você pode aplicar isso em qualquer widget que exiba texto, como botões, campos de texto, e labels.

    font-size: Define o tamanho da fonte do texto dentro do widget. Assim como font-family, pode ser aplicado a qualquer widget que contenha texto.

    border: Define a borda ao redor do widget. Isso pode ser usado em botões, campos de texto, áreas de texto, entre outros, para dar destaque ou melhorar o design do widget.

    border-radius: Define os cantos arredondados da borda do widget. Isso é útil em qualquer widget, especialmente botões e campos de texto, para criar uma aparência mais suave e moderna.

    padding: Define o espaçamento interno dentro do widget, criando espaço entre o conteúdo (como texto) e a borda do widget. Isso é aplicável a botões, campos de texto, e áreas de texto para melhorar a legibilidade e a estética.'''
        

import main

class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Config_Tela()
        self.Criar_Widgets()
    
    def Config_Tela(self):
        self.setWindowTitle('ChatMárcio')
        self.setGeometry(100, 100, 500, 600)
        
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
        self.chat_display = QTextEdit(self)
        self.chat_display.setReadOnly(True)
       
        self.setStyleSheet("""
            QTextEdit {
                border: 1px solid gray;
                border-radius: 10px;
                padding: 10px;
                background-color: #f5f5f5;
            }
        """)
        self.layout.addWidget(self.chat_display)
        
        # Criando o campo de entrada de texto
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Digite sua pergunta...")
        self.setStyleSheet('''
            QLineEdit {
                font-family: Corbel;
                font-size: 17px
                font-size: 17px;
            }
        ''')
        self.layout.addWidget(self.input_field)
        
        # Criando o botão de enviar
        self.send_button = QPushButton("Enviar", self)
        self.send_button.clicked.connect(self.send_message)
        #coloque aqui
        self.layout.addWidget(self.send_button)
    
    def send_message(self):
        print('botão clicado')
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
            
            # Estilizando e exibindo a mensagem do chatbot
            bot_message_label = QLabel(f"Chatbot: {resposta}")
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
        print(f'Botao Apertado: {event.key()}')
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.send_button.click()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())