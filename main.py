import sys
from source_code.classes.QtNoteClass import NoteButton
import fluidsynth
from PyQt5.Qt import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.fs = fluidsynth.Synth()
        self.fs.start()
        sfid = self.fs.sfload("example.sf2")
        self.fs.program_select(0, sfid, 0, 0)
        self.setGeometry(300, 300, 425, 500)
        self.setWindowTitle('test_example')
        self.btn = NoteButton()
        self.layout = QHBoxLayout(self)


        self.layout.addWidget(self.btn)
        self.btn.pressed.connect(self.pressed)
        self.btn.released.connect(self.released)

    def pressed(self, i=0):
        print(f'pressed {i}')
        self.fs.noteon(0, 50, 127)

    def released(self, i=0):
        print(f'unpressed {i}')
        self.fs.noteoff(0, 50)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
