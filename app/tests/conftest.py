from app.db.models import Users, Devices
from app.app import create_app
import pytest
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
def test_client():
    flask_app = create_app('flask_test.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client