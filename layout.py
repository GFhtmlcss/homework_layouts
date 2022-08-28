import sys
import datetime
import requests

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QSizePolicy, QFrame
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout

#  TODO
# 1 - узнать, как зафиксировать размер лэйаута
# 2 - сделать кнопки кликабельными (менять блок справа по нажатию на кнопку) - частично, с багом

# 3 - вставлять данные из api в градусы на сегодня - выполнено
# 4 - подставлять название города

# если открыт какой-то другой блок, его надо скрыть

class Weather(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Погода')
        self.setGeometry(150, 150, 1500, 650)
        # self.setMaximumSize(1750, 650)

        layout = QHBoxLayout() # основной лайаут
        layout_text = QVBoxLayout()

        self.api_token = 'засекречено'

        self.city_name = self.get_city_name()
        self.get_today(self.city_name)

        self.setStyleSheet('background-color: rgb(211, 231, 242);')
        # self.setStyleSheet("background-image: url(небофон.png); background-repeat: no-repeat; background-position: center")
        # self.setStyleSheet('background-image: url("C:/Python - проекты/WeatherProgramm/image/небо для погоды приложения.png"); background-repeat: no-repeat; background-position: center;')

        self.css_weather_today_main = 'color: rgb(59, 105, 138); margin: 150px 0 0 0' # погода главное (пасмурно и тп)
        self.css_city_today_main = 'color: rgb(121, 178, 219); margin: 0 0 150px 0;'  # местоположение главное
        self.css_du_today_main = 'color: rgb(103, 155, 191); margin-left: 50px;'  # градусов главное

        self.text_du = QtWidgets.QLabel(self)
        self.text_du.setFont(QFont('Arial', 20))
        self.text_du.setText('{} градусов'.format(self.temp))
        self.text_du.setStyleSheet(self.css_du_today_main)
        print(self.temp)

        self.text_weather_base = QtWidgets.QLabel(self)
        self.text_weather_base.setFont(QFont('Arial', 40))
        self.text_weather_base.setText(self.main_weather.capitalize())
        self.text_weather_base.setStyleSheet(self.css_weather_today_main)

        self.text_city = QtWidgets.QLabel(self)
        self.text_city.setFont(QFont('Arial', 15))
        self.text_city.setText('Москва, \nРоссия')
        self.text_city.setStyleSheet(self.css_city_today_main)

        layout_text.addWidget(self.text_weather_base, alignment=Qt.AlignCenter) # был AlignBottom
        layout_text.addWidget(self.text_du, alignment=Qt.AlignCenter) # был AlignTop
        layout_text.addWidget(self.text_city, alignment=Qt.AlignCenter)  # был AlignBottom

        layout_weather_all = QHBoxLayout()

        self.weather_frame = QFrame()
        self.weather_frame.setStyleSheet('')

        layout_weather = QVBoxLayout()
        layout_weather_text_1 = QHBoxLayout()
        layout_weather_text_2 = QHBoxLayout()
        layout_weather_text_3 = QHBoxLayout()
        layout_weather_text_4 = QHBoxLayout()
        layout_weather_text_5 = QHBoxLayout()

        weekday_num = datetime.datetime.today().weekday()  # число от 1 до 7, сегодняшний номер дня недели
        weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        weekday = weekdays[weekday_num]  # (weekday_num + 1) % 7 - на завтра например при переходе на след неделю
        weekday_five_day = [weekday, weekdays[(weekday_num + 1) % 7], weekdays[(weekday_num + 2) % 7],
                            weekdays[(weekday_num + 3) % 7], weekdays[(weekday_num + 4) % 7]]
        print(*weekday_five_day)

        self.text_weather_text = QtWidgets.QLabel(self)
        self.text_weather_text.setFont(QFont('Arial', 12))
        self.text_weather_text.setText(weekday_five_day[0])

        self.text_weather_text_du = QtWidgets.QLabel(self)
        self.text_weather_text_du.setFont(QFont('Arial', 12))
        self.text_weather_text_du.setText('{} градусов'.format(self.temp))

        self.text_weather_text_du_feels_like = QtWidgets.QLabel(self)
        self.text_weather_text_du_feels_like.setFont(QFont('Arial', 12))
        self.text_weather_text_du_feels_like.setText('ощущается как {} градусов'.format(self.feels_like))

        self.text_weather_text_1 = QtWidgets.QLabel(self)
        self.text_weather_text_1.setFont(QFont('Arial', 12))
        self.text_weather_text_1.setText(weekday_five_day[1])

        self.text_weather_text_du_1 = QtWidgets.QLabel(self)
        self.text_weather_text_du_1.setFont(QFont('Arial', 12))
        self.text_weather_text_du_1.setText('нетданных градусов')

        self.text_weather_text_du_feels_like_1 = QtWidgets.QLabel(self)
        self.text_weather_text_du_feels_like_1.setFont(QFont('Arial', 12))
        self.text_weather_text_du_feels_like_1.setText('ощущается как нетданных градусов')

        self.text_weather_text_2 = QtWidgets.QLabel(self)
        self.text_weather_text_2.setFont(QFont('Arial', 12))
        self.text_weather_text_2.setText(weekday_five_day[2])

        self.text_weather_text_du_2 = QtWidgets.QLabel(self)
        self.text_weather_text_du_2.setFont(QFont('Arial', 12))
        self.text_weather_text_du_2.setText('нетданных градусов')

        self.text_weather_text_du_feels_like_2 = QtWidgets.QLabel(self)
        self.text_weather_text_du_feels_like_2.setFont(QFont('Arial', 12))
        self.text_weather_text_du_feels_like_2.setText('ощущается как нетданных градусов')

        self.text_weather_text_3 = QtWidgets.QLabel(self)
        self.text_weather_text_3.setFont(QFont('Arial', 12))
        self.text_weather_text_3.setText(weekday_five_day[3])

        self.text_weather_text_du_3 = QtWidgets.QLabel(self)
        self.text_weather_text_du_3.setFont(QFont('Arial', 12))
        self.text_weather_text_du_3.setText('нетданных градусов')

        self.text_weather_text_du_feels_like_3 = QtWidgets.QLabel(self)
        self.text_weather_text_du_feels_like_3.setFont(QFont('Arial', 12))
        self.text_weather_text_du_feels_like_3.setText('ощущается как нетданных градусов')

        self.text_weather_text_4 = QtWidgets.QLabel(self)
        self.text_weather_text_4.setFont(QFont('Arial', 12))
        self.text_weather_text_4.setText(weekday_five_day[4])

        self.text_weather_text_du_4 = QtWidgets.QLabel(self)
        self.text_weather_text_du_4.setFont(QFont('Arial', 12))
        self.text_weather_text_du_4.setText('нетданных градусов')

        self.text_weather_text_du_feels_like_4 = QtWidgets.QLabel(self)
        self.text_weather_text_du_feels_like_4.setFont(QFont('Arial', 12))
        self.text_weather_text_du_feels_like_4.setText('ощущается как нетданных градусов')

        self.css_weather_days = 'color: rgb(103, 134, 153); margin-left: 50px' # стиль дней (воскресенье и тп)
        self.css_weather_days_weather = 'color: rgb(103, 134, 153); background-color: rgb(232, 245, 255); margin: 30px; padding: 5px 15px 5px 15px; border-radius: 15px' # стиль текста дней (столько-то градусов и тп)

        self.text_weather_text.setStyleSheet(self.css_weather_days)
        self.text_weather_text_1.setStyleSheet(self.css_weather_days)
        self.text_weather_text_2.setStyleSheet(self.css_weather_days)
        self.text_weather_text_3.setStyleSheet(self.css_weather_days)
        self.text_weather_text_4.setStyleSheet(self.css_weather_days)

        self.text_weather_text_du.setStyleSheet(self.css_weather_days_weather)
        self.text_weather_text_du_feels_like.setStyleSheet(self.css_weather_days_weather)
        self.text_weather_text_du_1.setStyleSheet(self.css_weather_days_weather)
        self.text_weather_text_du_feels_like_1.setStyleSheet(self.css_weather_days_weather)
        self.text_weather_text_du_2.setStyleSheet(self.css_weather_days_weather)
        self.text_weather_text_du_feels_like_2.setStyleSheet(self.css_weather_days_weather)
        self.text_weather_text_du_3.setStyleSheet(self.css_weather_days_weather)
        self.text_weather_text_du_feels_like_3.setStyleSheet(self.css_weather_days_weather)
        self.text_weather_text_du_4.setStyleSheet(self.css_weather_days_weather)
        self.text_weather_text_du_feels_like_4.setStyleSheet(self.css_weather_days_weather)

        layout_weather_text_1.addWidget(self.text_weather_text, alignment=Qt.AlignLeft)
        layout_weather_text_1.addWidget(self.text_weather_text_du, alignment=Qt.AlignRight)
        layout_weather_text_1.addWidget(self.text_weather_text_du_feels_like, alignment=Qt.AlignRight)

        layout_weather_text_2.addWidget(self.text_weather_text_1, alignment=Qt.AlignLeft)
        layout_weather_text_2.addWidget(self.text_weather_text_du_1, alignment=Qt.AlignRight)
        layout_weather_text_2.addWidget(self.text_weather_text_du_feels_like_1, alignment=Qt.AlignRight)

        layout_weather_text_3.addWidget(self.text_weather_text_2, alignment=Qt.AlignLeft)
        layout_weather_text_3.addWidget(self.text_weather_text_du_2, alignment=Qt.AlignRight)
        layout_weather_text_3.addWidget(self.text_weather_text_du_feels_like_2, alignment=Qt.AlignRight)

        layout_weather_text_4.addWidget(self.text_weather_text_3, alignment=Qt.AlignLeft)
        layout_weather_text_4.addWidget(self.text_weather_text_du_3, alignment=Qt.AlignRight)
        layout_weather_text_4.addWidget(self.text_weather_text_du_feels_like_3, alignment=Qt.AlignRight)

        layout_weather_text_5.addWidget(self.text_weather_text_4, alignment=Qt.AlignLeft)
        layout_weather_text_5.addWidget(self.text_weather_text_du_4, alignment=Qt.AlignRight)
        layout_weather_text_5.addWidget(self.text_weather_text_du_feels_like_4, alignment=Qt.AlignRight)

        self.detailed_frame = QFrame()

        self.css_detailed = 'color: rgb(103, 134, 153); margin-left: 50px;'

        self.text_detailed = QtWidgets.QLabel(self)
        self.text_detailed.setFont(QFont('Arial', 22))
        self.text_detailed.setText('Подробная погода пока в разработке :D')
        self.text_detailed.setStyleSheet(self.css_detailed)

        detailed_layout = QVBoxLayout()
        detailed_layout.addWidget(self.text_detailed)
        self.detailed_frame.setLayout(detailed_layout)
        self.detailed_frame.hide()

        self.settings_frame = QFrame()

        self.text_settings = QtWidgets.QLabel(self)
        self.text_settings.setFont(QFont('Arial', 22))
        self.text_settings.setText('Настройки пока в разработке :D')
        self.text_settings.setStyleSheet(self.css_detailed)

        settings_layout = QVBoxLayout()
        settings_layout.addWidget(self.text_settings)
        self.settings_frame.setLayout(settings_layout)
        self.settings_frame.hide()

        layout_button = QVBoxLayout()

        self.css_btn = 'background-color: rgb(175, 211, 222); border: 2px solid rgb(175, 211, 222); padding: 15px; border-radius:20px; color: rgb(84, 102, 107); max-width: 250px;'

        self.btn1 = QPushButton('Погода на ближайшие дни')
        self.btn1.clicked.connect(self.set_option('weather'))
        self.btn1.resize(100, 10)
        self.btn1.setStyleSheet(self.css_btn)
        self.btn1.setFont(QFont('Arial', 12))
        # print(self.text_du.styleSheet())

        self.btn2 = QPushButton('Подробная погода')
        self.btn2.clicked.connect(self.set_option('detailed'))
        self.btn2.resize(100, 10)
        self.btn2.setStyleSheet(self.css_btn)
        self.btn2.setFont(QFont('Arial', 12))

        self.btn3 = QPushButton('Настройки')
        self.btn3.clicked.connect(self.set_option('settings'))
        self.btn3.resize(100, 10)
        self.btn3.setStyleSheet(self.css_btn)
        self.btn3.setFont(QFont('Arial', 12))

        layout_button.addWidget(self.btn1)
        layout_button.addWidget(self.btn2)
        layout_button.addWidget(self.btn3)

        layout_weather.addLayout(layout_weather_text_1)
        layout_weather.addLayout(layout_weather_text_2)
        layout_weather.addLayout(layout_weather_text_3)
        layout_weather.addLayout(layout_weather_text_4)
        layout_weather.addLayout(layout_weather_text_5)

        self.weather_frame.setLayout(layout_weather)

        layout.addLayout(layout_text)
        layout_weather_all.addLayout(layout_button)
        layout_weather_all.addWidget(self.weather_frame)
        layout.addLayout(layout_weather_all)
        layout.addWidget(self.settings_frame)
        layout.addWidget(self.detailed_frame)

        self.weather_frame.show()

        # print(weather_frame.isHidden(), detailed_frame.isHidden(), settings_frame.isHidden())

        self.setLayout(layout)

    def set_option(self, option):
        def options():
            if option == 'weather':
                self.detailed_frame.hide()
                self.settings_frame.hide()
                self.weather_frame.show()
                print(self.text_weather_base.styleSheet())
            elif option == 'detailed':
                self.weather_frame.hide()
                self.settings_frame.hide()
                self.detailed_frame.show()
                print(self.text_weather_base.styleSheet())
            else:
                self.weather_frame.hide()
                self.detailed_frame.hide()
                self.settings_frame.show()
                print(self.text_weather_base.styleSheet())

        return options


    def get_today(self, city):
        params = {'q': city, 'appid': self.api_token, 'units': 'metric', 'lang': 'ru'}
        response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
        self.today_data = response.json()
        self.temp = self.today_data['main']['temp']
        self.feels_like = self.today_data['main']['feels_like']
        self.main_weather = self.today_data['weather'][0]['description']

    def get_city_name(self):
        # в будущем будет возвращать название того города, который имел в виду пользователь
        return 'Москва'


app = QApplication(sys.argv)
weather = Weather()
weather.show()
sys.exit(app.exec())
