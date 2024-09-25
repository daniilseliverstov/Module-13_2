import sqlite3


def initiate_db():
    connection = sqlite3.connect('Product.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    title = ['Product 1', 'Product 2', 'Product 3', 'Product 4']
    description = ['Описание 1', 'Описание 2', 'Описание 3', 'Описание 4']
    price = ['100', '200', '300', '400']

    for prod in range(len(title)):
        cursor.execute('INSERT INTO Products(title, description, price) VALUES (?, ?, ?)',
                       (f'{title[prod]}', f'{description[prod]}', f'{price[prod]}'))
    connection.commit()
    connection.close()


initiate_db()


def get_all_products():
    connection = sqlite3.connect('Product.db')
    cursor = connection.cursor()
    cursor.execute("SELECT title, description, price FROM Products")
    db = cursor.fetchall()
    return list(db)
