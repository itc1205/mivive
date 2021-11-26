import sys
from source_code.classes.QtNoteClasses import NoteButton
import fluidsynth
from PyQt5.Qt import *
from untitled import Ui_Sample_synth
from source_code.functions.db_funcs import *
import numpy
import time
import pyaudio

NOTE_BUTTON_IMG1 = "source_code/icons/on.png"
NOTE_BUTTON_IMG2 = "source_code/icons/off.png"
WIDTH = 2
CHANNELS = 2
RATE = 44100
CHANNEL = 0
BUFFER_LATENCY = 0.001
pa = pyaudio.PyAudio()
strm = pa.open(
    format=pyaudio.paInt16,
    channels=CHANNELS,
    rate=RATE,
    output=True)

fs = fluidsynth.Synth()

class SoundThread(QObject):
    finished = pyqtSignal()

    def __init__(self, fs, stream):
        super().__init__()
        self.fs = fs
        self.stream = stream

    def run(self):
        while True:
            s = []
            s = numpy.append(s, fs.get_samples(int(44100 * 0.1)))
            samps = (fluidsynth.raw_audio_string(s))
            # time.sleep(0.0001)
            self.stream.write(samps)


class Example(QWidget, Ui_Sample_synth):
    def __init__(self, stream, fs_synth, img_path1, img_path2, channel, buffer_latency):
        super().__init__()
        check_db_exists()
        self.stream = stream
        self.fs = fs_synth
        self.sound_thread_start()
        self.img_path = img_path1
        self.img_path2 = img_path2
        self.channel = channel
        self.octaves = {}
        self.buffer_latency = buffer_latency
        for i in range(9):
            self.octaves[i] = [7 * i, 7 * i + 1, 7 * i + 2, 7 * i + 3, 7 * i + 4, 7 * i + 5, 7 * i + 6]
        print(self.octaves)
        self.cur_octave = 6
        self.initUI()
        self.load_db()

    def initUI(self):
        super().setupUi(self)

        self.key1 = NoteButton(self.img_path, self.img_path2)
        self.key2 = NoteButton(self.img_path, self.img_path2)
        self.key3 = NoteButton(self.img_path, self.img_path2)
        self.key4 = NoteButton(self.img_path, self.img_path2)
        self.key5 = NoteButton(self.img_path, self.img_path2)
        self.key6 = NoteButton(self.img_path, self.img_path2)
        self.key7 = NoteButton(self.img_path, self.img_path2)

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

        self.add_to_db.clicked.connect(self.add_font_to_db)
        self.delete_from_db.clicked.connect(self.del_font_from_db)
        self.fonts_list.itemDoubleClicked.connect(self.set_font)

        for key in self.keys:
            self.horizontalLayout.addWidget(key)

    def sound_thread_start(self):
        self.thread = QThread()
        self.worker = SoundThread(self.fs, self.stream)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.thread.start()

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
            self.key2.setDown(False)
            self.released(self.octaves.get(self.cur_octave)[1])

        if event.key() == Qt.Key_G and not event.isAutoRepeat():
            self.key3.setDown(False)
            self.released(self.octaves.get(self.cur_octave)[2])

        if event.key() == Qt.Key_H and not event.isAutoRepeat():
            self.key4.setDown(False)
            self.released(self.octaves.get(self.cur_octave)[3])

        if event.key() == Qt.Key_J and not event.isAutoRepeat():
            self.key5.setDown(False)
            self.released(self.octaves.get(self.cur_octave)[4])

        if event.key() == Qt.Key_K and not event.isAutoRepeat():
            self.key6.setDown(False)
            self.released(self.octaves.get(self.cur_octave)[5])

        if event.key() == Qt.Key_L and not event.isAutoRepeat():
            self.key7.setDown(False)
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
        self.fs.noteoff(self.channel, i)

    def pressed(self, i):
        self.fs.noteon(self.channel, i, 127)

    def load_db(self):
        self.fonts_list.clear()
        self.fonts_dict = get_items_from_fonts_db()
        self.fonts_list.addItems(self.fonts_dict.keys())

    def set_font(self):
        sfid = self.fs.sfload(self.fonts_dict[self.fonts_list.currentItem().text()])
        self.fs.program_select(self.channel, sfid, 0, 0)

    def add_font_to_db(self):
        path = QFileDialog.getOpenFileName(
            self, 'Выбрать музыкальный шрифт', '',
            'Soundfont2 (*.sf2);;Все файлы (*)')[0]
        write_into_database(path)
        self.load_db()

    def del_font_from_db(self):
        delete_from_db(self.fonts_dict[self.fonts_list.currentItem().text()])
        self.load_db()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example(strm, fs, NOTE_BUTTON_IMG1, NOTE_BUTTON_IMG2, CHANNEL, BUFFER_LATENCY)
    ex.show()
    sys.exit(app.exec_())
