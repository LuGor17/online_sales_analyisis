from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        self.cart_items.append(product)
        print(f"Added {product.name} to cart.")

    def total_amount(self):
        total = sum(product.price * product.quantity for product in self.cart_items)
        return total

    def display_cart(self):
        if not self.cart_items:
            print("Cart is empty.")
        else:
            print("Cart contents:")
            for product in self.cart_items:
                print(f"- {product.name}, Price: {product.price}, Quantity: {product.quantity}")