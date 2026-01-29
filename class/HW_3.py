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


# Пример использования класса Designer
print("\n=== Пример использования класса Designer ===")

# Создаем дизайнера с 2 премиями по умолчанию
designer = Designer("Анна", seniority=0)
print(f"Начальные данные: {designer.get_info()}")

# Проводим несколько аккредитаций
print("\nПроводим аккредитации:")
for i in range(15):
    print(f"Аккредитация {i+1}: ", end="")
    designer.check_if_it_is_time_for_upgrade()

print(f"\nДанные после 15 аккредитаций: {designer.get_info()}")

# Добавляем еще премий
print("\nДобавляем 2 дополнительные премии:")
designer.add_award(2)

# Проводим еще несколько аккредитаций
print("\nПроводим еще 5 аккредитаций:")
for i in range(5):
    print(f"Аккредитация {i+1}: ", end="")
    designer.check_if_it_is_time_for_upgrade()

print(f"\nИтоговые данные: {designer.get_info()}")

# Пример сравнения с разработчиком
print("\n=== Сравнение с разработчиком ===")
dev = Developer("Иван", seniority=0)
des = Designer("Мария", seniority=0)

print("Разработчик:")
for i in range(10):
    dev.check_if_it_is_time_for_upgrade()

print("\nДизайнер:")
for i in range(10):
    des.check_if_it_is_time_for_upgrade()
