from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField, TextAreaField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange

from app import create_app
from db.models import db, Users, Devices
from db.database import generate_id, add_instance, delete_instance, edit_instance
app = create_app()
Bootstrap(app)


class AddDevice(FlaskForm):
    # id used only by update/edit
    id_field = HiddenField()
    device_name = StringField('Name')
    device_type = StringField('Type')
    device_serial = StringField('Serial')
    device_model = StringField('Model')
    device_mac = StringField('MAC Address')
    status = SelectField('Device Status', [InputRequired()],
                         choices=[('', ''), ('Active', 'Active'),
                                  ('Inactive', 'Inactive'),
                                  ('Abandoned', 'Abandoned'),
                                  ('Lost', 'Lost')])
    purchase_date = StringField('Purchase Date', [InputRequired()])
    owner = StringField('Owner Username')
    category = SelectField('Device Category', [InputRequired()],
                           choices=[('', ''), ('Phone', 'Phone'),
                                    ('Tablet', 'Tablet'),
                                    ('Laptop', 'Laptop'),
                                    ('Desktop', 'Desktop'),
                                    ('Other', 'Other')])
    notes = TextAreaField('Notes')
    submit = SubmitField('Add/Update Device')


class DeleteForm(FlaskForm):
    id_field = HiddenField()
    purpose = HiddenField()
    submit = SubmitField('Delete This Device')

# routes
# add a new device to the database


@app.route('/')
def index():
    # get a list of unique values in the category column
    device_categories = Devices.query.with_entities(
        Devices.category).distinct()
    return render_template('index.html', device_categories=device_categories)


@app.route('/inventory/<category>')
def inventory(category):
    tech = Devices.query.filter_by(
        category=category).order_by(Devices.name).all()
    return render_template('device_list.html', tech=tech, category=category)


@app.route('/add_device', methods=['GET', 'POST'])
def add_device():
    form1 = AddDevice()
    if form1.validate_on_submit():
        add_instance(Devices,
                     id=generate_id(),
                     name=request.form['device_name'],
                     device_type=request.form['device_type'],
                     serial=request.form['device_serial'],
                     model=request.form['device_model'],
                     mac_address=request.form['device_mac'],
                     status=request.form['status'],
                     purchase_date=request.form['purchase_date'],
                     owner_username=request.form['owner'],
                     category=request.form['category'],
                     notes=request.form['notes']
                     )
        # create a message to send to the template
        message = f"The data for device {request.form['device_name']} has been submitted."
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

# select a device to edit or delete


@app.route('/select_device/<letters>')
def select_device(letters):
    # Alphabetical sort of devices by name, chunked by letters between _ and _
    a, b = list(letters)
    tech = Devices.query.filter(
        Devices.name.between(a, b)).order_by(Devices.name).all()
    return render_template('select_device.html', tech=tech)


# edit or delete a device
@app.route('/edit_or_delete', methods=['POST'])
def edit_or_delete():
    id = request.form['id']
    choice = request.form['choice']
    device = Devices.query.filter(Devices.id == id).first()
    form1 = AddDevice()
    form2 = DeleteForm()
    return render_template('edit_or_delete.html', device=device, form1=form1, form2=form2, choice=choice)


# result of delete - this function deletes the record
@app.route('/delete_result', methods=['POST'])
def delete_result():
    id = request.form['id_field']
    purpose = request.form['purpose']
    if purpose == 'delete':
        deleted_device = delete_instance(Devices, id)
        db.session.commit()
        message = f"The device {deleted_device} has been deleted from the database."
        return render_template('result.html', message=message)
    else:
        # this calls an error handler
        abort(405)

# result of edit - this function updates the record


@app.route('/edit_result', methods=['POST'])
def edit_result():
    id = request.form['id_field']
    device = edit_instance(Devices, id,
                           name=request.form['device_name'],
                           device_type=request.form['device_type'],
                           serial=request.form['device_serial'],
                           model=request.form['device_model'],
                           mac_address=request.form['device_mac'],
                           status=request.form['status'],
                           purchase_date=request.form['purchase_date'],
                           owner_username=request.form['owner'],
                           category=request.form['category'],
                           notes=request.form['notes']
                           )
    form1 = AddDevice()
    if form1.validate_on_submit():
        # create a message to send to the template
        message = f"The data for device {device[1]} has been updated."
        return render_template('result.html', message=message)
    else:
        # show validaton errors
        device[0] = id

        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('edit_or_delete.html', form1=form1, device=device, choice='edit')

# error routes


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', pagetitle="404 Error - Page Not Found", pageheading="Page not found (Error 404)", error=e), 404


@app.errorhandler(405)
def form_not_posted(e):
    return render_template('error.html', pagetitle="405 Error - Form Not Submitted", pageheading="The form was not submitted (Error 405)", error=e), 405


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', pagetitle="500 Error - Internal Server Error", pageheading="Internal server error (500)", error=e), 500


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
