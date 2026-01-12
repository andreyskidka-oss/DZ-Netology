def get_unique_geo_tags(ids):
    unique_tags = set()
    
    for user_tags in ids.values():
        unique_tags.update(user_tags)
    
    return unique_tags

# Пример использования:
ids = {
    'user1': [213, 213, 213, 15, 213],
    'user2': [54, 54, 119, 119, 119],
    'user3': [213, 98, 98, 35]
}

print(f"Результат: {get_unique_geo_tags(ids)}")
