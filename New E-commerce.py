from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Mock database
products = [
    {'id': 1, 'name': 'Laptop', 'price': 1000, 'stock': 10},
    {'id': 2, 'name': 'Smartphone', 'price': 500, 'stock': 20},
    {'id': 3, 'name': 'Headphones', 'price': 100, 'stock': 50},
]

cart = []

@app.route('/')
def home():
    return render_template('home.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product and product['stock'] > 0:
        cart.append(product)
        product['stock'] -= 1
    return redirect(url_for('home'))

@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart)

@app.route('/checkout', methods=['POST'])
def checkout():
    cart.clear()
    return render_template('checkout.html', message="Purchase successful!")

if __name__ == '__main__':
    app.run(debug=True)