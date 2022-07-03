"""
This file contains utility functions needed for the application
to run successfully.
"""
from uuid import uuid4
import hashlib
from app.models import db, Users

# Custom Exceptions


class WrongSignIn(Exception):
    """Raised when the sign in form is blank but sign-in is pressed"""

    pass


def get_all(table):
    """
    Queries an entire table in the database.

    Args:
        table (Class): Database table to query.

    Returns:
        data: Query result.
    """
    data = table.query.all()
    return data


def add_instance(table, **kwargs):
    """
    Adds items into a specified table in the database.

    Args:
        table (Class): Database table to insert data into.
        **kwargs: Data to insert into table

    Returns:
        None
    """
    instance = table(**kwargs)
    db.session.add(instance)
    commit_changes()


def delete_instance(table, id):
    """
    Deletes an item from a specified table (mainly Devices table).

    Args:
        table (Class): Database table to delete from.
        id (int): ID of the item in the table

    Returns:
        item.name : Name of the deleted item.
    """
    item = table.query.filter(table.id == id).first()
    db.session.delete(item)
    commit_changes()
    return item.name


def edit_instance(table, id, **kwargs):
    """
    Edits an item in a specified table (mainly Devices table).

    Args:
        table (Class): Database table to apply edit to.
        id (int): ID of the item in the table
        **kwargs: Data to edit in the table

    Returns:
        [instance.id, instance.name] (list) : Name and id of the edited item.
    """
    instance = table.query.filter(table.id == id).first()
    for attr, new_value in kwargs.items():
        setattr(instance, attr, new_value)
    commit_changes()
    return [instance.id, instance.name]


def commit_changes():
    """
    Commit changes to db.

    Args:
        None

    Returns:
        None
    """
    db.session.commit()


def generate_id():
    """
    Generate a random id to be used in the db.

    Args:
        None

    Returns:
        id (int): Random id
    """
    random_id = str(uuid4().int >> 64)
    id = int(random_id[:5])
    return id


def hash_password(password):
    """
    Generate an md5 hash of a given text password.

    Args:
        password (str): Password to be hashed.

    Returns:
        hashed_password (str): md5 hashed password.
    """
    hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
    return hashed_password


def validate_login(username, password):
    """
    Validate whether a user is registered in the db.

    Args:
        username (str): User's username.
        password (str): User's password.

    Returns:
        logged_in (bool): True if user is registered in db.
                          False otherwise.
    """
    user = Users.query.filter_by(username=username).first()
    user_pass = user.password
    hashed_pass = hash_password(password)
    # check if the user actually exists
    # take the hashed user-entered password and compare it to the
    # hashed password in the database
    if not user or not user_pass == hashed_pass:
        logged_in = False
    else:
        logged_in = True
    return logged_in
