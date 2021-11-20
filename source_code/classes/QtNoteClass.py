from PyQt5.QtWidgets import QAbstractButton
from PyQt5.QtGui import QIcon, QPainter, QPixmap, QPaintEvent
from PyQt5.QtCore import QSize
SIZE = [30, 120]


# Класс для отжимаемых кнопок
class NoteButton(QAbstractButton):
    def __init__(self):
        super().__init__()
        #self.setIcon(QIcon(":/icons/note.png"))
        self.pixmap = QPixmap("source_code/icons/note.png")
        # self.setDown(True)
        print("initialized!")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    def sizeHint(self):
        return self.pixmap.size()