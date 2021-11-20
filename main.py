import sys
from source_code.classes.QtNoteClasses import NoteButton
import fluidsynth
from PyQt5.Qt import *
from untitled import Ui_Sample_synth
import time
import pyaudio

WIDTH = 2
CHANNELS = 2
RATE = 44100

fs = fluidsynth.Synth()
fs.start()


class Example(QWidget, Ui_Sample_synth):
    def __init__(self, pa, fs_synth):
        super().__init__()
        self.pa = pa
        self.fs = fs_synth
        sfid = self.fs.sfload("example.sf2")
        self.fs.program_select(0, sfid, 0, 0)
        self.initUI()


    def initUI(self):
        super().setupUi(self)
        self.key1 = NoteButton()
        self.key2 = NoteButton()
        self.key3 = NoteButton()
        self.key4 = NoteButton()
        self.key5 = NoteButton()
        self.key6 = NoteButton()
        self.key7 = NoteButton()
        self.key1.pressed.connect(lambda: self.pressed(0))
        self.key2.pressed.connect(lambda: self.pressed(1))
        self.key3.pressed.connect(lambda: self.pressed(2))
        self.key4.pressed.connect(lambda: self.pressed(3))
        self.key5.pressed.connect(lambda: self.pressed(4))
        self.key6.pressed.connect(lambda: self.pressed(5))
        self.key7.pressed.connect(lambda: self.pressed(6))
        self.key1.released.connect(lambda: self.released(0))
        self.key2.released.connect(lambda: self.released(1))
        self.key3.released.connect(lambda: self.released(2))
        self.key4.released.connect(lambda: self.released(3))
        self.key5.released.connect(lambda: self.released(4))
        self.key6.released.connect(lambda: self.released(5))
        self.key7.released.connect(lambda: self.released(6))

        self.keys = [
            self.key1, self.key2, self.key3, self.key4, self.key5, self.key6, self.key7
        ]

        for key in self.keys:
            self.horizontalLayout.addWidget(key)

    def pressed(self, i):
        print(f'pressed {i}')
        self.fs.noteon(0, i, 127)

    def released(self, i):
        print(f'unpressed {i}')
        self.fs.noteoff(0, i)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example(None, fs)
    ex.show()
    sys.exit(app.exec_())
