import sqlite3
from datetime import date

conn = sqlite3.connect('art.sqlite')
cursor = conn.cursor()

cursor.execute("""
SELECT DISTINCT artworks.Title, artworks.Genre, artworks.Tools, artworks.Price, employees.BeginDate
FROM artworks 
INNER JOIN employees ON artworks.DepId = employees.DepId
WHERE strftime('%m', employees.BeginDate) = ? AND strftime('%Y', employees.BeginDate) = ?
ORDER BY employees.BeginDate
""", ('07', '2017'))

print(cursor.fetchall())

conn.close()