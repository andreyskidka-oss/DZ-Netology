def calculate_ingredients():
    cook_book = {
        'салат': [
            {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
            {'ingridient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
            {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
            {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
            {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
            {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
            {'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
        ],
        'пицца': [
            {'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
            {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
            {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
            {'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
            {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
            {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},
        ],
        'лимонад': [
            {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
            {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
            {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
            {'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},
        ]
    }
    
    portions = int(input("Введите количество порций: "))
    
    # Создаем словарь для хранения суммарных количеств
    total_ingredients = {}
    
    # Собираем все ингредиенты
    for dish_name, ingredients in cook_book.items():
        for ingredient in ingredients:
            name = ingredient['ingridient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * portions
            
            # Создаем ключ
            key = f"{name}|{measure}"
            
            if key in total_ingredients:
                total_ingredients[key] += quantity
            else:
                total_ingredients[key] = quantity
    
    # Преобразуем в список и сортируем
    result_list = []
    for key, quantity in total_ingredients.items():
        name, measure = key.split("|")
        result_list.append([name, quantity, measure])
    
    # Простая сортировка пузырьком
    n = len(result_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if result_list[j][0] > result_list[j+1][0]:
                result_list[j], result_list[j+1] = result_list[j+1], result_list[j]
    
    # Выводим результат
    print("\nРезультат:")
    for item in result_list:
        print(f"{item[0].capitalize()}: {item[1]} {item[2]}")

# ВЫЗЫВАЕМ ФУНКЦИЮ!
calculate_ingredients()
