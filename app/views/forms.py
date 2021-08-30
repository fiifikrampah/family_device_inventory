from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, RadioField, HiddenField, StringField, IntegerField, FloatField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, Length, Regexp, NumberRange

class UserLogIn(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    sign_in = SubmitField('Sign In')
    sign_up = SubmitField('Sign Up')


class AddUser(FlaskForm):
    uid = HiddenField()
    username = StringField('Username', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])
    usertype = HiddenField()
    fname = StringField('First Name', [InputRequired()])
    lname = StringField('Last Name', [InputRequired()])
    submit = SubmitField('Sign Up')


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
