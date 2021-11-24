from PyQt5.QtWidgets import QWidget, QHBoxLayout, QAbstractButton
from PyQt5.QtGui import QIcon, QPainter, QPixmap, QPaintEvent
from PyQt5.QtCore import QSize


# Класс для отжимаемых кнопок
class NoteButton(QAbstractButton):
    def __init__(self, path):
        super().__init__()
        self.note_on_pixmap = QPixmap(path)
        # self.note_off_pixmap = QPixmap(path_2)
        print("initialized!")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.note_on_pixmap)

    def sizeHint(self):
        return self.note_on_pixmap.size()
