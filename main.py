class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name}: ${self.price} (Stock: {self.stock})"

class Cart:
    def __init__(self):
        self.items = {}
    def add_product(self, product, quantity):
        if product.stock >= quantity:
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            product.stock -= quantity
            print(f"Added {quantity} of {product.name} to the cart.")
        else:
            print(f"Insufficient stock for {product.name}. Only {product.stock} available.")

    def remove_product(self, product, quantity):
        if product in self.items:
            if quantity >= self.items[product]:
                product.stock += self.items[product]
                del self.items[product]
                print(f"Removed all {product.name} from the cart.")
            else:
                self.items[product] -= quantity
                product.stock += quantity
                print(f"Removed {quantity} of {product.name} from the cart.")
        else:
            print(f"{product.name} is not in the cart.")

    def total_price(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def show_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            for product, quantity in self.items.items():
                print(f"{product.name} - {quantity} pcs - ${product.price * quantity}")
            print(f"Total Price: ${self.total_price()}")

product1 = Product("Laptop", 1000, 5)
product2 = Product("Phone", 500, 10)
product3 = Product("Headphones", 150, 20)

cart = Cart()

cart.add_product(product1, 1)
cart.add_product(product2, 2)
cart.add_product(product3, 3)

cart.show_cart()

cart.remove_product(product2, 1)

cart.show_cart()

