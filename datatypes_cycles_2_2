def analyze_queries(queries):
    word_counts = {}
    total_queries = len(queries)
    
    # Подсчитываем количество запросов с определенным числом слов
    for query in queries:
        word_count = len(query.split())
        if word_count in word_counts:
            word_counts[word_count] += 1
        else:
            word_counts[word_count] = 1
    
    # Выводим результаты
    for count, queries_count in sorted(word_counts.items()):
        percentage = (queries_count / total_queries) * 100
        print(f"Поисковых запросов, содержащих {count} слов(а): {percentage:.2f}%")

# Пример использования:
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

analyze_queries(queries)
