import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QSizePolicy
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout

class Weather(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Погода')
        self.setGeometry(150, 150, 1000, 650)

        layout = QHBoxLayout() # основной лайаут
        layout_text = QVBoxLayout()

        self.text_du = QtWidgets.QLabel(self)
        self.text_du.setFont(QFont('Arial', 15))
        self.text_du.setText('26 градусов')

        self.text_city = QtWidgets.QLabel(self)
        self.text_city.setFont(QFont('Arial', 12))
        self.text_city.setText('Москва, \nРоссия')

        self.text_weather_base = QtWidgets.QLabel(self)
        self.text_weather_base.setFont(QFont('Arial', 15))
        self.text_weather_base.setText('Облачно')

        layout_text.addWidget(self.text_weather_base, alignment = Qt.AlignBottom)
        layout_text.addWidget(self.text_city, alignment=Qt.AlignBottom)
        layout_text.addWidget(self.text_du, alignment=Qt.AlignTop)

        layout_button = QVBoxLayout()

        self.btn1 = QPushButton('Погода на ближайшие дни')
        self.btn1.resize(100, 10)

        self.btn2 = QPushButton('Подробная погода')
        self.btn2.resize(100, 10)

        self.btn3 = QPushButton('Настройки')
        self.btn3.resize(100, 10)

        layout_button.addWidget(self.btn1)
        layout_button.addWidget(self.btn2)
        layout_button.addWidget(self.btn3)


        layout_weather = QVBoxLayout()
        layout_weather_text_1 = QHBoxLayout()
        layout_weather_text_2 = QHBoxLayout()
        layout_weather_text_3 = QHBoxLayout()
        layout_weather_text_4 = QHBoxLayout()
        layout_weather_text_5 = QHBoxLayout()

        self.text_weather_text = QtWidgets.QLabel(self)
        self.text_weather_text.setFont(QFont('Arial', 12))
        self.text_weather_text.setText('Понедельник')

        self.text_weather_text_du = QtWidgets.QLabel(self)
        self.text_weather_text_du.setFont(QFont('Arial', 12))
        self.text_weather_text_du.setText('21 градусов / ощущается как 20 градусов')

        self.text_weather_text_1 = QtWidgets.QLabel(self)
        self.text_weather_text_1.setFont(QFont('Arial', 12))
        self.text_weather_text_1.setText('Вторник')

        self.text_weather_text_du_1 = QtWidgets.QLabel(self)
        self.text_weather_text_du_1.setFont(QFont('Arial', 12))
        self.text_weather_text_du_1.setText('14 градусов / ощущается как 15 градусов')

        self.text_weather_text_2 = QtWidgets.QLabel(self)
        self.text_weather_text_2.setFont(QFont('Arial', 12))
        self.text_weather_text_2.setText('Среда')

        self.text_weather_text_du_2 = QtWidgets.QLabel(self)
        self.text_weather_text_du_2.setFont(QFont('Arial', 12))
        self.text_weather_text_du_2.setText('34 градусов / ощущается как 35 градусов')

        self.text_weather_text_3 = QtWidgets.QLabel(self)
        self.text_weather_text_3.setFont(QFont('Arial', 12))
        self.text_weather_text_3.setText('Четверг')

        self.text_weather_text_du_3 = QtWidgets.QLabel(self)
        self.text_weather_text_du_3.setFont(QFont('Arial', 12))
        self.text_weather_text_du_3.setText('26 градусов / ощущается как 30 градусов')

        self.text_weather_text_4 = QtWidgets.QLabel(self)
        self.text_weather_text_4.setFont(QFont('Arial', 12))
        self.text_weather_text_4.setText('Пятница')

        self.text_weather_text_du_4 = QtWidgets.QLabel(self)
        self.text_weather_text_du_4.setFont(QFont('Arial', 12))
        self.text_weather_text_du_4.setText('9 градусов / ощущается как 6 градусов')

        layout_weather_text_1.addWidget(self.text_weather_text, alignment = Qt.AlignLeft)
        layout_weather_text_1.addWidget(self.text_weather_text_du, alignment=Qt.AlignRight)
        layout_weather_text_2.addWidget(self.text_weather_text_1, alignment=Qt.AlignLeft)
        layout_weather_text_2.addWidget(self.text_weather_text_du_1, alignment=Qt.AlignRight)
        layout_weather_text_3.addWidget(self.text_weather_text_2, alignment=Qt.AlignLeft)
        layout_weather_text_3.addWidget(self.text_weather_text_du_2, alignment=Qt.AlignRight)
        layout_weather_text_4.addWidget(self.text_weather_text_3, alignment=Qt.AlignLeft)
        layout_weather_text_4.addWidget(self.text_weather_text_du_3, alignment=Qt.AlignRight)
        layout_weather_text_5.addWidget(self.text_weather_text_4, alignment=Qt.AlignLeft)
        layout_weather_text_5.addWidget(self.text_weather_text_du_4, alignment=Qt.AlignRight)

        layout_weather.addLayout(layout_weather_text_1)
        layout_weather.addLayout(layout_weather_text_2)
        layout_weather.addLayout(layout_weather_text_3)
        layout_weather.addLayout(layout_weather_text_4)
        layout_weather.addLayout(layout_weather_text_5)

        layout.addLayout(layout_text)
        layout.addLayout(layout_button, Qt.AlignLeft)
        layout.addLayout(layout_weather)
        self.setLayout(layout)


app = QApplication(sys.argv)
weather = Weather()
weather.show()
sys.exit(app.exec())
