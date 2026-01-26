from datetime import datetime

# Форматы для каждой газеты:
# The Moscow Times — Wednesday, October 2, 2002
# The Guardian — Friday, 11.10.13
# Daily News — Thursday, 18 August 1977

moscow_times_date = "Wednesday, October 2, 2002"
the_guardian_date = "Friday, 11.10.13"
daily_news_date = "Thursday, 18 August 1977"

# Преобразование строк в объекты datetime
moscow_times_format = "%A, %B %d, %Y"  # Полное название дня недели, полное название месяца, день, год
the_guardian_format = "%A, %d.%m.%y"   # Полное название дня недели, день.месяц.год (2 цифры года)
daily_news_format = "%A, %d %B %Y"     # Полное название дня недели, день, полное название месяца, год

# Проверка преобразования
print("The Moscow Times:")
print(datetime.strptime(moscow_times_date, moscow_times_format))
print()

print("The Guardian:")
print(datetime.strptime(the_guardian_date, the_guardian_format))
print()

print("Daily News:")
print(datetime.strptime(daily_news_date, daily_news_format))
