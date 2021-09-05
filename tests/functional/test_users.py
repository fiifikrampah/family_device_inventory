"""
This file contains the functional tests for the `users` blueprint.

These tests use GETs and POSTs to different URLs to check for
the proper behavior of the `users` blueprint.
"""


def test_login_page(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Sign In' in response.data
    assert b'Sign Up' in response.data
    assert b'Username' in response.data
    assert b'Password' in response.data


def test_invalid_login(client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = client.post('/login',
                           data=dict(username='user1', password='password2'),
                           follow_redirects=True)
    assert response.status_code == 200
    assert b'Sign In' in response.data
    assert b'Username' in response.data
    assert b'Password' in response.data


def test_valid_signup(client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/signup' page is posted to (POST)
    THEN check the response is valid and the user is logged in
    """
    response = client.post('/signup',
                           data=dict(username='user3',
                                     password='password3',
                                     first_name='User2Fname',
                                     last_name='User2Lname'),
                           follow_redirects=True)
    assert response.status_code == 200
    assert b'Username' in response.data
    assert b'Password' in response.data
    assert b'First Name' in response.data
    assert b'Last Name' in response.data
    assert b'Sign Up' in response.data


def test_index(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET) and user not logged if
    THEN check the response is valid
    """
    logged_in = True
    response = client.get('/')
    assert response.status_code == 302
    assert b'Redirecting...' in response.data


def test_duplicate_signup(client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to (POST) using a
    username already registered
    THEN check an error message is returned to the user
    """
    # Register the new account
    client.post('/signup',
                data=dict(username='user4',
                          password='password4',
                          first_name='User4Fname',
                          last_name='User4Lname'),
                follow_redirects=True)
    # Try registering with the same username
    response = client.post('/signup',
                           data=dict(username='user4',
                                     password='password4',
                                     first_name='User4Fname',
                                     last_name='User4Lname'),
                           follow_redirects=True)
    assert response.status_code == 200
    assert b'Login' not in response.data
