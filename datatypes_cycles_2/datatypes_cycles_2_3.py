def add_roi_to_results(results):
    for platform, data in results.items():
        revenue = data['revenue']
        cost = data['cost']
        
        # Рассчитываем ROI
        roi = ((revenue / cost) - 1) * 100
        data['ROI'] = round(roi, 2)
    
    return results

# Пример использования:
results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}

updated_results = add_roi_to_results(results)

# Красиво выводим результат
import json
print(json.dumps(updated_results, ensure_ascii=False, indent=2))
