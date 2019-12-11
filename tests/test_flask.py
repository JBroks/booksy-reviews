from flask import Flask
from flask_testing import TestCase
from flask_login import current_user, LoginManager, login_user
from app import app, mongo
from werkzeug.security import generate_password_hash, check_password_hash
from user import User
from datetime import datetime

import unittest

class TestFlaskApp(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['MONGO_URI'] = 'mongodb:///:memory:'
        return app
    
    def setUp(self):
        self.client = app.test_client()
        pass

    def tearDown(self):
        pass
    
     # Test if pages load correctly - without login
    
    ''' Ensure that pages load correctly without user being 
        authenticated '''
        
    def test_index_loads(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('index.html')
     
    def test_register_loads(self):
        response = self.client.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('register.html')
     
    def test_login_loads(self):
        response = self.client.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('login.html')
        
    def test_logout_loads(self):
    
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('login.html')
    
    # Test fields on register form
    
    def test_too_short_username(self):
        """ Test if username provided by user is too short, error message is displayed """
        response = self.client.post('/register', data=dict( username='test',
            email='testing1@test.com',
            password='blablabla',
            password2='blablabla',
        ))
        data = response.data.decode('utf-8')
        assert 'Field must be between 5 and 25 characters long' in data
    
    def test_valid_email(self):
        """ Test if email address provided by user is invalid, error message is displayed """
        response = self.client.post('/register', data=dict( username='testing1',
            email='testing1aaaaaaa',
            password='blablabla',
            password2='blablabla',
        ))
        data = response.data.decode('utf-8')
        assert 'This is not a valid email address' in data
    
    def test_too_short_password(self):
        """ Test if password is too short, error message is displayed """
        response = self.client.post('/register', data=dict( username='testing1',
            email='testing1@test.com',
            password='bla',
            password2='bla',
        ))
        data = response.data.decode('utf-8')
        assert 'Field must be between 7 and 50 characters long' in data
        
    def test_repeat_password(self):
        """ Test if repeated password is incorrect error, message is displayed """
        response = self.client.post('/register', data=dict( username='testing1',
            email='testing1@test.com',
            password='blablabla',
            password2='aaaaaaaaaa',
        ))
        data = response.data.decode('utf-8')
        assert 'Field must be equal to password' in data
    
    # Test fields on login form
    
    def test_no_username(self):
        """ Test if no username is provided by user when attempting to login, error message is displayed """
        response = self.client.post('/login', data=dict( username='',
            password='blablabla'
        ))
        data = response.data.decode('utf-8')
        assert 'Please enter a valid username' in data
      
    def test_no_password(self):
        """ Test if no password is provided by user when attempting to login, error message is displayed """
        response = self.client.post('/login', data=dict( username='testing1',
            password=''
        ))
        data = response.data.decode('utf-8')
        assert 'Please enter your password' in data

    # Test password hashing
    
    def test_password_hashing(self):
        u = User(username='john')
        password_hash = generate_password_hash('bla')
        self.assertFalse(u.check_password(password_hash, 'aaa'))
        self.assertTrue(u.check_password(password_hash, 'bla'))
    
    # Test user login
    
    def test_user_login(self):
        
        login_manager = LoginManager()
        login_manager.init_app(app) 
        
        with app.test_request_context():
            
        # set up and log in user
            user = User(username='johnny')
            login_user(user)

        # test that user was logged in
            assert current_user.is_active
            assert current_user.is_authenticated
            assert current_user == user
     
if __name__ == '__main__':
    unittest.main()