import unittest
from django.test import Client
from django.test import TestCase


# Create your tests here.


class SimpleTest(unittest.TestCase):

    def testHomePage(self):
        c = Client()
        response = c.get('/home')
        self.assertEqual(response.status_code, 200)

    def testSignupPage(self):
        c = Client()
        response = c.get('/signup')
        self.assertEqual(response.status_code, 200)

    def testLoginView(self):
        c = Client()
        x = c.login(username='rpvirtuoso', password='admin@123')
        print("Was logintest successful?:" + str(x))

    def testSignupView(self):
        c = Client()
        response = c.post('/signup', {"username": "hritik", "password": "admin@123"})
        print("The Signup view status code is :" + str(response.status_code))

    def testChangePasswordView(self):
        c = Client()
        response = c.post('/change-password', )
