import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFrame, QGraphicsScene, QGraphicsView, QGraphicsWidget, QGraphicsRectItem, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import Qt, QMimeData, QRandomGenerator, QPointF
from PySide6.QtGui import QAction, QDrag, QPixmap, QIcon, QKeySequence, QColor, QTransform


class WidgetContainer(QPushButton):
    def __init__(self, text):
        super().__init__(text=text)

    # def mouseMoveEvent(self, event):
    #     # position = event.pos()
    #     # self.i.setPos(position)
    #     # event.accept()
    #     print("move button", event.pos().x(), event.pos().y())


    #     # orig_cursor_position = event.lastScenePos()
    #     # updated_cursor_position = event.scenePos()

    #     # orig_position = self.scenePos()

    #     # updated_cursor_x = updated_cursor_position.x() - orig_cursor_position.x() + orig_position.x()
    #     # updated_cursor_y = updated_cursor_position.y() - orig_cursor_position.y() + orig_position.y()
    #     self.i.setPos(event.pos().x(), event.pos().y())


class Button(QPushButton):
    def __init__(self, text):
        super().__init__(text=text)
        self.setStyleSheet('width: 200px; height: 50px; font-size: 30px')

    # def mouseMoveEvent(self, event):
    #     # print("move button", self.x(), self.y())
    #     if event.buttons() == Qt.LeftButton:
    #         drag = QDrag(self)
    #         mime = QMimeData()
    #         drag.setMimeData(mime)

    #         # pixmap = QPixmap(self.size())
    #         # self.render(pixmap)
    #         # drag.setPixmap(pixmap)

    #         drag.exec(Qt.MoveAction)

class MainGraphicsView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene=scene)
        # self.setDragMode(QGraphicsView.RubberBandDrag)
        self.setMouseTracking(True)
        self.mousePreseed = False

    # def mousePressEvent(self, event):
    #     print(event.pos())
    #     item = self.scene().itemAt(event.pos().x(), event.pos().y(), QTransform())
    #     print("MainGraphicsView", item)
    #     item.setPos(0,0)
    #     event.accept()

    def mousePressEvent(self, event):
        print("mousePressEvent", event.pos())

    def mouseReleaseEvent(self, event):
        print("mouseReleaseEvent", event.pos())

    def mouseReleaseEvent(self, event):
        print("mouseReleaseEvent", event.pos())

    def moveEvent(self, event):
        print("moveEvent", event.pos())

    def enterEvent(self, event):
        print("enterEvent", event.pos())

    def dragEnterEvent(self, event):
        print("dragEnterEvent", event.pos())

    def dragMoveEvent(self, event):
        print("dragMoveEvent", event.pos())

    def dragLeaveEvent(self, event):
        print("dragLeaveEvent", event.pos())
        # if event.buttons() == Qt.LeftButton:
        #     print(event.pos())
        #     item = self.scene().itemAt(event.pos().x(), event.pos().y(), QTransform())
        #     print("MainGraphicsView", item)
        #     item.setPos(event.pos())
        #     event.accept()

    def dropEvent(self, event):
        print("dropEvent", event.pos())


class MainGraphicsScene(QGraphicsScene):
    def __init__(self):
        super().__init__()

    # def mousePressEvent(self, event):
    #     print(event.pos())
    #     item = self.itemAt(event.pos().x(), event.pos().y(), QTransform())
    #     print("MainGraphicsScene", item)
    #     event.accept()


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

        self.scene = MainGraphicsScene()
        self.view = MainGraphicsView(self.scene)
        self.setCentralWidget(self.view)
        # self.layout().addWidget(self.view)
        self.view.setBackgroundBrush(Qt.yellow)

        items = []
        items.append(QGraphicsRectItem(10, 10, 20, 20))
        items.append(QGraphicsRectItem(20, 20, 20, 20))
        items.append(QPushButton(text="Widget 1"))
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

    def dragEnterEvent(self, event):
        print("drag QMainWindow")
        event.accept()

    def dropEvent(self, event):
        print("drop QMainWindow")
        position = event.pos()
        widget = event.source()
        widget.move(position)
        event.accept()

    def dragMoveEvent(self, event):
        print("move QMainWindow")
        position = event.pos()
        widget = event.source()
        widget.move(position)
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = AppDemo()
    demo.show()
    sys.exit(app.exec())