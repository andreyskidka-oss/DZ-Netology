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

# Пример использования
print("Валюта с максимальным курсом:", get_currency_with_max_value())
