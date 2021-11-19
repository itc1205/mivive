import sys
from source_code.QtNoteClass import NoteButton
from PyQt5.Qt import QMainWindow, QApplication, QThread, QObject, pyqtSignal, QFileDialog, QWidget, QGridLayout, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor(255, 255, 255))
        self.setPalette(p)
        self.setGeometry(300, 300, 425, 500)
        self.setWindowTitle('test_example')
        self.btn = NoteButton()
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(30, 30)
        self.btn.resize(self.btn.sizeHint())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
