class Restaurant:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def reviews(self):
        cursor = conn.cursor()
        cursor.execute("SELECT id, customer_id, rating FROM reviews WHERE restaurant_id=?", (self.id,))
        review_data = cursor.fetchall()
        reviews = []
        for review_id, customer_id, rating in review_data:
            customer = Customer.from_database(conn, customer_id)
            reviews.append(Review(review_id, customer, self, rating))
        return reviews

    def customers(self):
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT customer_id FROM reviews WHERE restaurant_id=?", (self.id,))
        customer_ids = cursor.fetchall()
        customers = []
        for customer_id in customer_ids:
            customer = Customer.from_database(conn, customer_id)
            customers.append(customer)
        return customers
