import requests

def get_currency_with_max_value():
    """
    Возвращает название валюты с максимальным значением курса
    с использованием сервиса www.cbr-xml-daily.ru/daily_json.js
    """
    try:
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        data = response.json()
        
        if 'Valute' not in data:
            return "Ошибка: данные о валютах не найдены"
        
        max_value = -1
        max_currency_name = ""
        
        for currency_code, currency_info in data['Valute'].items():
            # Учитываем номинал для правильного сравнения
            value_per_unit = currency_info['Value'] / currency_info['Nominal']
            
            if value_per_unit > max_value:
                max_value = value_per_unit
                max_currency_name = currency_info['Name']
        
        return max_currency_name
    
    except requests.exceptions.RequestException as e:
        return f"Ошибка при получении данных: {e}"
    except Exception as e:
        return f"Ошибка: {e}"

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

class Employee:
    """
    Базовый класс сотрудника
    """
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority
        self.grade = 1
    
    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1
    
    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(f"{self.name}: грейд {self.grade}")
    
    def check_if_it_is_time_for_upgrade(self):
        # Базовый метод, переопределяется в дочерних классах
        pass


class Developer(Employee):
    """
    Класс разработчика
    """
    def __init__(self, name, seniority):
        super().__init__(name, seniority)
    
    def check_if_it_is_time_for_upgrade(self):
        # Для каждой аккредитации увеличиваем счетчик на 1
        self.seniority += 1
        
        # Условие повышения сотрудника
        if self.seniority % 5 == 0:
            self.grade_up()
        
        # Публикация результатов
        return self.publish_grade()


class Designer(Employee):
    """
    Класс дизайнера с учетом международных премий
    """
    def __init__(self, name, seniority, awards=2):
        """
        :param name: имя дизайнера
        :param seniority: стаж (в баллах)
        :param awards: количество международных премий (по умолчанию 2)
        """
        super().__init__(name, seniority)
        self.awards = awards  # Количество международных премий
        self.award_points = awards * 2  # Каждая премия дает 2 балла
        self.total_points = self.seniority + self.award_points
    
    def check_if_it_is_time_for_upgrade(self):
        # Увеличиваем стаж на 1 за каждую аккредитацию
        self.seniority += 1
        self.total_points = self.seniority + self.award_points
        
        # Условие повышения: каждые 7 баллов - повышение на 1 грейд
        # При этом учитываем, что повышение может быть неоднократным за один раз
        required_for_upgrade = 7
        
        # Проверяем, сколько раз можно повысить грейд
        upgrades_count = self.total_points // required_for_upgrade
        
        # Вычитаем уже использованные баллы
        used_points = (self.grade - 1) * required_for_upgrade
        
        # Вычисляем текущие доступные баллы для повышения
        available_points = self.total_points - used_points
        
        # Если доступных баллов достаточно для повышения
        if available_points >= required_for_upgrade:
            # Повышаем грейд столько раз, сколько возможно
            possible_upgrades = available_points // required_for_upgrade
            for _ in range(possible_upgrades):
                self.grade_up()
        
        # Публикация результатов
        return self.publish_grade()
    
    def add_award(self, count=1):
        """
        Добавляет международные премии
        :param count: количество премий для добавления
        """
        self.awards += count
        self.award_points = self.awards * 2
        self.total_points = self.seniority + self.award_points
        print(f"{self.name}: добавлено {count} премий. Всего премий: {self.awards}")
    
    def get_info(self):
        """
        Возвращает информацию о дизайнере
        """
        return {
            'name': self.name,
            'seniority': self.seniority,
            'grade': self.grade,
            'awards': self.awards,
            'award_points': self.award_points,
            'total_points': self.total_points
        }

if __name__ == "__main__":
    print("=== Задание 1 ===")
    print(f"Валюта с максимальным курсом: {get_currency_with_max_value()}")
    
    print("\n=== Задание 2 ===")
    rate = Rate(diff=True)
    print(f"Изменение курса USD: {rate.usd()}")
    print(f"Изменение курса EUR: {rate.eur()}")
    
    print("\n=== Задание 3 ===")
    designer = Designer("Ольга", seniority=0, awards=2)
    print("Тестирование системы повышения дизайнера:")
    for i in range(20):
        designer.check_if_it_is_time_for_upgrade()
