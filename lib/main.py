from customers import Customer
from reviews import Review
from restaurants import Restaurant

try:
    # Customer instance
    customer = Customer(1, "John", "Doe")
    
    # Restaurant instance
    restaurant = Restaurant(1, "Restaurant A", 10)
    
    #Review instance
    review = Review(1, customer, restaurant, 4.5)

    print("Customer:", review.customer.first_name, review.customer.last_name)

    print("Restaurant:", review.restaurant.name)

    print("Rating:", review.rating)
except Exception as e:
    print("Test Case 1 Failed:", e)

# Customer ID that doesn't exist
try:
    review = Review(4, Customer(100, "Non-existent", "Customer"), restaurant, 3.5)

    print("Customer:", review.customer.first_name, review.customer.last_name)
except Exception as e:
    print("Test Case 4 Failed:", e)

#Restaurant ID that doesn't exist
try:
    review = Review(5, customer, Restaurant(100, "Non-existent Restaurant", 20), 4.0)

    print("Restaurant:", review.restaurant.name)
except Exception as e:
    print("Test Case 5 Failed:", e)
