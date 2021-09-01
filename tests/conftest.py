from app.models import Users, Devices
from app.models import db
import testing.postgresql
import pytest
import sqlalchemy
from app import create_app
from app.views.views import logged_in


@pytest.fixture(scope='module')
def new_user():
    user = Users(1029384756, 'testUser', 'TDDIsAwesome',
                 'FamilyMember', 'Test', 'User')
    return user


@pytest.fixture(scope='module')
def new_device():
    device = Devices(1029384756, 'testDeviceName', 'testDevice', '11111111', 'testDeviceModel',
                     'A1:B2:C3:D4:F6', 'Active', '08/22/2021', 'testUser', 'test', 'Just a test device.')
    return device


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()
    # Insert user data
    user1 = Users(uid='123456789', username='user1', password='password1',
                  usertype='FamilyMember', first_name='User1Fname', last_name='User1Lname')
    user2 = Users(uid='987654321', username='user2', password='password2',
                  usertype='FamilyMember', first_name='User2Fname', last_name='User2Lname')
    db.session.add(user1)
    db.session.add(user2)
    # Commit the changes for the users
    db.session.commit()
    yield db
    db.drop_all()


@pytest.fixture(scope="session")
def postgres():
    """
    Starts a postgres instance inside a temp directory
    and closes it after tests are completed.
    """
    with testing.postgresql.Postgresql() as postgresql:
        yield postgresql

# create temporary postgres instance for testing


@pytest.fixture(scope="session")
def client(postgres):
    config_dict = {
        "SQLALCHEMY_DATABASE_URI": postgres.url(),
        "DEBUG": True,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        "TESTING": True,
    }
    app = create_app(config_dict)
    app.app_context().push()
    app.secret_key = 'test_secret_key'
    db.create_all()
    client = app.test_client()
    yield client


@pytest.fixture(scope='function')
def logged_in_user(client):
    client.post('/login',
                data=dict(username='user1', password='password1'),
                follow_redirects=True)
    # logged_in = True
    yield
