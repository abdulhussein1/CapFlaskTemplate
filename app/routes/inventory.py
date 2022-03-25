from app import app, login
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Item, Post, Comment
from app.classes.forms import ItemForm, PostForm, CommentForm
from flask_login import login_required
import datetime as dt

@app.route('/inventory')
def inventory():
    items = Item.objects()
    return render_template('inventory.html', items = items)

@app.route('/inventory/new', methods=['GET', 'POST'])
def itemNew():
    form = ItemForm()

    if form.validate_on_submit():
        newItem = Item(
            item = form.item.data
        )

        newItem.save()
    
        return redirect(url_for('inventory'))

    return render_template('itemform.html', form = form)