import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFrame, QGraphicsScene, QGraphicsView, QGraphicsWidget, QGraphicsRectItem, QDockWidget, QSizePolicy, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt, QMimeData, QRandomGenerator, QPointF
from PySide6.QtGui import QAction, QDrag, QPixmap, QIcon, QKeySequence, QColor, QTransform

class WidgetContainer(QPushButton):
    def __init__(self, text):
        super().__init__(text=text)


    def mousePressEvent(self, event):
        print("WidgetContainer mousePressEvent", event.position().toPoint())
        if event.button() == Qt.LeftButton:
            drag = QDrag(self)
            mimeData = QMimeData()
            drag.setMimeData(mimeData)
            drag.exec(Qt.MoveAction)


class Button(WidgetContainer):
    def __init__(self, text):
        super().__init__(text=text)
        self.setStyleSheet('width: 200px; height: 50px; font-size: 30px')


class MainGraphicsView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene=scene)


    def dragEnterEvent(self, event):
        print("QGraphicsView dragEnterEvent", event.position().toPoint())
        event.accept()


    def dragMoveEvent(self, event):
        position = event.position().toPoint()
        print("QGraphicsView dragMoveEvent", position)
        widget = event.source()
        widget.move(position)
        event.accept()


    def dropEvent(self, event):
        print("QGraphicsView dropEvent", event.position().toPoint())
        event.accept()


class MainGraphicsScene(QGraphicsScene):
    def __init__(self):
        super().__init__()


class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 400)
        self.setAcceptDrops(True)
        # self.setStyleSheet("background-color:black;")

        menu_bar = QMenuBar()
        menu = QMenu("Menu")
        action = QAction("Action", self)

        openIcon = QIcon.fromTheme("document-open", QIcon(":/images/open.png"))
        openAct = QAction(openIcon, "Open...", self)
        # openAct.setShortcuts(QKeySequence.Open)
        # openAct.setStatusTip("Open an existing file")
        # openAct.triggered.connect(self.open)

        menu.addAction(action)
        menu.addAction(openAct)
        menu_bar.addMenu(menu)
        self.setMenuBar(menu_bar)

        # self.main_layout = QHBoxLayout()
        # self.setLayout(self.main_layout)

        # self.frame = QFrame()
        # self.setCentralWidget(self.frame)

        dockWidget = QDockWidget("Dock Widget", self)
        dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        dockWidget.setWidget(QPushButton(text="Widget 1"))
        self.addDockWidget(Qt.LeftDockWidgetArea, dockWidget)

        self.scene = MainGraphicsScene()
        self.view = MainGraphicsView(self.scene)
        self.setCentralWidget(self.view)
        # self.layout().addWidget(self.view)
        self.scene.setBackgroundBrush(Qt.green)
        # self.view.setBackgroundBrush(Qt.yellow)
        self.view.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

        items = []
        items.append(QGraphicsRectItem(10, 10, 20, 20))
        items.append(QGraphicsRectItem(20, 20, 20, 20))
        items.append(Button(text="Widget 1"))
        items.append(Button('My Button'))
        items.append(WidgetContainer(text="eee"))
        # self.scene.addText("Hello, world!")
        i0 = self.scene.addItem(items[0])
        i1 = self.scene.addItem(items[1])
        i2 = self.scene.addWidget(items[2])
        i3 = self.scene.addWidget(items[3])
        i4 = self.scene.addWidget(items[4])
        i2.setPos(100, 1000)
        i3.setPos(200, 200)
        # i4.setPos(50, 50)
        print(self.view.rect(), self.scene.sceneRect())

        # self.widgetlist_layout = QVBoxLayout()
        # self.workboard_layout = QVBoxLayout()
        # self.main_layout.addLayout(self.workboard_layout)
        # self.main_layout.addLayout(self.widgetlist_layout)

        # self.widgetlist_layout.addWidget(QPushButton(text="Widget 1"))
        # self.widgetlist_layout.addWidget(QPushButton(text="Widget 2"))

        # self.button = Button('My Button', self)
        # self.button2 = Button('My Button 2', self)
        # self.workboard_layout.addWidget(self.button)
        # self.workboard_layout.addWidget(self.button2)
        # self.button.move(50, 50)
        # self.button2.move(100, 100)

    def open(self):
        print("action: open")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec())