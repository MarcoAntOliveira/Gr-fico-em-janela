import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matplotlib com PySide6")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Criar uma figura do matplotlib e um canvas para o PySide6
        self.figure, self.canvas = self.create_matplotlib_canvas()
        layout.addWidget(self.canvas)

        # Adicionar barra de ferramentas do Matplotlib
        self.addToolBar(NavigationToolbar(self.canvas, self))

        # Botão para exemplo de atualização do gráfico
        button = QPushButton("Atualizar Gráfico", self)
        button.clicked.connect(self.plot_data)
        layout.addWidget(button)

        # Plotar dados no gráfico inicialmente
        self.plot_data()

    def create_matplotlib_canvas(self):
        figure, canvas = plt.subplots()
        canvas = FigureCanvas(figure)
        return figure, canvas

    def plot_data(self):
        # Dados de exemplo
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # Plotar no gráfico
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        ax.set_title('Exemplo de Gráfico')
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())
