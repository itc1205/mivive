import sys
import fluidsynth
from source_code.ui.main_thing import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from sampled_synth import SampledSynth


class MainWin(Ui_MainWindow, QMainWindow):
    def __init__(self, fs_synth, img_path1, img_path2, note_sml_on, note_sml_off):
        super().__init__()
        self.fs = fs_synth
        self.img_path1 = img_path1
        self.img_path2 = img_path2
        self.note_sml_off = note_sml_off
        self.note_sml_on = note_sml_on
        self.setupUI()
        self.fs.start()

    def setupUI(self):
        super().setupUi(self)
        self.open_new_synth_btn.pressed.connect(self.open_new_synth)

    def open_new_synth(self):
        synth = SampledSynth(self.fs, self.img_path1, self.img_path2, self.note_sml_on, self.note_sml_off,
                             self.channel_chng.value())
        synth.show()


if __name__ == '__main__':
    ##############################################
    NOTE_BUTTON_IMG1 = "source_code/icons/on_l.png"
    NOTE_BUTTON_IMG2 = "source_code/icons/off_l.png"
    NOTE_SMALL_ON = "source_code/icons/note_small_on.png"
    NOTE_SMALL_OFF = "source_code/icons/note_small_off.png"
    ##############################################
    fs = fluidsynth.Synth()
    ##############################################
    app = QApplication(sys.argv)
    ex = MainWin(fs, NOTE_BUTTON_IMG1, NOTE_BUTTON_IMG2, NOTE_SMALL_ON, NOTE_SMALL_OFF)
    ex.show()
    sys.exit(app.exec_())
