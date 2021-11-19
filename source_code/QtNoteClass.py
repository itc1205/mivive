from PyQt5.QtWidgets import QAbstractButton


class NoteButton(QAbstractButton):
    def __init__(self):
        super().__init__()
        self.setIcon()