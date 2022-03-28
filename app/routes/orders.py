from app import app, login
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Item, Order, Post, Comment
from app.classes.forms import ItemForm, OrderForm, PostForm, CommentForm
from flask_login import login_required
import datetime as dt

@app.route('/order/list')
def orderList():
    orders = Order.objects()
    return render_template('orders.html', orders = orders)

@app.route('/order/new', methods=['GET', 'POST'])
def orderNew():
    form = OrderForm()

    if form.validate_on_submit():
        newOrder = Order(
            name = form.name.data,

        )
        newOrder.save()

        return redirect(url_for('orderList'))
    return render_template('orderform.html', form = form)
