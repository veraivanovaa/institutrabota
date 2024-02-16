import sqlite3
conn = sqlite3.connect('art.sqlite')
cursor = conn.cursor()

# Query the database to retrieve all entries from the Artworks table
cursor.execute("SELECT * FROM Artworks")
rows = cursor.fetchall()

# Print out the fetched data
for row in rows:
    print(row)

# Close the connection
conn.close()