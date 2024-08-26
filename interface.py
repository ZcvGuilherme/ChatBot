import sys
from PyQt5.QtWidgets import *
'''
Explicação do setStyleSheet (Aplicável a Qualquer Widget)

    background-color: Define a cor de fundo do widget. Isso pode ser aplicado a qualquer widget, como botões (QPushButton), campos de texto (QLineEdit), áreas de texto (QTextEdit), etc.

    color: Define a cor do texto exibido dentro do widget. Isso é útil para botões, campos de entrada de texto, labels (QLabel), e qualquer outro widget que contenha texto.

    font-family: Define a família de fontes usada no texto do widget. Você pode aplicar isso em qualquer widget que exiba texto, como botões, campos de texto, e labels.

    font-size: Define o tamanho da fonte do texto dentro do widget. Assim como font-family, pode ser aplicado a qualquer widget que contenha texto.

    border: Define a borda ao redor do widget. Isso pode ser usado em botões, campos de texto, áreas de texto, entre outros, para dar destaque ou melhorar o design do widget.

    border-radius: Define os cantos arredondados da borda do widget. Isso é útil em qualquer widget, especialmente botões e campos de texto, para criar uma aparência mais suave e moderna.

    padding: Define o espaçamento interno dentro do widget, criando espaço entre o conteúdo (como texto) e a borda do widget. Isso é aplicável a botões, campos de texto, e áreas de texto para melhorar a legibilidade e a estética.'''
        


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
        self.layout.addWidget(self.input_field)
        
        # Criando o botão de enviar
        self.send_button = QPushButton("Enviar", self)
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)
    
    def send_message(self):
        # Obtendo o texto do campo de entrada
        user_message = self.input_field.text().strip()
        
        if user_message:
            # Exibindo a mensagem do usuário na área de exibição
            self.chat_display.append(f"Você: {user_message}")
            
            # Aqui você chamaria a função do chatbot para obter a resposta
            resposta = "Esta é uma resposta de exemplo do chatbot."
            
            # Exibindo a resposta do chatbot
            self.chat_display.append(f"Chatbot: {resposta}")
            
            # Limpando o campo de entrada
            self.input_field.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())
