## Code Explanation: E-commerce System Core Classes

This section details the primary classes that constitute the core functionality of our e-commerce system.

**1. `Product` Class:**

* Represents an individual product available for sale.
* **Attributes:**
    * `name` (string): The product's name.
    * `price` (numeric): The product's price.
    * `stock` (integer): The current stock quantity.
* **Method:**
    * `update_stock()`: Decrements the `stock` attribute when a product is added to a `ShoppingCart`.

**2. `Customer` Class:**

* Represents a customer within the system.
* **Attributes:**
    * `name` (string): The customer's name.
    * `shopping_cart` (ShoppingCart object): An associated `ShoppingCart` instance.
* **Methods:**
    * `add_to_cart()`: Adds a `Product` to the customer's `shopping_cart`.
    * `remove_from_cart()`: Removes a `Product` from the customer's `shopping_cart`.

**3. `ShoppingCart` Class:**

* Manages the collection of `Product` objects in a customer's cart.
* **Attributes:**
    * `items` (dictionary): Stores `Product` objects and their quantities.
* **Methods:**
    * `add()`: Adds a `Product` to the cart.
    * `remove()`: Removes a `Product` from the cart.
    * `apply_discount()`: Calculates the total cost after applying discounts.

**4. `Order` Class:**

* Represents a finalized purchase order.
* Calculates the total price based on the `ShoppingCart` contents.
* **Method:**
    * `process_order()`: Clears the `shopping_cart` after purchase and processes the order.

**5. Example Transaction:**

* Demonstrates a typical transaction scenario:
    * A `Customer` (e.g., Alice) adds a "Laptop" and a "Phone" to their `ShoppingCart`.
    * Upon order placement, the system:
        * Updates the `stock` of the purchased products.
        * Calculates the total order price.
        * Outputs a confirmation message.
 adds a laptop and a phone to her shopping cart. When she places an order, the system deducts the
 stock, calculates the total, and prints a confirmation message.
 ©D
