class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def add_stock(self, quantity):
        self.stock += quantity

    def remove_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
        else:
            raise ValueError("Not enough stock available.")

    def __str__(self):
        return f"{self.name} - ${self.price} ({self.stock} in stock)"


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()

    def __str__(self):
        return f"Customer: {self.name}"


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product.stock >= quantity:
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            product.remove_stock(quantity)
        else:
            raise ValueError("Not enough stock available.")

    def remove_item(self, product, quantity):
        if product in self.items and self.items[product] >= quantity:
            self.items[product] -= quantity
            if self.items[product] == 0:
                del self.items[product]
            product.add_stock(quantity)
        else:
            raise ValueError("Item not in cart or insufficient quantity.")

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items.items())

    def apply_discount(self, discount_percentage):
        total = self.calculate_total()
        return total - (total * discount_percentage / 100)

    def __str__(self):
        return f"Cart: {[f'{product.name} x {quantity}' for product, quantity in self.items.items()]}"


class Order:
    def __init__(self, customer, cart):
        self.customer = customer
        self.cart = cart
        self.is_confirmed = False

    def checkout(self):
        if not self.cart.items:
            raise ValueError("Cart is empty.")
        self.is_confirmed = True
        return f"Order confirmed for {self.customer.name}. Total: ${self.cart.calculate_total()}"

    def __str__(self):
        return f"Order for {self.customer.name}: {self.cart}"


class ReturnRequest:
    def __init__(self, order, product, reason, days_since_purchase):
        self.order = order
        self.product = product
        self.reason = reason
        self.days_since_purchase = days_since_purchase

    def process_return(self):
        if not self.order.is_confirmed:
            raise ValueError("Order not confirmed.")
        if self.product not in self.order.cart.items:
            raise ValueError("Product not in order.")
        if self.days_since_purchase > 30:
            raise ValueError("Return period expired.")
        self.product.add_stock(self.order.cart.items[self.product])
        del self.order.cart.items[self.product]
        return f"Return processed for {self.product.name} due to '{self.reason}'."

    def __str__(self):
        return f"Return Request: {self.product.name} - Reason: {self.reason}"


# Example usage
if __name__ == "__main__":
    # Create products
    product1 = Product("Laptop", 1000, 10)
    product2 = Product("Phone", 500, 20)

    # Create a customer
    customer = Customer("Alice")

    # Add items to cart
    customer.cart.add_item(product1, 1)
    customer.cart.add_item(product2, 2)

    # Checkout
    order = Order(customer, customer.cart)
    print(order.checkout())

    # Process a return
    return_request = ReturnRequest(order, product2, "Defective item", 10)
    print(return_request.process_return())