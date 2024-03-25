import sqlite3

conn = sqlite3.connect("restaurants.db")
cursor = conn.cursor()

conn.execute('''CREATE TABLE IF NOT EXISTS restaurants(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 price INTEGER NOT NULL 
    )''')


conn.execute('''CREATE TABLE IF NOT EXISTS customers(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 first_name TEXT NOT NULL,
                 last_name INTEGER NOT NULL 
    )''')

conn.execute('''CREATE TABLE IF NOT EXISTS reviews(
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 restaurant_id INTEGER NOT NULL,
                 customer_id INTEGER NOT NULL,
                 star_rating TEXT NOT NULL, 
                 FOREIGN KEY (restaurant_id) REFERENCES restaurants(id),
                 FOREIGN KEY (customer_id) REFERENCES customers(id)
    )''')

conn.commit()


# Populate customers table
cursor.execute("INSERT INTO customers (first_name, last_name) VALUES (?, ?)", ("John", "Doe"))
cursor.execute("INSERT INTO customers (first_name, last_name) VALUES (?, ?)", ("Jane", "Smith"))
cursor.execute("INSERT INTO customers (first_name, last_name) VALUES (?, ?)", ("Alice", "Johnson"))

# Populate restaurants table
cursor.execute("INSERT INTO restaurants (name, price) VALUES (?, ?)", ("Restaurant A", 10))
cursor.execute("INSERT INTO restaurants (name, price) VALUES (?, ?)", ("Restaurant B", 20))
cursor.execute("INSERT INTO restaurants (name, price) VALUES (?, ?)", ("Restaurant C", 15))

# Populate reviews table
cursor.execute("INSERT INTO reviews (customer_id, restaurant_id, star_rating) VALUES (?, ?, ?)", (1, 1, 4.5))
cursor.execute("INSERT INTO reviews (customer_id, restaurant_id, star_rating) VALUES (?, ?, ?)", (2, 1, 3.0))
cursor.execute("INSERT INTO reviews (customer_id, restaurant_id, star_rating) VALUES (?, ?, ?)", (3, 2, 5.0))

# Commit the changes and close the connection
conn.commit()
conn.close()