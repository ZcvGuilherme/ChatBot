from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
import sys

class ToggleButtonExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Botão Toggle com Efeito de Clique')
        self.setGeometry(100, 100, 300, 200)

        # Criando o botão toggle
        self.toggle_button = QPushButton('Clique para Ligar', self)
        self.toggle_button.setCheckable(True)  # Permite que o botão permaneça pressionado (toggle)

        # Configurando os estilos para os estados normal e checked
        self.toggle_button.setStyleSheet("""
            QPushButton {
                background-color: lightblue;
                border: 2px solid darkblue;
                border-radius: 10px;
                padding: 5px 10px;
                font: bold 14px;
            }
            QPushButton:checked {
                background-color: darkblue;
                color: white;
            }
        """)

        # Conectar o sinal toggled ao método que muda o texto do botão
        self.toggle_button.toggled.connect(self.on_toggle)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.toggle_button)
        self.setLayout(layout)

    def on_toggle(self, checked):
        if checked:
            self.toggle_button.setText('Ligado')
        else:
            self.toggle_button.setText('Desligado')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ToggleButtonExample()
    ex.show()
    sys.exit(app.exec_())
