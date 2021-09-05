"""
This file contains the functional tests for the `devices` blueprint.

These tests use GETs and POSTs to different URLs to check for the
proper behavior of the `devices` blueprint.
"""


def test_inventory(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/inventory/<category>' page is requested (GET)
    with a sample category
    THEN check the response is valid
    """
    response = client.get('/inventory/Phone')
    assert response.status_code == 200


def test_add_device(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/add_device' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/add_device')
    assert response.status_code == 200
    assert b'Name' in response.data
    assert b'Type' in response.data
    assert b'Serial' in response.data
    assert b'Model' in response.data
    assert b'MAC Address' in response.data
    assert b'Device Status' in response.data
    assert b'Purchase Date' in response.data
    assert b'Owner Username' in response.data
    assert b'Device Category' in response.data
    assert b'Notes' in response.data
    assert b'Add/Update Device' in response.data


def test_select_device(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/select_device' page is requested (GET)
    with a sample letter range
    THEN check the response is valid
    """
    response = client.get('/select_device/AF')
    assert response.status_code == 200

# TODO:
# def test_edit_or_delete(client):
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/select_device' page is requested (GET)
#     THEN check the response is valid
#     """

# def test_delete_result(client):
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/select_device' page is requested (GET)
#     THEN check the response is valid
#     """

# def test_edit_result(client):
#     """
#     GIVEN a Flask application configured for testing
#     WHEN the '/edit_result' page is posted to (POST)
#     THEN check the response is valid
#     """
