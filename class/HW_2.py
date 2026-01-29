import requests

class Rate:
    def __init__(self, format_='value', diff=False):
        """
        Класс для работы с курсами валют
        :param format_: формат вывода ('value' или 'full')
        :param diff: если True, возвращает разницу с предыдущим значением
        """
        self.format = format_
        self.diff = diff
        
        # Кешируем данные, чтобы не делать запрос каждый раз
        self._cached_data = None
        self._last_update = None
        
    def exchange_rates(self, force_update=False):
        """
        Возвращает курсы валют с кешированием
        """
        # Делаем новый запрос только если данные устарели или принудительно
        if force_update or self._cached_data is None:
            self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
            self._cached_data = self.r.json()['Valute']
        return self._cached_data
    
    def make_format(self, currency):
        """
        Форматирует данные о валюте в соответствии с настройками
        """
        response = self.exchange_rates()
        
        if currency not in response:
            return 'Error'
        
        currency_data = response[currency]
        
        # Если diff=True, возвращаем разницу с предыдущим значением
        if self.diff and self.format == 'value':
            return round(currency_data['Value'] - currency_data['Previous'], 4)
        
        # Обычный режим работы
        if self.format == 'full':
            return currency_data
        elif self.format == 'value':
            return currency_data['Value']
        
        return 'Error'
    
    def eur(self):
        """Возвращает курс евро"""
        return self.make_format('EUR')
    
    def usd(self):
        """Возвращает курс доллара"""
        return self.make_format('USD')
    
    def azn(self):
        """Возвращает курс азербайджанского маната"""
        return self.make_format('AZN')
    
    # Можно добавить методы для других валют по аналогии
    
    def get_all_currencies(self):
        """
        Возвращает все валюты (без учета diff)
        """
        original_diff = self.diff
        self.diff = False  # Временное отключение diff для полного вывода
        
        result = {}
        response = self.exchange_rates()
        for code in response.keys():
            # Используем метод make_format, но временно игнорируем diff
            method_name = code.lower()
            if hasattr(self, method_name):
                result[code] = getattr(self, method_name)()
        
        self.diff = original_diff  # Восстанавливаем исходное значение
        return result


# Пример использования
print("=== Примеры использования класса Rate ===")

# Обычный режим
rate1 = Rate(format_='value', diff=False)
print(f"Курс USD: {rate1.usd()}")
print(f"Курс EUR: {rate1.eur()}")

# Режим с разницей
rate2 = Rate(format_='value', diff=True)
print(f"Изменение USD: {rate2.usd()}")
print(f"Изменение EUR: {rate2.eur()}")

# Полная информация (diff игнорируется)
rate3 = Rate(format_='full')
print(f"Полная информация об USD: {rate3.usd()}")

# Получение всех курсов
print("\nВсе курсы валют:")
all_rates = rate1.get_all_currencies()
for code, value in list(all_rates.items())[:5]:  # Выводим только первые 5
    print(f"{code}: {value}")
