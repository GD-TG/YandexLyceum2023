import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random
import sys
from PyQt5.QtWidgets import QApplication
from ui import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.qp = QPainter()
        self.x = 200
        self.y = 200
        self.paint = 0
        self.pushButton.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        self.paint = 1
        self.repaint()

    def paintEvent(self, event):
        if self.paint == 1:
            self.qp.begin(self)
            k = random.randint(10, 200)
            color = QColor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
            self.qp.setPen(color)
            self.qp.setBrush(color)
            print(self.x, self.y)
            self.qp.drawEllipse(self.x - k // 2, self.y - k // 2, k, k)
            self.qp.end()
            self.paint = 0
            # Имя элемента совпадает с objectName в QTDesigner


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
