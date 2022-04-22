#!/usr/bin/python3
"""routes"""

from flask import Flask, request
from .forms import BookingForm
from cenema import app, db
from wtforms.validators import email
from flask import render_template, url_for, flash, redirect
from .models import Booking
import email_validator



@app.route('/')
@app.route("/booking", methods=['GET','POST'])
def booking():
    emails = Booking.query.all()
    form = BookingForm(request.form)
    """add email withs spesific form"""
    if request.method == 'POST':
        booking = Booking(email=form.email.data)
        db.session.add(booking)
        db.session.commit()
        flash(f"your {form.email.data} has been aded","success")
        user = Booking.query.filter(Booking.email==email).first()
        if user != None: # the query has returned a user
            flash("Please use a different email.")
    else:
        flash("plz add the forms")
    booking = request.form.get('booking')
    return render_template('More_Information.html', form=form, BookingForm=BookingForm, emails=emails)
