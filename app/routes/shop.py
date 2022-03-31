from app import app, login
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Item, Post, Comment, Cart
from app.classes.forms import ItemForm, PostForm, CommentForm, ShopForm
from flask_login import login_required
import datetime as dt

cart = []

@app.route('/shop')
def shop(): 
    items = Item.objects()
    form = ShopForm()
    return render_template('shop.html', items = items, form = form)

@app.route('/shop/cart/<itemID>', methods=['GET', 'POST'])
def addToCart(itemID):
    cart.append(itemID)
    items = Item.objects()
    label = 'abc'
    price = ''
    for item in items:
        if str(item.id) == itemID:
            label = item.item
            price = item.price
    return render_template('cart.html', label = label, price = price)

