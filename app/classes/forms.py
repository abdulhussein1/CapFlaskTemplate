# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask.app import Flask
from flask import flash
from flask_wtf import FlaskForm
from mongoengine.fields import EmailField
import mongoengine.errors
from wtforms.validators import URL, NumberRange, Email, Optional, InputRequired, ValidationError, DataRequired, EqualTo, Length
from wtforms import PasswordField, StringField, SubmitField, TextAreaField, HiddenField, IntegerField, SelectField, FileField, BooleanField
from app.classes.data import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me?')
    submit = SubmitField()

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])  
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        try:
            User.objects.get(username=username.data)
        except mongoengine.errors.DoesNotExist:
            flash(f"{username.data} is available.")
        else:
            raise ValidationError('This username is taken.')

    def validate_email(self, email):
        try:
            User.objects.get(email=email.data)
        except mongoengine.errors.DoesNotExist:
            flash(f'{email.data} is a unique email address.')
        else:
            raise ValidationError('This email address is already in use. if you have forgotten your credentials you can try to recover your account.')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    submit = SubmitField('Post')
    role = SelectField('Role', choices = [("admin", "admin"), ("randUser", "randUser")])
    favColor = StringField('Favorite Color', validators=[DataRequired()])
    mascot = SelectField('Mascot', choices=[('bulldog', 'bulldog'), ('lion', 'lion')])

class PostForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Post', validators=[DataRequired()])
    submit = SubmitField('Post')
    rating = SelectField('Rating', choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')])
    likes = SubmitField('Like')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class ItemForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    submit = SubmitField('Submit')
    price = IntegerField('Price', validators=[DataRequired()])
    stock = IntegerField('Stock', validators=[DataRequired()])

class IngredientForm(FlaskForm):
    label = StringField('Ingredient', validators=[DataRequired()])
    submit = SubmitField('Add Ingredient')

class DonationsForm(FlaskForm):
    amount = IntegerField("Donation Amount", validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    country = SelectField('Country', choices=[('United States', 'United States')])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = SelectField('State', choices=[('California', 'California'), ('Kentucky', 'Kentucky')])
    zip = IntegerField('Zip Code', validators=[DataRequired()])
    phone_number = IntegerField('Phone Number', validators=[DataRequired()])
    currency = SelectField('Currency', choices=[('USD', 'USD')])
    card_number = IntegerField('Credit Card Number', validators=[DataRequired()])
    cvv = StringField('CVV', validators=[DataRequired(), Length(min=3, max=3)])
    month =  SelectField('Expiration Date', choices=[('January','January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')])
    year = StringField('Year', validators=[DataRequired(), Length(min=4, max=4)])
    submit = SubmitField('Donate')




