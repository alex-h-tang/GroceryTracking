import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, Response
from werkzeug.exceptions import abort
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hwqweh82q9r854jadsnvOsfasrga0956ADST4CS'

login_manager = LoginManager(app)
login_manager.login_view = "login"

class User(UserMixin):
    def __init__(self, username, email, password, admin, active=True):
         self.id = username
         self.email = email
         self.password = password
         self.admin = admin
         self.active = active
    def is_active(self):
         return self.active
    def is_anonymous(self):
         return False
    def is_authenticated(self):
        return True
    def is_admin(self):
         return self.admin
    def get_username(self):
         return self.id

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
    prices = {}
    for url in urls:
        print((url['url_id']))
        prices[url['url_id']] = get_price(url['url_id'])
    return render_template('product.html', product=name, category=cate, cate_id=cateid, urls=urls, prices=prices)

@app.route('/update/<int:product_id>/<int:url_id>', methods=('GET', 'POST'))
def update(url_id, product_id):
    new_price = -99999999
    if not current_user.is_authenticated:
        flash("no user currently logged in")
        return redirect(url_for('login'))
    if not current_user.is_admin():
        flash("only admins can update price")
        return redirect(url_for('index'))
    if request.method == 'POST':
        new_price = request.form['new_price']

        if not new_price:
            flash("new price is required")
        else:
            update_price(url_id, new_price)
            return redirect(url_for('product', product_id=product_id))
    return render_template('edit.html')

@login_manager.user_loader
def load_user(username):
   conn = get_db_connection()
   curs = conn.cursor()
   curs.execute("SELECT * from Accounts where username = (?)", [username])
   lu = curs.fetchone()
   if lu is None:
      return None
   else:
      return User(lu[0], lu[1], lu[2], int(lu[3]))

@app.route('/login', methods=('GET', 'POST'))
def login():
    conn = get_db_connection()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        if not username or not password:
            flash("password/username is required")

        else:
            check = conn.execute('SELECT * FROM Accounts WHERE username = ? and password = ?', (username, password,)).fetchone()
            if not check:
                flash("wrong username/password")
            else:
                user = list(check)
                Us = load_user(user[0])
                login_user(Us, remember=remember)
                return redirect(url_for('index'))
    return render_template('login.html')

def get_db_connection():
    conn = sqlite3.connect('database.db', timeout=10)
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
    urls = conn.execute('SELECT * FROM vUrlDetails WHERE product_id = ?', (product_id,)).fetchall()
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

def get_price(url_id):
    conn = get_db_connection()
    price = conn.execute('SELECT price FROM Prices WHERE url_id = ? ORDER BY price_dt DESC', (url_id,)).fetchone()
    if price is None:
        return -99999999
    conn.close()
    return price[0]

def update_price(url_id, price):
    conn = get_db_connection()
    conn.execute(f'INSERT INTO Prices (url_id, price) VALUES ({url_id}, {price})')
    conn.commit()
    conn.close()
    return

@app.route('/signup', methods=('GET', 'POST'))
def sign_up():
    conn = get_db_connection()
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        if not email or not password or not username:
            flash("email/password/username is required")
        else:
            row = conn.execute('SELECT * FROM Accounts WHERE username = ?', (username,)).fetchone()
            if not row:
                conn.execute('INSERT INTO Accounts (username, password, email) VALUES (?, ?, ?)', (username, password,
                                                                                                   email))
                conn.commit()
                conn.close()
                return redirect(url_for('login'))
            else:
                flash("username already exists")
    return render_template('create.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401

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
