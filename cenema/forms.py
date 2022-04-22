#!/usr/bin/python3


from flask_wtf import FlaskForm
from wtforms import (DateTimeField, FloatField, TextAreaField, HiddenField, FieldList,
                     FormField, IntegerField, SubmitField, validators, StringField)
from wtforms.validators import (DataRequired, Required, email_validator,
                                ValidationError, Email, EqualTo, Length)
from .models import Booking

"""
class NumberOfTicketsForm(FlaskForm):
    num_tickets = IntegerField('How many tickets?')
    ticket_type = HiddenField()

    def __init__(self, ticket_type_label, *args, **kwargs):
        super(NumberOfTicketsForm, self).__init__(*args, **kwargs)
        self.num_tickets.label.text = 'How many %s tickets?' % ticket_type_label
"""

"""
class AddTicketsForm(FlaskForm):
    tickets = FieldList(FormField(NumberOfTicketsForm), min_entries=1, validators=[Required()])
    showing_id = HiddenField('Showing', validators=[Required()])
    submit = SubmitField('Submit')
"""

class BookingForm(FlaskForm):
    email = StringField('', [validators.Length(min=2, max=35),
                                          validators.Email()])
    submit = SubmitField('Submit')

    """Email taken"""
    def validate_email(self, email):
        email = Booking.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email is taken')
