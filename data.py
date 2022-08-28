import requests
import schedule
import datetime

# 1. обновление информации (например, раз в минуту) - выполнено
# 2. погода на сегодня - наверное
# 3. погода на следующие 5 дней
# 4. получение названия населенного пункта
# 5. Повторение - модуль schedule - выполнено

# узнать день недели для интерфейса
# weekday_number = datetime.datetime.today().weekday()
# weekdays = ['Понедельник', 'Вторник', ...]
# weekday = weekdays[weekday_number]

api_token = '22f2077ee1f82638ad1d2361df8a1cc8'

weekday_num = datetime.datetime.today().weekday() # число от 1 до 7, сегодняшний ноомер дня недели
weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
weekday = weekdays[weekday_num] # (weekday_num + 1) % 7 - на завтра например при переходе на след неделю
weekday_five_day = [weekday, weekdays[(weekday_num + 1) % 7], weekdays[(weekday_num + 2) % 7], weekdays[(weekday_num + 3) % 7], weekdays[(weekday_num + 4) % 7]]
print(*weekday_five_day)


def get_city_name():
    # в будущем будет возвращать название того города, который имел в виду пользователь
    return 'Москва'


def refresh_data():
    city = get_city_name()
    get_next_five_days(city)
    get_today(city)
    print('well')

def get_today(city):
    params = {'q': city, 'appid': api_token, 'units': 'metric', 'lang': 'ru'}
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    data = response.json()
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    main_weather = data['weather'][0]['description']
    print(temp)
    print(feels_like)
    print(main_weather)


def get_next_five_days(city):
    params_five_day = {'q': city, 'appid': api_token}
    response_five_day = requests.get('https://api.openweathermap.org/data/2.5/forecast?', params=params_five_day)
    data_five_day = response_five_day.json()
    print(data_five_day)

refresh_data()
schedule.every(15).minutes.do(refresh_data)

while True:
    schedule.run_pending()
