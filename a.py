from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys

class StatChatbotGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Chatbot de Estatística')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        # Create a QPushButton widget
        self.button = QPushButton('Clique em mim')
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_button_click(self):
        print('Botão clicado!')

    def keyPressEvent(self, event):
        print(f'Botao Apertado: {event.key()}')
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.button.click()  # Simula o clique no botão

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = StatChatbotGUI()
    ex.show()
    sys.exit(app.exec_())
