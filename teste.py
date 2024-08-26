from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QScrollArea
from PyQt5.QtGui import QFontDatabase
import sys

class FontViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Visualizador de Fontes')
        self.setGeometry(100, 100, 600, 800)

        # Criação do layout principal
        layout = QVBoxLayout()

        # Instância de QFontDatabase para obter as fontes disponíveis
        fontes = QFontDatabase()

        # Loop através de todas as fontes disponíveis
        for fonte in fontes.families():
            label = QLabel(f'Fonte: {fonte}')
            label.setFont(fontes.font(fonte, '', 16))  # Define a fonte para a label
            layout.addWidget(label)

        # Cria um widget de rolagem para acomodar todas as fontes
        scroll = QScrollArea()
        container = QWidget()
        container.setLayout(layout)
        scroll.setWidget(container)
        scroll.setWidgetResizable(True)

        self.setCentralWidget(scroll)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = FontViewer()
    viewer.show()
    sys.exit(app.exec_())
