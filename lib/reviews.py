from customers import Customer
from restaurants import Restaurant
from database import conn

class Review:
    all_reviews = []
    def __init__(self,id,customer,restaurant,rating):
        if not isinstance(restaurant, Restaurant):
            raise ValueError("restaurant id should be an instance of Restaurant.")
        if not isinstance(customer, Customer):
            raise ValueError("customer id should be an instance of Customer.")
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.id = id

    def customer(self):
        cursor = conn.cursor()
        cursor.execute("SELECT first_name, last_name FROM customers WHERE id=?", (self.customer.id,))
        full_name = cursor.fetchone()
        if full_name:
            first_name,last_name = full_name
            return Customer(first_name, last_name)
        else:
            return None

    def restaurant(self):
        cursor = conn.cursor()
        cursor.execute("SELECT name, price FROM restaurants WHERE id=?", (self.restaurant.id,))
        rest_data = cursor.fetchone()
        if rest_data:
            name,price = rest_data
            return Restaurant(name, price)
        else:
            return None
