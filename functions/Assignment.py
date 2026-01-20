# Глобальные переменные (разрешены по условию)
books = [
    {'genre': 'поэзия', 'number': '978-5-1000-1234-7', 'title': 'Евгений Онегин', 'author': 'Александр Пушкин'},
    {'genre': 'фэнтези', 'number': '88006', 'title': 'Властелин колец', 'author': 'Джон Р. Р. Толкин'},
    {'genre': 'детектив', 'number': 'D-1122', 'title': 'Безмолвный свидетель', 'author': 'Агата Кристи'}
]

directories = {
    '1': ['978-5-1000-1234-7', '88006'],
    '2': ['D-1122'],
    '3': []
}

# Вспомогательные функции
def find_book_by_number(book_number):
    """Находит книгу по номеру"""
    for book in books:
        if book['number'] == book_number:
            return book
    return None

def find_book_by_title(book_title):
    """Находит книгу по названию"""
    for book in books:
        if book['title'] == book_title:
            return book
    return None

def find_shelf_by_book_number(book_number):
    """Находит полку по номеру книги"""
    for shelf, book_list in directories.items():
        if book_number in book_list:
            return shelf
    return None

def show_all_books():
    """Показывает все книги с информацией о полках"""
    print("\nТекущий список книг:")
    for book in books:
        shelf = find_shelf_by_book_number(book['number'])
        print(f"№: {book['number']}, жанр: {book['genre']}, "
              f"название: {book['title']}, автор: {book['author']}, "
              f"полка хранения: {shelf}")

# Основные функции для команд
def book_info():
    """Команда 'book_info' - информация о книге по номеру"""
    book_number = input("\nВведите номер книги: ")
    book = find_book_by_number(book_number)
    
    if book:
        print(f"\nНазвание книги: {book['title']}")
        print(f"Автор: {book['author']}")
    else:
        print("\nКнига не найдена в базе")

def shelf():
    """Команда 'shelf' - найти полку по названию книги"""
    book_title = input("\nВведите название книги: ")
    book = find_book_by_title(book_title)
    
    if not book:
        print("\nКнига не найдена в базе")
        return
    
    shelf_num = find_shelf_by_book_number(book['number'])
    if shelf_num:
        print(f"\nКнига хранится на полке: {shelf_num}")
    else:
        print("\nПолка для книги не найдена")

def all_books():
    """Команда 'all' - показать все книги"""
    show_all_books()

def add_shelf():
    """Команда 'add_shelf' - добавить новую полку"""
    shelf_number = input("\nВведите номер полки: ")
    
    # Используем setdefault() - если полка существует, ничего не меняем
    # Если не существует - создаем пустой список
    directories.setdefault(shelf_number, [])
    
    if shelf_number in directories and len(directories[shelf_number]) == 0:
        # Если только что создали полку - сообщаем об успехе
        print(f"\nПолка добавлена. Текущий перечень полок: {', '.join(sorted(directories.keys()))}.")
    else:
        # Если полка уже была - сообщаем об этом
        print(f"\nТакая полка уже существует. Текущий перечень полок: {', '.join(sorted(directories.keys()))}.")

def del_shelf():
    """Команда 'del_shelf' - удалить полку"""
    shelf_number = input("\nВведите номер полки: ")
    
    if shelf_number not in directories:
        print(f"\nТакой полки не существует. Текущий перечень полок: {', '.join(sorted(directories.keys()))}.")
    elif directories[shelf_number]:
        print(f"\nНа полке есть книги, удалите их перед удалением полки. Текущий перечень полок: {', '.join(sorted(directories.keys()))}.")
    else:
        del directories[shelf_number]
        print(f"\nПолка удалена. Текущий перечень полок: {', '.join(sorted(directories.keys()))}.")

def add_book():
    """Команда 'add_book' - добавить новую книгу"""
    book_number = input("\nВведите номер книги: ")
    genre = input("Введите жанр книги: ")
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    shelf = input("Введите полку для хранения: ")
    
    # Проверяем существование полки
    if shelf not in directories:
        print(f"\nТакой полки не существует. Добавьте полку командой add_shelf.")
        show_all_books()
        return
    
    # Проверяем, не существует ли уже книга с таким номером
    if find_book_by_number(book_number):
        print("Книга с таким номером уже существует!")
        return
    
    # Добавляем книгу
    books.append({
        'genre': genre,
        'number': book_number,
        'title': title,
        'author': author
    })
    
    # Используем setdefault() для добавления на полку
    # (хотя мы уже проверили, что полка существует)
    directories.setdefault(shelf, []).append(book_number)
    
    print("\nКнига добавлена.")
    show_all_books()

def del_book():
    """Команда 'del_book' - удалить книгу"""
    book_number = input("\nВведите номер книги: ")
    
    # Ищем книгу
    book = find_book_by_number(book_number)
    
    if not book:
        print("\nКнига не найдена в базе.")
        show_all_books()
        return
    
    # Удаляем книгу из списка книг
    books.remove(book)
    
    # Удаляем книгу с полки
    shelf = find_shelf_by_book_number(book_number)
    if shelf:
        directories[shelf].remove(book_number)
    
    print("\nКнига удалена.")
    show_all_books()

def move_book():
    """Команда 'move' - переместить книгу на другую полку"""
    book_number = input("\nВведите номер книги: ")
    new_shelf = input("Введите номер полки: ")
    
    # Проверяем существование книги
    book = find_book_by_number(book_number)
    if not book:
        print("\nКнига не найдена в базе.")
        show_all_books()
        return
    
    # Проверяем существование новой полки
    if new_shelf not in directories:
        print(f"\nТакой полки не существует. Текущий перечень полок: {', '.join(sorted(directories.keys()))}.")
        return
    
    # Находим текущую полку
    current_shelf = find_shelf_by_book_number(book_number)
    
    if current_shelf:
        # Удаляем книгу с текущей полки
        directories[current_shelf].remove(book_number)
    
    # Используем setdefault() для добавления на новую полку
    directories.setdefault(new_shelf, []).append(book_number)
    
    print("\nКнига перемещена.")
    show_all_books()

def main():
    """Основная функция программы"""
    print("Программа для управления библиотекой")
    print("Доступные команды:")
    print("  book_info - информация о книге по номеру")
    print("  shelf - найти полку по названию книги")
    print("  all - показать все книги")
    print("  add_shelf - добавить полку")
    print("  del_shelf - удалить полку")
    print("  add_book - добавить книгу")
    print("  del_book - удалить книгу")
    print("  move - переместить книгу")
    print("  q - выход")
    print("-" * 50)
    
    while True:
        command = input("\nВведите команду: ").strip()
        
        match command:
            case "q":
                print("\nВыход из программы.")
                break
            
            case "book_info":
                book_info()
            
            case "shelf":
                shelf()
            
            case "all":
                all_books()
            
            case "add_shelf":
                add_shelf()
            
            case "del_shelf":
                del_shelf()
            
            case "add_book":
                add_book()
            
            case "del_book":
                del_book()
            
            case "move":
                move_book()
            
            case _:
                print("\nНеизвестная команда. Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main()
