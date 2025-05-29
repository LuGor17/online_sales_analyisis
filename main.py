from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()

    # Dodavanje nekoliko proizvoda
    product1 = Product("Gaming Laptop", 1500, 3)
    product2 = Product("Wireless Mouse", 30, 15)
    product3 = Product("Mechanical Keyboard", 60, 5)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

    # Prikaz proizvoda
    manager.display_products()

    # Prikaz ukupne vrednosti inventara
    manager.total_value()

if __name__ == "__main__":
    main()