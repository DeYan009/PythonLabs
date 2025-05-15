import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Чтение данных из CSV файла
years = []
months = []
passengers = []

with open('airline-passengers.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # пропускаем заголовок
    for row in csv_reader:
        date = datetime.strptime(row[0], '%Y-%m')
        years.append(date.year)
        months.append(date.month)
        passengers.append(int(row[1]))

# Линейный график пассажиропотока за все время
plt.figure(figsize=(12, 6))
plt.plot(range(len(passengers)), passengers)
plt.title('Пассажиропоток авиакомпании по месяцам')
plt.xlabel('Месяцы')
plt.ylabel('Количество пассажиров')
plt.grid(True)
plt.show()

# Гистограмма распределения пассажиров по месяцам в 1951-1955 гг.
start_idx = years.index(1951)
end_idx = years.index(1955) + 12  # до конца 1955 года

filtered_months = months[start_idx:end_idx]
filtered_passengers = passengers[start_idx:end_idx]

monthly_data = [[] for _ in range(12)]
for m, p in zip(filtered_months, filtered_passengers):
    monthly_data[m-1].append(p)

monthly_avg = [np.mean(m) for m in monthly_data]

plt.figure(figsize=(12, 6))
plt.bar(range(1, 13), monthly_avg)
plt.title('Среднее количество пассажиров по месяцам (1951-1955)')
plt.xlabel('Месяц')
plt.ylabel('Среднее количество пассажиров')
plt.xticks(range(1, 13))
plt.grid(True)
plt.show()