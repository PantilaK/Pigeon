from editUI_ui import *
from PySide6.QtWidgets import QDialog
from PySide6 import QtCore

class ComponentEditUI(QDialog):
    def __init__(self, controller, parent=None) -> None:
        super().__init__(parent,Qt.WindowType.Dialog)
        self.controller = controller
        self.UI = Ui_Form()
        self.UI.setupUi(self)

        self.UI.typeComboBox.currentTextChanged.connect(self.typeComboBoxChanged)
        self.UI.okButton.clicked.connect(self.okButtonClicked)

    def typeComboBoxChanged(self):
        self.controller.typeChange()

    def okButtonClicked(self):
        self.controller.ok()

    