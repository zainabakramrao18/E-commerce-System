class Product:
    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.reviews = []

    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False

    def add_review(self, review):
        self.reviews.append(review)

    def get_details(self):
        print(f"\nProduct: {self.name}, Price: ${self.price}, Stock: {self.stock}, Category: {self.category}")
        if self.reviews:
            print("Reviews:")
            for review in self.reviews:
                print(f" - {review}")
        else:
            print("No reviews yet.")


class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        return self.cart.add_product(product, quantity)

    def remove_from_cart(self, product):
        return self.cart.remove_product(product)


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.update_stock(quantity):
            self.items[product] = self.items.get(product, 0) + quantity
            return True
        return False

    def remove_product(self, product):
        if product in self.items:
            product.stock += self.items[product]
            del self.items[product]
            return True
        return False

    def apply_discount(self, percentage):
        return sum(product.price * qty * (1 - percentage / 100) for product, qty in self.items.items())

    def view_cart(self):
        print("\nShopping Cart:")
        if not self.items:
            print(" - Cart is empty.")
        for product, quantity in self.items.items():
            print(f" - {product.name} x {quantity} @ ${product.price} each")


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.total_price = customer.cart.apply_discount(0)

    def process_order(self):
        total = self.customer.cart.apply_discount(0)
        self.customer.cart.items.clear()
        return f"Order processed for {self.customer.name}. Total: ${total:.2f}"

    def make_payment(self, method="Credit Card"):
        return f"Payment successfully received using {method}."


# === Data Stores ===
product_list = []
customer = None


# === Menu System ===
def show_menu():
    print("\n==== E-Commerce System ====")
    print("1. Add Product")
    print("2. View All Products")
    print("3. Add Review to Product")
    print("4. Create Customer")
    print("5. Add to Cart")
    print("6. View Cart")
    print("7. Place Order")
    print("8. Exit")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Product Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        category = input("Category: ")
        product = Product(name, price, stock, category)
        product_list.append(product)
        print(f"{name} added successfully!")

    elif choice == "2":
        if not product_list:
            print("No products available.")
        for idx, p in enumerate(product_list):
            print(f"\nProduct #{idx + 1}")
            p.get_details()

    elif choice == "3":
        if not product_list:
            print("No products to review.")
            continue
        for i, p in enumerate(product_list):
            print(f"{i + 1}. {p.name}")
        prod_idx = int(input("Select product number: ")) - 1
        review = input("Enter your review: ")
        product_list[prod_idx].add_review(review)
        print("Review added!")

    elif choice == "4":
        name = input("Customer Name: ")
        email = input("Email: ")
        address = input("Address: ")
        customer = Customer(name, email, address)
        print("Customer created.")

    elif choice == "5":
        if not customer:
            print("Create a customer first.")
            continue
        if not product_list:
            print("No products available.")
            continue
        for i, p in enumerate(product_list):
            print(f"{i + 1}. {p.name} (${p.price}) - Stock: {p.stock}")
        prod_idx = int(input("Select product number: ")) - 1
        quantity = int(input("Enter quantity: "))
        success = customer.add_to_cart(product_list[prod_idx], quantity)
        if success:
            print("Added to cart.")
        else:
            print("Not enough stock.")

    elif choice == "6":
        if not customer:
            print("No customer found.")
        else:
            customer.cart.view_cart()

    elif choice == "7":
        if not customer:
            print("No customer found.")
            continue
        order = Order(customer)
        print(order.process_order())
        method = input("Enter payment method: ")
        print(order.make_payment(method))

    elif choice == "8":
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice. Try again.")


