"""
Dummy E-commerce Code for GitHub + Jira Testing
Author: Demo
Purpose: Placeholder code for frontend, backend, and test simulation.
"""

# ---------------- Backend Simulation ----------------
## pr CRM-13 change
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        print(f"Added {product.name} to cart.")

    def remove_item(self, product_id):
        self.items = [p for p in self.items if p.id != product_id]
        print(f"Removed product {product_id} from cart.")

def apply_coupon(cart, coupon_code):
    if coupon_code == "DISCOUNT10":
        print("Coupon applied! 10% discount.")
    else:
        print("Invalid coupon.")

# ---------------- Frontend Simulation ----------------

def show_homepage():
    print("Welcome to E-Commerce Dummy Website!")
    print("1. Browse Products")
    print("2. View Cart")
    print("3. Checkout")

def show_product(product):
    print(f"Product: {product.name}")
    print(f"Price: ${product.price}")

# ---------------- Test Simulation ----------------

def test_add_to_cart():
    p = Product(1, "Demo Product", 100)
    cart = Cart()
    cart.add_item(p)
    assert len(cart.items) == 1
    print("test_add_to_cart passed!")

def test_apply_coupon():
    cart = Cart()
    apply_coupon(cart, "DISCOUNT10")  # Dummy check
    print("test_apply_coupon passed!")

# ---------------- Main ----------------

if __name__ == "__main__":
    show_homepage()
    p1 = Product(1, "Laptop", 1200)
    show_product(p1)
    cart = Cart()
    cart.add_item(p1)
    apply_coupon(cart, "DISCOUNT10")

    # Run dummy tests
    test_add_to_cart()
    test_apply_coupon()
