import sqlite3

conn = sqlite3.connect('art.sqlite')
cursor = conn.cursor()
cursor.executescript("""
CREATE TABLE IF NOT EXISTS Artworks
(
  ArtworkId INTEGER PRIMARY KEY,
  Title VARCHAR(100) NULL,
  Genre VARCHAR (50) NULL,
  Tools VARCHAR (50) NULL,
  AuthorId BIGINT NULL,
  CreateDate DATE NULL,
  Price BIGINT NULL,
  DepId INT NOT NULL
);
""")
cursor.executescript("""
CREATE TABLE IF NOT EXISTS Authors
(
	AuthorId INTEGER PRIMARY KEY,
	Lastname VARCHAR (25) NOT NULL,
	Firstname VARCHAR (25) NOT NULL,
	Middlename VARCHAR (25) NULL,
	DateOfBirth DATE NULL,
	DateOfDeath DATE NULL,
	Country VARCHAR (25) NULL
);
""")
cursor.executescript("""
CREATE TABLE IF NOT EXISTS Employees
(
	EmpId INTEGER PRIMARY KEY,
	Lastname VARCHAR (25) NOT NULL,
	Firstname VARCHAR (25) NOT NULL,
	Middlename VARCHAR (25) NOT NULL,
	Position VARCHAR (25) NULL,
	Salary MONEY NULL,
	BeginDate DATE NOT NULL,
	DepId INT NULL
);
""")
cursor.executescript("""
CREATE TABLE IF NOT EXISTS Departments
(
	DepId INTEGER PRIMARY KEY,
	Name VARCHAR (25) NOT NULL
);
""")
conn.commit()

conn.close()
