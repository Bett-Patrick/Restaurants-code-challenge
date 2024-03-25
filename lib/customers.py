class Customer:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def reviews(self):
        cursor = conn.cursor()
        cursor.execute("SELECT id, restaurant_id, rating FROM reviews WHERE customer_id=?", (self.id,))
        review_data = cursor.fetchall()
        reviews = []
        for review_id, restaurant_id, rating in review_data:
            restaurant = Restaurant.from_database(conn, restaurant_id)
            reviews.append(Review(review_id, self, restaurant, rating))
        return reviews

    def restaurants(self):
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT restaurant_id FROM reviews WHERE customer_id=?", (self.id,))
        restaurant_ids = cursor.fetchall()
        restaurants = []
        for restaurant_id in restaurant_ids:
            restaurant = Restaurant.from_database(conn, restaurant_id)
            restaurants.append(restaurant)
        return restaurants
