from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)
# env = Environment(loader=FileSystemLoader("templates/"))
# template = env.get_template("index.html")
def create_table():
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL, years INTEGER, owner TEXT, contact TEXT, image BLOB)')
    conn.commit()
    conn.close()

def insert_data(product_name, product_price, used_years, owner_name, contact, image):
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute('INSERT INTO products (name, price, years,owner,contact,image) VALUES (?, ?, ?, ?, ?, ?)', (product_name, product_price, used_years, owner_name, contact, image))
    conn.commit()
    conn.close()

def fetch_all_data():
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute('SELECT * FROM products')
    rows = c.fetchall()
    conn.close()
    return rows

def delete_item(name):
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute('DELETE FROM products WHERE name = {name}')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/help') 
def help():
    return render_template('help.html')

@app.route('/vehicles') 
def vehicles():
    return render_template('vehicles.html')
@app.route('/electronics') 
def electronics():
    return render_template('electronics.html')
@app.route('/furnitures') 
def furnitures():
    return render_template('furnitures.html')
@app.route('/books') 
def books():
    return render_template('books.html')
@app.route('/view') 
def view():
    items = fetch_all_data()
    return render_template('view.html',items=items)


@app.route('/sell', methods=['GET', 'POST'])
def sell():
    if request.method == 'POST':
        product_name = request.form['product_name']
        product_price = request.form['product_price']
        used_years = request.form['used_years'] 
        owner_name = request.form['owner_name'] 
        contact = request.form['contact'] 
        image = request.files['image'].read()
        
        insert_data(product_name, product_price, used_years, owner_name, contact, image)
        return redirect(url_for('index'))
    items = fetch_all_data()
    return render_template('sell.html', items=items)

@app.route('/delete_item', methods=['POST'])
def delete_items():
    delete_item()
    return redirect(url_for('sell'))

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
