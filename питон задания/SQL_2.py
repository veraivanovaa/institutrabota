import sqlite3
from datetime import date

conn = sqlite3.connect('art.sqlite')
cursor = conn.cursor()
dataArtworks = [    
    {
        "Title": "Ирисы",
        "Genre": "Импрессионизм",
        "Tools": "масло",
        "AuthorId": "1",
        "CreateDate": date(1900, 12, 1),
        "Price": 4000000,
        "DepId": 1,
    },
    {
        "Title": "Флейтист",
        "Genre": "Реализм",
        "Tools": "масло",
        "AuthorId": "6",
        "CreateDate": date(1866, 1, 1),
        "Price": 350000,
        "DepId": 7,
    },
    {
        "Title": "Впечатление",
        "Genre": "Импрессионизм",
        "Tools": "масло",
        "AuthorId": "2",
        "CreateDate": date(1872, 3, 15),
        "Price": 500000,
        "DepId": 1,
    },
    {
        "Title": "Феодосия",
        "Genre": "Реализм",
        "Tools": "масло",
        "AuthorId": "3",
        "CreateDate": date(1880, 1, 3),
        "Price": 400000,
        "DepId": 7,
    },
    {
        "Title": "Золотая осень",
        "Genre": "Импрессионизм",
        "Tools": "масло",
        "AuthorId": "4",
        "CreateDate": date(1895, 3, 8),
        "Price": 333000,
        "DepId": 7,
    },
    {
        "Title": "Рожь",
        "Genre": "Пейзаж",
        "Tools": "масло",
        "AuthorId": "5",
        "CreateDate": date(1878, 3, 1),
        "Price": 220000,
        "DepId": 3,
    },
    {
        "Title": "Черный квадрат",
        "Genre": "Супрематизм",
        "Tools": "масло",
        "AuthorId": "7",
        "CreateDate": date(1915, 5, 5),
        "Price": 900000,
        "DepId": 4,
    },
    {
        "Title": "Итальянское утро",
        "Genre": "Портрет",
        "Tools": "масло",
        "AuthorId": "8",
        "CreateDate": date(1823, 5, 1),
        "Price": 500000,
        "DepId": 3,
    },
    {
        "Title": "Радостная борзая",
        "Genre": "Реализм",
        "Tools": "мел",
        "AuthorId": "9",
        "CreateDate": date(1902, 3, 11),
        "Price": 150000,
        "DepId": 2,
    },
    {
        "Title": "Таитянские пасторали",
        "Genre": "Экспрессионизм",
        "Tools": "масло",
        "AuthorId": "10",
        "CreateDate": date(1892, 1, 6),
        "Price": 111000,
        "DepId": 3,
    },
]

for entryArtworks in dataArtworks:
    entryArtworks['CreateDate'] = entryArtworks['CreateDate'].isoformat()

statementArtworks = cursor.executemany(
    """INSERT INTO Artworks (Title, Genre, Tools, AuthorId, CreateDate, Price, DepId)
       VALUES(:Title, :Genre, :Tools, :AuthorId, :CreateDate, :Price, :DepId);""",
    dataArtworks
)

dataAuthors = (
[    
    {
        "Lastname": "Ван",
        "Firstname": "Гог",
        "Middlename": "NULL",
        "DateOfBirth": date(1853,3,30),
        "DateOfDeath": date(1890,7,29),
        "Country": "Нидерланды",
    },  
    {
        "Lastname": "Моне",
        "Firstname": "Клод",
        "Middlename": "NULL",
        "DateOfBirth": date(1840,11,14),
        "DateOfDeath": date(1926,12,5),
        "Country": "Франция",
    }, 
    {
        "Lastname": "Айвазовский",
        "Firstname": "Иван",
        "Middlename": "Константинович",
        "DateOfBirth": date(1817,7,29),
        "DateOfDeath": date(1900,5,2),
        "Country": "Россия",
    }, 
    {
        "Lastname": "Левитан",
        "Firstname": "Исаак",
        "Middlename": "Ильич",
        "DateOfBirth": date(1860,8,30),
        "DateOfDeath": date(1900,8,4),
        "Country": "Россия",
    }, 
    {
        "Lastname": "Шишкин",
        "Firstname": "Иван",
        "Middlename": "Иванович",
        "DateOfBirth": date(1832,1,25),
        "DateOfDeath": date(1898,3,20),
        "Country": "Россия",
    }, 
    {
        "Lastname": "Мане",
        "Firstname": "Эдуард",
        "Middlename": "NULL",
        "DateOfBirth": date(1832,1,23),
        "DateOfDeath": date(1883,4,30),
        "Country": "Франция",
    }, 
    {
        "Lastname": "Малевич",
        "Firstname": "Казимир",
        "Middlename": "NULL",
        "DateOfBirth": date(1879,2,11),
        "DateOfDeath": date(1935,5,15),
        "Country": "Россия",
    }, 
    {
        "Lastname": "Брюллов",
        "Firstname": "Карл",
        "Middlename": "Павлович",
        "DateOfBirth": date(1799,12,12),
        "DateOfDeath": date(1852,6,23),
        "Country": "Россия",
    }, 
    {
        "Lastname": "Серов",
        "Firstname": "Валентин",
        "Middlename": "Александрович",
        "DateOfBirth": date(1865,1,16),
        "DateOfDeath": date(1911,12,5),
        "Country": "Россия",
    },   
    {
        "Lastname": "Гоген",
        "Firstname": "Поль",
        "Middlename": "NULL",
        "DateOfBirth": date(1848,6,7),
        "DateOfDeath": date(1903,5,8),
        "Country": "Франция",
    },   
]
)

