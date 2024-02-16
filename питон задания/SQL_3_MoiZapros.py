#Запрос находит менеджеров, зарплата которых выше 15000, работающих с произведениями модерна
import sqlite3
from datetime import date

conn = sqlite3.connect('art.sqlite')
cursor = conn.cursor()

cursor.execute("""
SELECT DISTINCT employees.Lastname, employees.Firstname, employees.Salary, employees.Position, departments.Name
FROM employees
INNER JOIN departments ON employees.DepId = departments.DepId
WHERE departments.Name = ? and employees.Salary > ? and employees.Position = ?
ORDER BY employees.Salary
""", ('Модернисты', '15000', 'Менеджер'))

print(cursor.fetchall())

conn.close()