import sqlite3

conn = sqlite3.connect('art.sqlite')
cursor = conn.cursor()

cursor.execute("""
SELECT DISTINCT artworks.Title, artworks.Genre, artworks.Tools, artworks.CreateDate, artworks.Price, authors.Country
FROM artworks
INNER JOIN Authors ON Artworks.AuthorId = Authors.AuthorId
WHERE authors.Country = ?
ORDER BY artworks.CreateDate
""", ("Франция",))  

print(cursor.fetchall())

conn.close()