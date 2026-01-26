from datetime import datetime, timedelta

def date_range(start_date, end_date):
    """
    Возвращает список дат за период от start_date до end_date включительно
    Даты должны быть в формате YYYY-MM-DD
    """
    result = []
    
    try:
        # Пробуем преобразовать строки в даты
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        
        # Проверяем, что start_date <= end_date
        if start > end:
            return result
        
        # Генерируем список дат
        current_date = start
        while current_date <= end:
            result.append(current_date.strftime("%Y-%m-%d"))
            current_date += timedelta(days=1)
            
    except ValueError:
        # Если формат даты неверный
        return result
    
    return result

# Примеры использования функции
print("Пример 1 - корректный диапазон:")
print(date_range("2023-01-01", "2023-01-05"))
print()

print("Пример 2 - start_date > end_date:")
print(date_range("2023-01-10", "2023-01-01"))
print()

print("Пример 3 - неверный формат даты:")
print(date_range("2023-13-01", "2023-01-05"))
