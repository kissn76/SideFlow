import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import QDrag, QPixmap

class Button(QPushButton):
    def __init__(self, button_text, parent):
        super().__init__(button_text, parent)
        self.setStyleSheet('width: 200px; height: 50px; font-size: 30px')

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)

            # pixmap = QPixmap(self.size())
            # self.render(pixmap)
            # drag.setPixmap(pixmap)

            drag.exec_(Qt.MoveAction)

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)
        self.setAcceptDrops(True)
        # self.setStyleSheet("background-color:black;")

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.widgetlist_layout = QVBoxLayout()
        self.workboard_layout = QVBoxLayout()
        self.main_layout.addLayout(self.workboard_layout)
        self.main_layout.addLayout(self.widgetlist_layout)

        self.widgetlist_layout.addWidget(QPushButton(text="Widget 1"))
        self.widgetlist_layout.addWidget(QPushButton(text="Widget 2"))

        self.button = Button('My Button', self)
        self.button2 = Button('My Button 2', self)
        # self.workboard_layout.addWidget(self.button)
        # self.workboard_layout.addWidget(self.button2)
        # self.button.move(50, 50)
        # self.button2.move(100, 100)

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        position = event.pos()
        widget = event.source()
        widget.move(position)
        event.accept()

    def dragMoveEvent(self, event):
        position = event.pos()
        widget = event.source()
        widget.move(position)
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec_())