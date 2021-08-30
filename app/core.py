from app.models import db, Users
from uuid import uuid4
import hashlib

# Custom Exceptions


class WrongSignIn(Exception):
    """Raised when the sign in form is blank but sign-in is pressed"""
    pass


def get_all(table):
    data = table.query.all()
    return data


def add_instance(table, **kwargs):
    instance = table(**kwargs)
    db.session.add(instance)
    commit_changes()


def delete_instance(table, id):
    item = table.query.filter(table.id == id).first()
    db.session.delete(item)
    commit_changes()
    return item.name


def edit_instance(table, id, **kwargs):
    instance = table.query.filter(table.id == id).first()
    for attr, new_value in kwargs.items():
        setattr(instance, attr, new_value)
    commit_changes()
    return [instance.id, instance.name]


def commit_changes():
    db.session.commit()


def generate_id():
    random_id = str(uuid4().int >> 64)
    id = int(random_id[:5])
    return id


def hash_password(password):
    """Create hashed password."""
    hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
    return hashed_password


def validate_login(username, password):
    user = Users.query.filter_by(username=username).first()
    user_pass = user.password
    hashed_pass = hash_password(password)
    # check if the user actually exists
    # take the hashed user-entered password and compare it to the hashed password in the database
    if not user or not user_pass == hashed_pass:
        logged_in = False
    else:
        logged_in = True
    return logged_in
