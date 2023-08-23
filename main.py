import random
import sys

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton,
                               QVBoxLayout, QWidget)


class MyWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.hello = [
            "Hallo Welt",
            "ä˝ ĺĽ˝ďźä¸ç",
            "Hei maailma",
            "Hola Mundo",
            "ĐŃĐ¸Đ˛ĐľŃ ĐźĐ¸Ń",
        ]

        self.button = QPushButton("Click me!")
        self.message = QLabel("Hello World")
        self.message.alignment = Qt.AlignCenter

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.message)
        self.layout.addWidget(self.button)

        # Connecting the signal
        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        self.message.text = random.choice(self.hello)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())