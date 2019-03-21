from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, session
from flask_login import login_user, current_user, logout_user, login_required
from shop import app, db
from shop.models import User, Item, W_item, payment
from shop.forms import RegisterForm, LoginForm
from flask_sqlalchemy import SQLAlchemy

@app.route("/")
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/mens', methods=['GET', 'POST'])
def mens():
    Items  = Item.query.all()
    return render_template('men_index.html', items=Items)


@app.route('/men/<string:id>/')
def men(id):
    item = Item.query.get_or_404(id)
    return render_template('item_view.html', item=item)

@app.route('/womens')
def womens():
    Items  = W_item.query.all()
    return render_template('women_index.html', items = Items)

@app.route('/women/<string:id>/')
def women(id):
    item = W_item.query.get_or_404(id)
    return render_template('item_view.html', item=item)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now registered and can log in', 'success')
        return redirect(url_for('sign_in'))
    return render_template('register.html',  form=form)


@app.route('/sign_in_page', methods=['GET', 'POST'])
def sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            flash("You are now Logged In!", 'success')
            session['logged_in'] = True
            return redirect(url_for("index"))
        flash("Invalid username or password.", 'danger')

        return render_template("sign_in_page.html", form=form)

    return render_template('sign_in_page.html', title='Login', form=form)


@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('sign_in'))

@app.route('/review')
def review():
    Items  = Item.query.all()
    Items_2 = W_item.query.all()
    return render_template('review.html', items = Items, items_2=Items_2)

@app.route("/add_to_cart/<string:id>/")
def add_to_cart(id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(id)
    flash('The item has been added to your basket', 'success')
    return redirect("/basket")

@app.route('/basket', methods=['GET', 'POST'])
def basket():
    if 'cart' not in session:
        flash('There is nothing in your basket.', 'danger')
        return render_template('basket.html', display_cart = {}, total = 0)
    else:
        products = session['cart']
        cart = {}

        total_price = 0
        total_quantity = 0
        s_total = 0
        for product in products:
            item = Item.query.get_or_404(product)

            total_price += item.price
            s_total = int(total_price) * 0.85

            if item.id in cart:
                cart[item.id]["quantity"] += 1
            else:
                cart[item.id] = {'quantity':1, 'Product name': item.item_name, 'price':item.price}
            total_quantity = sum(product['quantity'] for product in cart.values())

        return render_template('basket.html', display_cart = cart, total = total_price, total_quantity = total_quantity, sub_total = s_total)
    return render_template('basket.html')

@app.route("/delete_item/<string:id>", methods=['GET', 'POST'])
def delete_item(id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].remove(id)

    flash('The item has been removed from your basket', 'success')
    session.modified = True
    return redirect('/basket')

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    return render_template('checkout.html', title='Checkout')
