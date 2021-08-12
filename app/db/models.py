import flask_sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = flask_sqlalchemy.SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    usertype = db.Column(db.String(255), unique=False, nullable=False)
    phone_number = db.Column(db.Unicode(255), unique=False, nullable=True)
    first_name = db.Column(db.String(255), unique=False, nullable=False)
    last_name = db.Column(db.String(255), unique=False, nullable=False)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Devices(db.Model):
    __tablename__ = "devices"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    device_type = db.Column(db.String(255), nullable=False)
    serial = db.Column(db.String(255), nullable=False)
    model = db.Column(db.String(255), nullable=False)
    mac_address = db.Column(db.String(255), nullable=True)
    status = db.Column(
        db.Enum("Active", "Inactive", "Abandoned", "Lost", name='status_types'), nullable=False)
    purchase_date = db.Column(db.DateTime, nullable=False)
    owner_username = db.Column(db.String(255), db.ForeignKey('users.username'))
    owner = db.relationship("Users", backref="devices")
    category = db.Column(
        db.Enum("Phone", "Tablet", "Laptop", "Desktop", "Other", name='category_types'), nullable=False)
    notes = db.Column(db.Text())

    def __repr__(self):
        return '<Device {}>'.format(self.name)

    def __init__(self, id, name, device_type, serial, model, mac_address, status, purchase_date, owner_username, category, notes):
        self.id = id
        self.name = name
        self.device_type = device_type
        self.serial = serial
        self.model = model
        self.mac_address = mac_address
        self.status = status
        self.purchase_date = purchase_date
        self.owner_username = owner_username
        self.category = category
        self.notes = notes
