import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE orders
#              (text, trans text, symbol text, qty real, price real)''')


# Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# EXISTING ORDERS
# Create table
c.execute('''CREATE TABLE IF NOT EXISTS orders
             (order_date, order_number, order_phone, color, size, status)''')

# data to be added
# purchases = [('2006-01-05',123456,'example@rasa.com','blue', 9, 'shipped'),
#              ('2021-01-05',123457,'me@rasa.com','black', 10, 'order pending'),
#              ('2021-01-05',123458,'me@gmail.com','gray', 11, 'delivered'),
#              ('2021-01-05',123459,'me@jpmc.com', 'green', 10, 'delivered'),
#              ('2021-01-05',123460,'hello@hotstar.com','black', 11, 'shipped'),
#             ]
purchases = [('2021-4-21', 171126, '9356 927 800', 'black',8,'order pending'),
             ('2021-4-21', 171126, '935 692 7800', 'blue', 10, 'shipped'),
             ('2021-4-21', 171126, '8171 427 101', 'gray', 9, 'delivered'),
             ('2021-4-21', 171126, '817 1427 101', 'black', 11, 'shipped'),
]

# add data
c.executemany('INSERT INTO orders VALUES (?,?,?,?,?,?)', purchases)

# AVAILABLE INVENTORY
# Create table
c.execute('''CREATE TABLE IF NOT EXISTS inventory
             (size, color)''')

# data to be added
inventory = [(7, 'blue'),
             (8, 'blue'),
             (9, 'blue'),
             (10, 'blue'),
             (11, 'blue'),
             (12, 'blue'),
             (7, 'black'),
             (8, 'black'),
             (9, 'black'),
             (10, 'black')
            ]

# add data
c.executemany('INSERT INTO inventory VALUES (?,?)', inventory)


# Save (commit) the changes
conn.commit()

# end connection
conn.close()
