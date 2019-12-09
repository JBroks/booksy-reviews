from flask_testing import TestCase
from flask import url_for, request
from flask_login import current_user
from app import app, mongo
from user import User

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
        
    def test_index_loads(self):
        '''Ensure index page loads correctly.'''
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('index.html')
     
    def test_register_loads(self):
        '''Without login. 
        Ensure register page loads correctly.'''
        response = self.client.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('register.html')
     
    def test_login_loads(self):
        '''Without login.
        Ensure login page loads correctly.'''
        response = self.client.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('login.html')
        
    def test_logout_loads(self):
        '''Without login.
        Ensure logout page loads correctly.'''
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('login.html')
        
    def test_profile_loads(self):
        '''Without login'''
        response = self.client.get('/user/<username>', follow_redirects=True)
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
        
if __name__ == '__main__':
    unittest.main()