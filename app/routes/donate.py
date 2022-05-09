from app import app, login
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Post, Comment, Donations
from app.classes.forms import PostForm, CommentForm, DonationsForm
from flask_login import login_required
import datetime as dt

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/donate/info<amount>', methods=['GET', 'POST'])
def info(amount):
    form = DonationsForm()

    form.amount.data = amount

    if form.validate_on_submit():
        newDonation = Donations(
            amount = form.amount.data,
            fname = form.fname.data,
            lname = form.lname.data,
            country = form.country.data,
            address = form.address.data,
            city = form.city.data,
            state = form.state.data,
            zip = form.zip.data,
            phone_number = form.phone_number.data,
            currency = form.currency.data,
            card_number = form.card_number.data,
            cvv = form.cvv.data,
            month = form.month.data,
            year = form.year.data
        )

        newDonation.save()
    
        return redirect(url_for('thankyou', fname = form.fname.data))

    return render_template('info.html', form = form)


@app.route('/donate/thanks<fname>', methods=['GET', 'POST'])
def thankyou(fname):
    return render_template('thankyou.html', fname = fname)