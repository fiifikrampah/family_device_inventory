from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField, TextAreaField
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
    owner = StringField('Username')
    category = SelectField('Device Category', [InputRequired()],
                           choices=[('', ''), ('Phone', 'Phone'),
                                    ('Tablet', 'Tablet'),
                                    ('Laptop', 'Laptop'),
                                    ('Desktop', 'Desktop'),
                                    ('Other', 'Other')])
    notes = TextAreaField('Notes')
    submit = SubmitField('Add/Update Device')

# routes
# add a new device to the database


@app.route('/add_device', methods=['GET', 'POST'])
def add_device():
    form1 = AddDevice()
    if form1.validate_on_submit():
        name = request.form['device_name']
        device_type = request.form['device_type']
        serial = request.form['device_serial']
        model = request.form['device_model']
        mac_address = request.form['device_mac']
        status = request.form['status']
        purchase_date = request.form['purchase_date']
        owner = request.form['owner']
        category = request.form['category']
        notes = request.form['notes']

        # Add the data into the Devices table
        record = Devices(name, device_type, serial, model, mac_address,
                         status, purchase_date, owner, category, notes)
        db.session.add(record)
        db.session.commit()
        # create a message to send to the template
        message = f"The data for device {name} has been submitted."
        return render_template('add_device.html', message=message)
    else:
        # show validaton errors
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_device.html', form1=form1)
