from app.models import Users, Devices


def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the uid, username, hashed_password, usertype, first name and last name are defined correctly
    """
    assert new_user.uid == 1029384756
    assert new_user.username == 'testUser'
    assert new_user.password != 'TDDIsAwesome'
    assert new_user.usertype == 'FamilyMember'
    assert new_user.first_name == 'Test'
    assert new_user.last_name == 'User'


def test_new_device(new_device):
    """
    GIVEN a Device model
    WHEN a new Device is created
    THEN check the id, name, device_type, serial, model, MAC address, status, purchase date, owner, category and notes are defined correctly
    """
    assert new_device.id == 1029384756
    assert new_device.name == 'testDeviceName'
    assert new_device.device_type == 'testDevice'
    assert new_device.serial == '11111111'
    assert new_device.model == 'testDeviceModel'
    assert new_device.mac_address == 'A1:B2:C3:D4:F6'
    assert new_device.status == 'Active'
    assert new_device.purchase_date == '08/22/2021'
    assert new_device.owner_username == 'testUser'
    assert new_device.category == 'test'
    assert new_device.notes == 'Just a test device.'