for entryAuthors in dataAuthors:
    entryAuthors["DateOfBirth"] = entryAuthors["DateOfBirth"].isoformat()
    entryAuthors["DateOfDeath"] = entryAuthors["DateOfDeath"].isoformat()

statementAuthors = cursor.executemany(
    """INSERT INTO Authors (Lastname, Firstname, Middlename, DateOfBirth, DateOfDeath, Country)
       VALUES(:Lastname, :Firstname, :Middlename, :DateOfBirth, :DateOfDeath, :Country);""",
    dataAuthors
)

dataDepartments = (
[    
    {
        "Name": "Имперссионисты",
    },  
    {
        "Name": "Передвижники",
    },  
    {
        "Name": "Экспрессионисты",
    },  
    {
        "Name": "Модернисты",
    },  
    {
        "Name": "Художники Поп",
    },  
    {
        "Name": "Неоклассицисты",
    },  
    {
        "Name": "Реалисты",
    },  
    {
        "Name": "Романисты",
    },  
]
)

statementDepartments = cursor.executemany(
    """INSERT INTO Departments (Name)
       VALUES(:Name);""",
    dataDepartments
)

dataEmployees = (
[    
    {
        "Lastname": "Иванов",
        "Firstname": "Иван",
        "Middlename": "Петрович",
        "Position": "Менеджер",
        "Salary": "20000",
        "BeginDate": date(2017,8,1),
        "DepId": "1",
    },  
    {
        "Lastname": "Смирнов",
        "Firstname": "Алексей",
        "Middlename": "Васильевич",
        "Position": "Менеджер",
        "Salary": "40000",
        "BeginDate": date(2017,7,1),
        "DepId": "2",
    },
    {
        "Lastname": "Васильев",
        "Firstname": "Андрей",
        "Middlename": "Васильевич",
        "Position": "Менеджер",
        "Salary": "30000",
        "BeginDate": date(2017,7,17),
        "DepId": "4",
    },
    {
        "Lastname": "Егоров",
        "Firstname": "Егор",
        "Middlename": "Егорович",
        "Position": "Менеджер",
        "Salary": "20000",
        "BeginDate": date(2017,6,13),
        "DepId": "4",
    },
    {
        "Lastname": "Забулов",
        "Firstname": "Илья",
        "Middlename": "Максимович",
        "Position": "Менеджер",
        "Salary": "22000",
        "BeginDate": date(2017,7,17),
        "DepId": "7",
    },  
    {
        "Lastname": "Парабулов",
        "Firstname": "Дмитрий",
        "Middlename": "Александрович",
        "Position": "Куратор",
        "Salary": "33000",
        "BeginDate": date(2017,7,3),
        "DepId": "2",
    }, 
    {
        "Lastname": "Левый",
        "Firstname": "Максим",
        "Middlename": "Егорович",
        "Position": "Куратор",
        "Salary": "26000",
        "BeginDate": date(2017,6,25),
        "DepId": "3",
    },  
    {
        "Lastname": "Правый",
        "Firstname": "Георгий",
        "Middlename": "Павлович",
        "Position": "Куратор",
        "Salary": "23000",
        "BeginDate": date(2017,1,1),
        "DepId": "7",
    }, 
    {
        "Lastname": "Шуров",
        "Firstname": "Александр",
        "Middlename": "Максимович",
        "Position": "Куратор",
        "Salary": "30000",
        "BeginDate": date(2017,7,3),
        "DepId": "3",
    }, 

]
)
for entryEmployees in dataEmployees:
    entryEmployees["BeginDate"] = entryEmployees["BeginDate"].isoformat()

statementEmployees = cursor.executemany(
    """INSERT INTO Employees(Lastname, Firstname, Middlename, Position, Salary,BeginDate, DepId)
       VALUES(:Lastname, :Firstname, :Middlename, :Position, :Salary, :BeginDate, :DepId);""",
    dataEmployees
)


conn.commit()
conn.close()