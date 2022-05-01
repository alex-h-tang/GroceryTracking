import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hwqweh82q9r854jadsnvOsfasrga0956ADST4CS'

@app.route('/')
def index():
    conn = get_db_connection()
    cates = conn.execute('SELECT * FROM Categories').fetchall()
    conn.close()
    return render_template('index.html', categories=cates)
    
@app.route('/category/<int:category_id>')
def category(category_id):
    products = get_category_products(category_id)
    catename = get_category_name(category_id)
    return render_template('category.html', catename=catename, products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    urls = get_product_urls(product_id)
    name, cate, cateid = get_product_info(product_id)
    return render_template('product.html', product=name, category=cate, cate_id=cateid, urls=urls)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_category_products(cate_id):
    conn = get_db_connection()
    products = conn.execute('SELECT * FROM Products WHERE category_id = ?', (cate_id,)).fetchall()
    conn.close()
    if products is None:
        abort(404)
    return products

def get_all_categories():
    conn = get_db_connection()
    cates = conn.execute('SELECT * FROM Categories').fetchall()
    conn.close()
    if cates is None:
        abort(404)
    return cates

def get_category_name(cate_id):
    conn = get_db_connection()
    catename = conn.execute('SELECT category_name FROM Categories WHERE category_id = ?', (cate_id,)).fetchone()
    conn.close()
    if catename is None:
        abort(404)
    return catename[0]

def get_product_urls(product_id):
    conn = get_db_connection()
    urls= conn.execute('SELECT * FROM vUrlDetails WHERE product_id = ?', (product_id,)).fetchall()
    conn.close()
    if urls is None:
        abort(404)
    return urls

def get_product_info(prod_id):
    conn = get_db_connection()
    name, cate_id = conn.execute('SELECT name,category_id FROM Products WHERE product_id = ?', (prod_id,)).fetchone()
    if cate_id:
        cate = conn.execute('SELECT category_name FROM Categories WHERE category_id = ?', (cate_id,)).fetchone()
    conn.close()
    if name is None or cate is None:
        abort(404)
    return name, cate[0], cate_id


# @app.route('/create', methods=('GET', 'POST'))
# def create():
#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']
#
#         if not title:
#             flash('Title is required!')
#         else:
#             conn = get_db_connection()
#             conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
#                          (title, content))
#             conn.commit()
#             conn.close()
#             return redirect(url_for('index'))
#
#     return render_template('create.html')

# @app.route('/<int:id>/edit', methods=('GET', 'POST'))
# def edit(id):
#     post = get_category(id)
#
#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']
#
#         if not title:
#             flash('Title is required!')
#         else:
#             conn = get_db_connection()
#             conn.execute('UPDATE posts SET title = ?, content = ?'
#                          ' WHERE id = ?',
#                          (title, content, id))
#             conn.commit()
#             conn.close()
#             return redirect(url_for('index'))
#
#     return render_template('edit.html', post=post)

# @app.route('/<int:id>/delete', methods=('POST',))
# def delete(id):
#     post = get_category(id)
#     conn = get_db_connection()
#     conn.execute('DELETE FROM posts WHERE id = ?', (id,))
#     conn.commit()
#     conn.close()
#     flash('"{}" was successfully deleted!'.format(post['title']))
#     return redirect(url_for('index'))
