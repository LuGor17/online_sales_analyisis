from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Added product: {product.name}")

    def display_products(self):
        if not self.products:
            print("No products available.")
        for product in self.products:
            product.display_info()

    def total_value(self):
        total = sum(product.price * product.quantity for product in self.products)
        print(f"Total inventory value: {total}")
        return total
    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Removed product: {product_name}")
                return
        print(f"Product '{product_name}' not found.")