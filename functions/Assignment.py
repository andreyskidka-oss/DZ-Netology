documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def get_document_by_number(doc_number):
    """Находит документ по номеру"""
    for doc in documents:
        if doc['number'] == doc_number:
            return doc
    return None

def get_shelf_by_document_number(doc_number):
    """Находит полку по номеру документа"""
    for shelf, docs in directories.items():
        if doc_number in docs:
            return shelf
    return None

def get_document_info(doc):
    """Возвращает отформатированную информацию о документе"""
    shelf = get_shelf_by_document_number(doc['number'])
    return f"№: {doc['number']}, тип: {doc['type']}, владелец: {doc['name']}, полка хранения: {shelf}"

# ========== КОМАНДЫ ИЗ ЗАДАНИЯ 1 ==========

def command_p():
    """Команда p - найти владельца по номеру документа"""
    doc_number = input('Введите номер документа: ')
    doc = get_document_by_number(doc_number)
    if doc:
        print(f'Владелец документа: {doc["name"]}')
    else:
        print('Документ не найден в базе')

def command_s():
    """Команда s - найти полку по номеру документа"""
    doc_number = input('Введите номер документа: ')
    shelf = get_shelf_by_document_number(doc_number)
    if shelf:
        print(f'Документ хранится на полке: {shelf}')
    else:
        print('Документ не найден в базе')

def command_l():
    """Команда l - показать все документы"""
    for doc in documents:
        print(get_document_info(doc))

def command_ads():
    """Команда ads - добавить новую полку"""
    shelf_number = input('Введите номер полки: ')
    if shelf_number in directories:
        shelves = ', '.join(sorted(directories.keys()))
        print(f'Такая полка уже существует. Текущий перечень полок: {shelves}.')
    else:
        directories[shelf_number] = []
        shelves = ', '.join(sorted(directories.keys()))
        print(f'Полка добавлена. Текущий перечень полок: {shelves}.')

def command_ds():
    """Команда ds - удалить полку"""
    shelf_number = input('Введите номер полки: ')
    if shelf_number not in directories:
        shelves = ', '.join(sorted(directories.keys()))
        print(f'Такой полки не существует. Текущий перечень полок: {shelves}.')
    elif directories[shelf_number]:
        shelves = ', '.join(sorted(directories.keys()))
        print(f'На полке есть документа, удалите их перед удалением полки. Текущий перечень полок: {shelves}.')
    else:
        del directories[shelf_number]
        shelves = ', '.join(sorted(directories.keys()))
        print(f'Полка удалена. Текущий перечень полок: {shelves}.')

# ========== КОМАНДЫ ИЗ ЗАДАНИЯ 2 ==========

def command_ad():
    """Команда ad - добавить новый документ"""
    doc_number = input('Введите номер документа: ')
    doc_type = input('Введите тип документа: ')
    owner = input('Введите владельца документа: ')
    shelf = input('Введите полку для хранения: ')
    
    if shelf not in directories:
        print('Такой полки не существует. Добавьте полку командой as.')
        print('Текущий список документов:')
        for doc in documents:
            print(get_document_info(doc))
        return
    
    # Проверяем, нет ли уже документа с таким номером
    if get_document_by_number(doc_number):
        print('Документ с таким номером уже существует!')
        return
    
    documents.append({
        'type': doc_type,
        'number': doc_number,
        'name': owner
    })
    directories[shelf].append(doc_number)
    
    print('Документ добавлен. Текущий список документов:')
    for doc in documents:
        print(get_document_info(doc))

def command_d():
    """Команда d - удалить документ"""
    doc_number = input('Введите номер документа: ')
    doc = get_document_by_number(doc_number)
    
    if not doc:
        print('Документ не найден в базе.')
        print('Текущий список документов:')
        for doc in documents:
            print(get_document_info(doc))
        return
    
    # Удаляем документ из списка документов
    documents.remove(doc)
    
    # Удаляем документ с полки
    shelf = get_shelf_by_document_number(doc_number)
    if shelf:
        directories[shelf].remove(doc_number)
    
    print('Документ удален.')
    print('Текущий список документов:')
    for doc in documents:
        print(get_document_info(doc))

def command_m():
    """Команда m - переместить документ на другую полку"""
    doc_number = input('Введите номер документа: ')
    new_shelf = input('Введите номер полки: ')
    
    doc = get_document_by_number(doc_number)
    if not doc:
        print('Документ не найден в базе.')
        print('Текущий список документов:')
        for doc in documents:
            print(get_document_info(doc))
        return
    
    if new_shelf not in directories:
        shelves = ', '.join(sorted(directories.keys()))
        print(f'Такой полки не существует. Текущий перечень полок: {shelves}.')
        return
    
    # Находим старую полку и удаляем оттуда документ
    old_shelf = get_shelf_by_document_number(doc_number)
    if old_shelf:
        directories[old_shelf].remove(doc_number)
    
    # Добавляем документ на новую полку
    directories[new_shelf].append(doc_number)
    
    print('Документ перемещен.')
    print('Текущий список документов:')
    for doc in documents:
        print(get_document_info(doc))

def main():
    """Основная функция программы"""
    commands = {
        'p': command_p,
        's': command_s,
        'l': command_l,
        'ads': command_ads,
        'ds': command_ds,
        'ad': command_ad,
        'd': command_d,
        'm': command_m
    }
    
    print('Добро пожаловать в систему учета документов!')
    print('Доступные команды:')
    print('p - найти владельца документа')
    print('s - найти полку документа')
    print('l - показать все документы')
    print('ads - добавить полку')
    print('ds - удалить полку')
    print('ad - добавить документ')
    print('d - удалить документ')
    print('m - переместить документ')
    print('q - выход')
    print()
    
    while True:
        command = input('Введите команду: ').strip()
        
        if command == 'q':
            print('Выход из программы.')
            break
        
        if command in commands:
            print()
            commands[command]()
        else:
            print('Неизвестная команда. Попробуйте снова.')
        
        print()  # Пустая строка для разделения команд

if __name__ == "__main__":
    main()
