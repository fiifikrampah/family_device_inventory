from db.models import db
from uuid import uuid4


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
