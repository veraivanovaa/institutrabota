import numpy as np
import pandas as pd
from scipy.stats import gmean

data = pd.read_excel('data_1.xlsx', header=1)
column = 'NOTES'

avg_arifm = data[column].mean()
mediana = data[column].median()
moda = data[column].mode().iloc[0]
avg_geom = gmean(data[column])

print("Среднее арифметическое =", avg_arifm)
print("Среднее геометрическое =", avg_geom)
print("Медиана =", mediana)
print("Мода =", moda)

q1 = data[column].quantile(0.25)
q2 = data[column].quantile(0.5)  
q3 = data[column].quantile(0.75)

print("Первый квартиль =", q1)
print("Второй квартиль =", q2)
print("Третий квартиль =", q3)

minimum = data[column].min()
maximum = data[column].max()

print("Минимум =", minimum)
print("Максимум =", maximum)

razmah = maximum - minimum

print("Размах вариаций =", razmah)

otklonenie = np.abs(data[column] - data[column].median()).mean()

print("Среднее линейное отклонение =", otklonenie)

dispersiya = data[column].var()
otklonenie_kvadrat = data[column].std()
oscillation = (maximum - minimum) / (maximum + minimum)
k_variation = (otklonenie_kvadrat / avg_arifm) * 100 

print("Дисперсия =", dispersiya)
print("Среднее квадратичное отклонение =", otklonenie_kvadrat)
print("Коэффициент осцилляции =", oscillation)
print("Линейный коэффициент вариации =", k_variation,"%")

quad_k_variation = (otklonenie_kvadrat**2 / avg_arifm) * 100
central_moment_3 = ((data[column] - avg_arifm) ** 3).mean()
central_moment_4 = ((data[column] - avg_arifm) ** 4).mean()
asym = ((data[column] - avg_arifm) ** 3).mean() / otklonenie_kvadrat**3
exces = ((data[column] - avg_arifm) ** 4).mean() / otklonenie_kvadrat**4 - 3

print("Квадратичный коэффициент вариации =", quad_k_variation,"%")
print("Центральный момент 3-го порядка =", central_moment_3)
print("Центральный момент 4-го порядка =", central_moment_4)
print("Ассиметрия =", asym)
print("Эксцесс =", exces)
