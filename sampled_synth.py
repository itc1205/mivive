import sys
from source_code.classes.QtNoteClasses import NoteButton
from source_code.ui.sampled_synth_ui import Ui_Sample_synth
from source_code.functions.db_funcs import *
from source_code.functions.cc_values import cc_dict_msb, cc_dict_on_off
import fluidsynth
from PyQt5.Qt import *
import numpy
import pyaudio

##############################################

# Наш класс воспроизведения звука в реальном времени
# (Поток с рабочим воспроизведением звуковых данных из fluidsynth)
# class SoundThread(QObject):
#     def __init__(self, f_synth, stream):
#         super().__init__()
#         self.fs = f_synth
#         self.stream = stream
#
#     def run(self):
#         while True:
#             s = []
#             s = numpy.append(s, self.fs.get_samples(int(44100 * 0.1)))
#             samps = fluidsynth.raw_audio_string(s)
#             self.stream.write(samps)


class SampledSynth(QWidget, Ui_Sample_synth):
    def __init__(self, fs_synth, img_path1, img_path2, sml_note_on, sml_note_off, channel=1, stream=None):
        super().__init__()
        # Создаем ссылки на наши классы, копируем нужные переменные и проверяем наличие базы данных
        self.sml_note_on = sml_note_on
        self.sml_note_off = sml_note_off
        self.stream = stream
        self.fs = fs_synth
        self.img_path = img_path1
        self.img_path2 = img_path2
        self.channel = channel
        check_db_exists()
        # Создаем словарь с нумерацией кнопок по октавам
        self.octaves = {}
        for i in range(8):
            self.octaves[i + 1] = [(12 * i + j) for j in range(12)]
        self.cur_octave = 8
        # Собственно запускаем звуковой поток, наш интерфейс и подгружаем базы данных в интерфейс
        # self.fs.start()
        # self.sound_thread_start()
        self.setupUI()
        self.load_db()

    def setupUI(self):
        super().setupUi(self)
        self.key1 = NoteButton(self.img_path, self.img_path2)
        self.key_sml1 = NoteButton(self.sml_note_on, self.sml_note_off)
        self.key2 = NoteButton(self.img_path, self.img_path2)
        self.key_sml2 = NoteButton(self.sml_note_on, self.sml_note_off)
        self.key3 = NoteButton(self.img_path, self.img_path2)
        self.key4 = NoteButton(self.img_path, self.img_path2)
        self.key_sml3 = NoteButton(self.sml_note_on, self.sml_note_off)
        self.key5 = NoteButton(self.img_path, self.img_path2)
        self.key_sml4 = NoteButton(self.sml_note_on, self.sml_note_off)
        self.key6 = NoteButton(self.img_path, self.img_path2)
        self.key_sml5 = NoteButton(self.sml_note_on, self.sml_note_off)
        self.key7 = NoteButton(self.img_path, self.img_path2)

        self.first_keys = [self.key1, self.key_sml1, self.key2, self.key_sml2, self.key3]
        self.second_keys = [
            self.key4, self.key_sml3, self.key5, self.key_sml4, self.key6, self.key_sml5, self.key7
        ]
        # Соединяем кнопки к обработчику(к сожалению через цикл они теряют свои уникальные свойства)
        self.key1.pressed.connect(lambda: self.pressed(0))
        self.key_sml1.pressed.connect(lambda: self.pressed(1))
        self.key2.pressed.connect(lambda: self.pressed(2))
        self.key_sml2.pressed.connect(lambda: self.pressed(3))
        self.key3.pressed.connect(lambda: self.pressed(4))
        self.key4.pressed.connect(lambda: self.pressed(5))
        self.key_sml3.pressed.connect(lambda: self.pressed(6))
        self.key5.pressed.connect(lambda: self.pressed(7))
        self.key_sml4.pressed.connect(lambda: self.pressed(8))
        self.key6.pressed.connect(lambda: self.pressed(9))
        self.key_sml5.pressed.connect(lambda: self.pressed(10))
        self.key7.pressed.connect(lambda: self.pressed(11))

        self.key1.released.connect(lambda: self.released(0))
        self.key_sml1.released.connect(lambda: self.released(1))
        self.key2.released.connect(lambda: self.released(2))
        self.key_sml2.released.connect(lambda: self.released(3))
        self.key3.released.connect(lambda: self.released(4))
        self.key4.released.connect(lambda: self.released(5))
        self.key_sml3.released.connect(lambda: self.released(6))
        self.key5.released.connect(lambda: self.released(7))
        self.key_sml4.released.connect(lambda: self.released(8))
        self.key6.released.connect(lambda: self.released(9))
        self.key_sml5.released.connect(lambda: self.released(10))
        self.key7.released.connect(lambda: self.released(11))

        self.reverb_dial.sliderMoved.connect(lambda: self.control_change(cc_dict_msb["reverb"], self.reverb_dial))
        self.vibrato_dial.sliderMoved.connect(lambda: self.control_change(cc_dict_msb["modulation"], self.vibrato_dial))
        self.pan_dial.sliderMoved.connect(lambda: self.control_change(cc_dict_msb["pan"], self.pan_dial))
        self.expression_dial.sliderMoved.connect(lambda: self.control_change(cc_dict_msb["exp"], self.expression_dial))
        self.sustain_dial.sliderMoved.connect(lambda: self.control_change(cc_dict_msb["sustain"], self.sustain_dial))
        self.chorus_dial.sliderMoved.connect(lambda: self.control_change(cc_dict_msb["chorus"], self.chorus_dial))
        self.volume_dial.sliderMoved.connect(lambda: self.control_change(cc_dict_msb["volume"], self.volume_dial))

        self.add_to_db.clicked.connect(self.add_font_to_db)
        self.delete_from_db.clicked.connect(self.del_font_from_db)
        self.fonts_list.itemDoubleClicked.connect(self.set_font)

        self.fitrst3noteslayout.addWidget(self.key1)
        self.fitrst3noteslayout.addWidget(self.key_sml1)
        self.fitrst3noteslayout.addWidget(self.key2)
        self.fitrst3noteslayout.addWidget(self.key_sml2)
        self.fitrst3noteslayout.addWidget(self.key3)

        for i in range(5):
            self.fitrst3noteslayout.addWidget(self.first_keys[i])

        for i in range(7):
            self.last4notes_layout.addWidget(self.second_keys[i])


    # def sound_thread_start(self):
    # Рабочий код, убрал изза того что не нужен(пока что)
    # Создаем поток который будет перенаправлять звук из fluidsynth'а в класс PyAudio
    #     self.thread = QThread()
    #     self.worker = SoundThread(self.fs, self.stream)
    #     self.worker.moveToThread(self.thread)
    #     self.thread.started.connect(self.worker.run)
    #     self.thread.start()

    def keyPressEvent(self, event):
        # Подключаем клавиши к кнопкам, немного костыльно но сойдет
        if event.key() == Qt.Key_D and not event.isAutoRepeat():
            self.key1.setDown(True)
            self.pressed(0)

        if event.key() == Qt.Key_E and not event.isAutoRepeat():
            self.key_sml1.setDown(True)
            self.pressed(1)

        if event.key() == Qt.Key_F and not event.isAutoRepeat():
            self.key2.setDown(True)
            self.pressed(2)

        if event.key() == Qt.Key_R and not event.isAutoRepeat():
            self.key_sml2.setDown(True)
            self.pressed(3)

        if event.key() == Qt.Key_G and not event.isAutoRepeat():
            self.key3.setDown(True)
            self.pressed(4)

        if event.key() == Qt.Key_H and not event.isAutoRepeat():
            self.key4.setDown(True)
            self.pressed(5)

        if event.key() == Qt.Key_U and not event.isAutoRepeat():
            self.key_sml3.setDown(True)
            self.pressed(6)

        if event.key() == Qt.Key_J and not event.isAutoRepeat():
            self.key5.setDown(True)
            self.pressed(7)

        if event.key() == Qt.Key_I and not event.isAutoRepeat():
            self.key_sml4.setDown(True)
            self.pressed(8)

        if event.key() == Qt.Key_K and not event.isAutoRepeat():
            self.key6.setDown(True)
            self.pressed(9)

        if event.key() == Qt.Key_O and not event.isAutoRepeat():
            self.key_sml5.setDown(True)
            self.pressed(10)

        if event.key() == Qt.Key_L and not event.isAutoRepeat():
            self.key7.setDown(True)
            self.pressed(11)

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_D and not event.isAutoRepeat():
            self.key1.setDown(False)
            self.released(0)

        if event.key() == Qt.Key_E and not event.isAutoRepeat():
            self.key_sml1.setDown(False)
            self.released(1)

        if event.key() == Qt.Key_F and not event.isAutoRepeat():
            self.key2.setDown(False)
            self.released(2)

        if event.key() == Qt.Key_R and not event.isAutoRepeat():
            self.key_sml2.setDown(False)
            self.released(3)

        if event.key() == Qt.Key_G and not event.isAutoRepeat():
            self.key3.setDown(False)
            self.released(4)

        if event.key() == Qt.Key_H and not event.isAutoRepeat():
            self.key4.setDown(False)
            self.released(5)

        if event.key() == Qt.Key_U and not event.isAutoRepeat():
            self.key_sml3.setDown(False)
            self.released(6)

        if event.key() == Qt.Key_J and not event.isAutoRepeat():
            self.key5.setDown(False)
            self.released(7)

        if event.key() == Qt.Key_I and not event.isAutoRepeat():
            self.key_sml4.setDown(False)
            self.released(8)

        if event.key() == Qt.Key_K and not event.isAutoRepeat():
            self.key6.setDown(False)
            self.released(9)

        if event.key() == Qt.Key_O and not event.isAutoRepeat():
            self.key_sml5.setDown(False)
            self.released(10)

        if event.key() == Qt.Key_L and not event.isAutoRepeat():
            self.key7.setDown(False)
            self.released(11)

    def control_change(self, cc_prog, dial):
        self.fs.cc(self.channel, cc_prog, dial.value())

    def released(self, i):
        self.fs.noteoff(self.channel, self.octaves.get(self.cur_octave)[i])

    def pressed(self, i):
        self.fs.noteon(self.channel, self.octaves.get(self.cur_octave)[i], 127)

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
        self.fs.sfunload()
        self.load_db()

    def closeEvent(self, event):
        super().closeEvent(event)
        print(self.size())


if __name__ == '__main__':
    ##############################################
    NOTE_BUTTON_IMG1 = "source_code/icons/on.png"
    NOTE_BUTTON_IMG2 = "source_code/icons/off.png"
    WIDTH = 2
    CHANNELS = 2
    RATE = 44100
    CHANNEL = 0
    ##############################################
    pa = pyaudio.PyAudio()
    strm = pa.open(
        format=pyaudio.paInt16,
        channels=CHANNELS,
        rate=RATE,
        output=True)

    fs = fluidsynth.Synth()
    ##############################################
    app = QApplication(sys.argv)
    ex = SampledSynth(strm, fs, NOTE_BUTTON_IMG1, NOTE_BUTTON_IMG2, CHANNEL)
    ex.show()
    sys.exit(app.exec_())
