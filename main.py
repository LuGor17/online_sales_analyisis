from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()

    # Dodavanje nekoliko proizvoda
    product1 = Product("Laptop", 1200, 5)
    product2 = Product("Mouse", 25, 10)
    product3 = Product("Keyboard", 45, 7)

    manager.add_product(product1)
    manager.add_product(product2)
    manager.add_product(product3)

    # Prikaz proizvoda
    manager.display_products()

    # Prikaz ukupne vrednosti inventara
    manager.total_value()

if __name__ == "__main__":
    main()