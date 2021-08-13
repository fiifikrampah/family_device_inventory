from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange

from app import create_app
from db.models import Users, Devices

app = create_app()
Bootstrap(app)


class AddDevice(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    device_name = StringField('Name')
    device_type = StringField('Type')
    device_serial = StringField('Serial')
    device_model = StringField('Model')
    device_mac = StringField('MAC ADDRESS', Regexp(r'[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$'),
                             message="Invalid MAC ADDRESS")
    status = SelectField('Device Status', [InputRequired()],
                         choices=[('', ''), ('Active', 'Active'),
                                  ('Inactive', 'Inactive'),
                                  ('Abandoned', 'Abandoned'),
                                  ('Lost', 'Lost')])
    purchase_date = StringField('Color', [InputRequired()], Regexp(
        r'[\d]{1,2}/[\d]{1,2}/[\d]{4}', message="Invalid Date. Date should be in dd/mm/yyyy format."))
    # the logged in user owns
    owner_id = HiddenField()
    category = SelectField('Device Category', [InputRequired()],
                         choices=[('', ''), ('Phone', 'Phone'),
                                  ('Tablet', 'Tablet'),
                                  ('Laptop', 'Laptop'),
                                  ('Other', 'Other')])
    # updated - date - handled in the route function
    updated = HiddenField()
    submit = SubmitField('Add/Update Device')
    
