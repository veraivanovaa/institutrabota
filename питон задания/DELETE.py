import sqlite3
from datetime import date
conn = sqlite3.connect('art.sqlite')
cursor = conn.cursor()

# Clear out existing data in the Artworks table
cursor.execute("DELETE FROM Artworks")
cursor.execute("DELETE FROM Authors")
cursor.execute("DELETE FROM Departments")
cursor.execute("DELETE FROM Employees")

# Commit the changes
conn.commit()
conn.close()