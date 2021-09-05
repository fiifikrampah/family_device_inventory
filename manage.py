"""
This file sets up a Command line interface
that allows one to perform common functions with a command
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from app.models import db

# set up the app
app = create_app()

manager = Manager(app)
migrate = Migrate(app, db)

# add the python manage.py db init, db migrate, db upgrade commands
manager.add_command("db", MigrateCommand)


@manager.command
def runserver():
    """
    runserver function utilized for development config
    """
    app.run(debug=True, host="0.0.0.0", port=5000)


@manager.command
def runworker():
    """
    runworker function utilized for production config
    """
    app.run(debug=False)


@manager.command
def recreate_db():
    """
    recreate_db function to create a new db
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    manager.run()
