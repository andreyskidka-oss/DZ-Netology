from datetime import datetime

def check_date(date_str):
    """
    Проверяет корректность даты в формате YYYY-MM-DD
    Возвращает True если дата корректна, False если некорректна
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Проверка работы функции
stream = ['2018-04-02', '2018-02-29', '2018-19-02']

for date in stream:
    result = check_date(date)
    print(f"{date}: {result}")
