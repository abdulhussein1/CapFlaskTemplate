from email.policy import default
from app import app, login
import mongoengine.errors
from flask import render_template, flash, redirect, url_for, request, session
from flask_login import current_user
from app.classes.data import Cart, Item, Post, Comment, User
from app.classes.forms import ItemForm, PostForm, CommentForm
from flask_login import login_required
import datetime as dt



@app.route('/shop', methods=['POST', 'GET'])
@login_required
def shop():
    items = Item.objects()
    return render_template('shop.html', items = items)

@app.route('/shop/cart/<itemID>')
@login_required
def addToCart(itemID):
    items = Item.objects()
    for item in items:
        if str(item.id) == str(itemID):
            newItem = Cart(
                username = current_user.username,
                label = item.item,
                price = item.price
            )
            newItem.save()
    return redirect(url_for('shop'))

@app.route('/shop/cart/clear')
@login_required
def clearCart():
    for object in Cart.objects():
        if object.username == current_user.username:
            object.delete()
    return redirect(url_for('shop'))

@app.route('/shop/cart')
@login_required
def viewCart():
    cart = []
    total = 0
    for object in Cart.objects():
        if object.username == current_user.username:
            cart.append(object)
            total += object.price
    return render_template('cart.html', cart = cart, total = total)

@app.route('/shop/delete/<itemID>')
@login_required
def cartItemDelete(itemID):
    for object in Cart.objects():
        if str(object.id) == str(itemID) and (object.username == current_user.username):
            object.delete()
    return redirect(url_for('viewCart'))

@app.route('/shop/cart/checkout')
def checkout():
    cart = []
    items = Item.objects()
    form = ItemForm()
    for object in Cart.objects():
        if object.username == current_user.username:
            cart.append(object)
    for object in cart:
        for item in items:
            if object.label == item.item:
                editItem = Item.objects.get(item = object.label)
                editItem.stock = editItem.stock - 1
                editItem.update(
                    stock = editItem.stock
                )
                form.stock.data = editItem.stock
    return redirect(url_for('clearCartandReturn'))

@app.route('/shop/cart/clearReturn')
def clearCartandReturn():
    for object in Cart.objects():
        if object.username == current_user.username:
            object.delete()
    return render_template('purchase.html')