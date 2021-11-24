import sys
from source_code.classes.QtNoteClasses import NoteButton
import fluidsynth
from PyQt5.Qt import *
from untitled import Ui_Sample_synth
import sqlite3
import time
import pyaudio

NOTE_BUTTON_IMG = "source_code/icons/note_on.png"
WIDTH = 2
CHANNELS = 2
RATE = 44100
CHANNEL = 0

fs = fluidsynth.Synth()
fs.start()

class Player(QObject):
    finished = pyqtSignal()

    def __init__(self, fs, pa):
        self.fs = fs
        self.pa = pa

    def run(self):
        while True:
            pass


class Example(QWidget, Ui_Sample_synth):
    def __init__(self, pa, fs_synth, img_path, channel):
        super().__init__()
        self.pa = pa
        self.fs = fs_synth
        self.img_path = img_path
        self.channel = channel
        sfid = self.fs.sfload("example.sf2")
        self.fs.program_select(0, sfid, 0, 0)
        self.octaves = {}
        for i in range(9):
            self.octaves[i] = [7 * i, 7 * i + 1, 7 * i + 2, 7 * i + 3, 7 * i + 4, 7 * i + 5, 7 * i + 6]
        print(self.octaves)
        self.cur_octave = 4
        self.initUI()

    def initUI(self):
        super().setupUi(self)

        self.key1 = NoteButton(self.img_path)
        self.key2 = NoteButton(self.img_path)
        self.key3 = NoteButton(self.img_path)
        self.key4 = NoteButton(self.img_path)
        self.key5 = NoteButton(self.img_path)
        self.key6 = NoteButton(self.img_path)
        self.key7 = NoteButton(self.img_path)

        self.keys = [
            self.key1, self.key2, self.key3, self.key4, self.key5, self.key6, self.key7
        ]

        self.key1.pressed.connect(lambda: self.pressed(self.octaves.get(self.cur_octave)[0]))
        self.key2.pressed.connect(lambda: self.pressed(self.octaves.get(self.cur_octave)[1]))
        self.key3.pressed.connect(lambda: self.pressed(self.octaves.get(self.cur_octave)[2]))
        self.key4.pressed.connect(lambda: self.pressed(self.octaves.get(self.cur_octave)[3]))
        self.key5.pressed.connect(lambda: self.pressed(self.octaves.get(self.cur_octave)[4]))
        self.key6.pressed.connect(lambda: self.pressed(self.octaves.get(self.cur_octave)[5]))
        self.key7.pressed.connect(lambda: self.pressed(self.octaves.get(self.cur_octave)[6]))

        self.key1.released.connect(lambda: self.released(self.octaves.get(self.cur_octave)[0]))
        self.key2.released.connect(lambda: self.released(self.octaves.get(self.cur_octave)[1]))
        self.key3.released.connect(lambda: self.released(self.octaves.get(self.cur_octave)[2]))
        self.key4.released.connect(lambda: self.released(self.octaves.get(self.cur_octave)[3]))
        self.key5.released.connect(lambda: self.released(self.octaves.get(self.cur_octave)[4]))
        self.key6.released.connect(lambda: self.released(self.octaves.get(self.cur_octave)[5]))
        self.key7.released.connect(lambda: self.released(self.octaves.get(self.cur_octave)[6]))

        self.reverb_dial.sliderMoved.connect(self.reverb_change)
        self.vibrato_dial.sliderMoved.connect(self.vibrato_change)
        self.pan_dial.sliderMoved.connect(self.pan_change)
        self.expression_dial.sliderMoved.connect(self.expression_change)
        self.sustain_dial.sliderMoved.connect(self.sustain_change)
        self.chorus_dial.sliderMoved.connect(self.chorus_change)
        self.volume_dial.sliderMoved.connect(self.volume_change)

        for key in self.keys:
            self.horizontalLayout.addWidget(key)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D and not event.isAutoRepeat():
            self.key1.setDown(True)
            self.pressed(self.octaves.get(self.cur_octave)[0])

        if event.key() == Qt.Key_F and not event.isAutoRepeat():
            self.key2.setDown(True)
            self.pressed(self.octaves.get(self.cur_octave)[1])

        if event.key() == Qt.Key_G and not event.isAutoRepeat():
            self.key3.setDown(True)
            self.pressed(self.octaves.get(self.cur_octave)[2])

        if event.key() == Qt.Key_H and not event.isAutoRepeat():
            self.key4.setDown(True)
            self.pressed(self.octaves.get(self.cur_octave)[3])

        if event.key() == Qt.Key_J and not event.isAutoRepeat():
            self.key5.setDown(True)
            self.pressed(self.octaves.get(self.cur_octave)[4])

        if event.key() == Qt.Key_K and not event.isAutoRepeat():
            self.key6.setDown(True)
            self.pressed(self.octaves.get(self.cur_octave)[5])

        if event.key() == Qt.Key_L and not event.isAutoRepeat():
            self.key7.setDown(True)
            self.pressed(self.octaves.get(self.cur_octave)[6])

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_D and not event.isAutoRepeat():
            self.key1.setDown(False)
            self.released(self.octaves.get(self.cur_octave)[0])

        if event.key() == Qt.Key_F and not event.isAutoRepeat():
            self.key1.setDown(False)
            self.released(self.octaves.get(self.cur_octave)[1])

        if event.key() == Qt.Key_G and not event.isAutoRepeat():
            self.key1.setDown(False)
            self.released(self.octaves.get(self.cur_octave)[2])

        if event.key() == Qt.Key_H and not event.isAutoRepeat():
            self.key1.setDown(False)
            self.released(self.octaves.get(self.cur_octave)[3])

        if event.key() == Qt.Key_J and not event.isAutoRepeat():
            self.key1.setDown(False)
            self.released(self.octaves.get(self.cur_octave)[4])

        if event.key() == Qt.Key_K and not event.isAutoRepeat():
            self.key1.setDown(False)
            self.released(self.octaves.get(self.cur_octave)[5])

        if event.key() == Qt.Key_L and not event.isAutoRepeat():
            self.key1.setDown(False)
            self.released(self.octaves.get(self.cur_octave)[6])

    def reverb_change(self):
        self.fs.cc(self.channel, 91, self.reverb_dial.value())

    def vibrato_change(self):
        self.fs.cc(self.channel, 1, self.vibrato_dial.value())

    def volume_change(self):
        self.fs.cc(self.channel, 7, self.volume_dial.value())

    def sustain_change(self):
        self.fs.cc(self.channel, 64, self.sustain_dial.value())

    def chorus_change(self):
        self.fs.cc(self.channel, 93, self.chorus_dial.value())

    def pan_change(self):
        self.fs.cc(self.channel, 10, self.pan_dial.value())

    def expression_change(self):
        self.fs.cc(self.channel, 11)

    def released(self, i):
        self.fs.noteoff(0, i)

    def pressed(self, i):
        self.fs.noteon(0, i, 127)

    def load_db(self):

    def startup_load_fonts(self):


    def load_font_from_db(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example(None, fs, NOTE_BUTTON_IMG, CHANNEL)
    ex.show()
    sys.exit(app.exec_())
