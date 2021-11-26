from PyQt5.QtWidgets import QWidget, QHBoxLayout, QAbstractButton
from PyQt5.QtGui import QIcon, QPainter, QPixmap, QPaintEvent
from PyQt5.QtCore import QSize


# Класс для отжимаемых кнопок
class NoteButton(QAbstractButton):
    def __init__(self, path, path2):
        super().__init__()
        self.note_on_pixmap = QPixmap(path)
        self.note_off_pixmap = QPixmap(path2)

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.isDown():
            pix = self.note_on_pixmap
        else:
            pix = self.note_off_pixmap
        painter.drawPixmap(event.rect(), pix)

    def sizeHint(self):
        return self.note_on_pixmap.size()
