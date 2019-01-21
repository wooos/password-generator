import sys
import random
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QLineEdit, QLabel, QPushButton, QTextEdit, QSpinBox


class PasswordGenerator(QWidget):
    def __init__(self):
        super(PasswordGenerator, self).__init__()
        self.width = 430
        self.height = 330
        self.left = (self.get_desktop_width() - self.width) / 2
        self.top = (self.get_desktop_height() - self.height) / 2
        self.icon = QIcon('resource/favicon.ico')
        self.init_ui()

    @staticmethod
    def get_desktop_width():
        return QApplication.desktop().availableGeometry().width()

    @staticmethod
    def get_desktop_height():
        return QApplication.desktop().availableGeometry().height()

    def init_ui(self):
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.CustomizeWindowHint)
        self.setWindowTitle('Password Generator')
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.setStyleSheet(open('resource/style.qss').read())
        self.setWindowIcon(self.icon)

        self.character_label = QLabel('所用字符', self)
        self.character_label.setGeometry(30, 30, 60, 30)


        self.super_checkbox = QCheckBox('A-Z', self)
        self.super_checkbox.setGeometry(125, 30, 45, 30)
        self.super_checkbox.setChecked(True)

        self.lower_checkbox = QCheckBox('a-z', self)
        self.lower_checkbox.setGeometry(175, 30, 45, 30)
        self.lower_checkbox.setChecked(True)

        self.number_checkbox = QCheckBox('0-9', self)
        self.number_checkbox.setGeometry(230, 30, 45, 30)
        self.number_checkbox.setChecked(True)

        self.special_checkbox = QCheckBox(self)
        self.special_checkbox.setGeometry(285, 30, 15, 30)
        self.special_checkbox.setChecked(False)

        self.special_edit = QLineEdit('!@#', self)
        self.special_edit.setPlaceholderText('特殊字符')
        self.special_edit.setGeometry(305, 35, 100, 20)

        self.password_length_label = QLabel('密码长度', self)
        self.password_length_label.setGeometry(30, 80, 60, 30)

        self.password_length_edit = QSpinBox(self)
        self.password_length_edit.setMinimum(1)
        self.password_length_edit.setMaximum(128)
        self.password_length_edit.setValue(8)
        self.password_length_edit.setGeometry(125, 83, 280, 24)

        self.generator_button = QPushButton('Generator Password', self)
        self.generator_button.setGeometry(30, 130, 375, 38)
        self.generator_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.generator_button.clicked.connect(self.generator_password)

        self.generator_password_text = QTextEdit(self)
        self.generator_password_text.setPlaceholderText('Generator Result')
        self.generator_password_text.setGeometry(30, 195, 375, 90)
        self.generator_password_text.setReadOnly(True)

        self.show()

    def get_special_text(self):
        return self.special_edit.text()

    def get_password_length(self):
        return self.password_length_edit.text()

    def generator_password(self):
        ll, result = '', ''
        if self.super_checkbox.checkState():
            ll += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if self.lower_checkbox.checkState():
            ll += 'abcdefghijklmnopqrstuvwxyz'
        if self.number_checkbox.checkState():
            ll += '0123456789'
        if self.special_checkbox.checkState():
            ll += self.get_special_text()
        for i in range(int(self.get_password_length())):
            result += random.choice(ll)
        self.generator_password_text.setText(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PasswordGenerator()
    sys.exit(app.exec_())