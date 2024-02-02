```python
import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.setWindowTitle("Matplotlib com PySide6")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Criar uma figura do matplotlib e um canvas para o PySide6
        self.figure, self.canvas = self.create_matplotlib_canvas()
        layout.addWidget(self.canvas)

        # Plotar dados no gráfico
        self.plot_data()

    def create_matplotlib_canvas(self):
        # Criar uma figura do matplotlib e associar um canvas do PySide6 a ela
        figure, canvas = plt.subplots()
        canvas = FigureCanvas(figure)
        return figure, canvas

    def plot_data(self):
        # Dados de exemplo
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # Plotar no gráfico
        self.figure.clear()  # Limpar qualquer conteúdo anterior do gráfico
        ax = self.figure.add_subplot(111)  # Adicionar um subplot ao gráfico
        ax.plot(x, y)  # Plotar os dados no gráfico
        ax.set_title('Exemplo de Gráfico')  # Adicionar um título ao gráfico
        self.canvas.draw()  # Atualizar o canvas para refletir as alterações

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())
```