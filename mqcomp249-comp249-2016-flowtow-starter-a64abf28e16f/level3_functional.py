'''
Created on Mar 3, 2014

@author: steve
'''
import unittest
import webtest
from urlparse import urlparse

import main
import users
from database import COMP249Db


class Level3FunctionalTests(unittest.TestCase):

    def setUp(self):
        self.app = webtest.TestApp(main.application)
        self.db = COMP249Db()
        self.db.create_tables()
        self.db.sample_data()
        self.users = self.db.users


    def tearDown(self):
        pass

    def doLogin(self, email, password):
        """Perform a login,
         returns the response to the login request"""

        response = self.app.get('/')

        loginform = response.forms['loginform']

        loginform['nick'] = email
        loginform['password'] = password

        return loginform.submit()


    def testLoginForms(self):
        """As a visitor to the site, when I load the home page,
        I see a form with entry boxes for email and password and a button labelled Login."""

        (password, nick, avatar) = self.users[0]

        response = self.app.get('/')

        # there is a form with the id 'loginform'
        loginform = response.forms['loginform']
        self.assertIsNotNone(loginform, "no form with id loginform in the page")

        # login form action should be /login
        self.assertEqual('/login', loginform.action, "login form action should be '/login'")

        # the form has an email field
        self.assertIn('nick', loginform.fields)
        # and a password field
        self.assertIn('password', loginform.fields)



    def testLogin(self):
        """As a registered user, when I enter my user nickname (eg. Bobalooba) and password (bob)
        into the login form and click on the Login button, the response is a redirect
        to the main application page (/).

        The response generated by the successful login action is a redirect (303 See Other) response that redirects the user to the home page.
        The redirect response also includes a cookie with the name sessionid that contains some kind of random string.
        """

        (password, nick, avatar) = self.users[0]

        # As a registered user, when I enter my nick (Bobalooba) and password
        # (bob) into the login form and click on the Login button,

        response = self.doLogin(nick, password)

        # response should be a redirect to the main page
        self.assertIn(response.status, ['303 See Other', '302 Found'])
        (_, _, path, _, _, _) = urlparse(response.headers['Location'])
        self.assertEqual('/', path)

        # The response also includes a cookie with the name
        # sessionid that contains some kind of random string.

        self.assertIn(users.COOKIE_NAME, self.app.cookies)
        sessionid = self.app.cookies[users.COOKIE_NAME]

    def testLoginError(self):
        """As a registered user, when I enter my email address but get my
        password wrong and click on the Login button, the page I get in
        response contains a message "Login Failed, please try again".
        The page also includes another login form."""


        (password, nick, avatar) = self.users[0]

        # try an invalid password
        response = self.doLogin(nick, 'not the password')

        # should see a page returned with the word Error somewhere
        self.assertEqual('200 OK', response.status)
        self.assertIn("Failed", response)

        # Should not have a cookie
        self.assertNotIn(users.COOKIE_NAME, self.app.cookies)


    def testLoginPagesLogoutForm(self):
        """As a registered user, once I have logged in,
         every page that I request contains my name and the logout form."""

        (password, nick, avatar) = self.users[0]

        response1 = self.doLogin(nick, password)
        response2 = self.app.get('/')

        # no login form
        self.assertNotIn('loginform', response2.forms)

        # but a logout form
        self.assertIn('logoutform', response2.forms)
        logoutform = response2.forms['logoutform']
        self.assertEqual('/logout', logoutform.action)

        # and the message "Logged in as XXX"
        self.assertIn("Logged in as %s" % nick, response2)

    def testLogoutForm(self):
        """As a registered user, once I have logged in, if I click on the Logout
        button in a page, the page that I get in response is the site home
        page which now doesn't have my name and again shows the login form."""

        (password, nick, avatar) = self.users[0]

        response1 = self.doLogin(nick, password)
        response2 = self.app.get('/')

        # and a logout form
        self.assertIn('logoutform', response2.forms)
        logoutform = response2.forms['logoutform']

        response3 = logoutform.submit()
        # response should be a redirect
        self.assertIn(response3.status, ['303 See Other', '302 Found'])
        (_, _, path, _, _, _) = urlparse(response3.headers['Location'])
        self.assertEqual('/', path)


        response4 = self.app.get('/')
        # should see login form again
        loginform = response4.forms['loginform']
        self.assertIsNotNone(loginform, "no form with id loginform in the page")



    def testMyImages(self):
        """As a registered user, once I have logged in, on the home
        page I see a new link called "My Images". When I click on this
        link the page I get in response contains all of the images that
        I have uploaded listed in order of date (newest first). Each
        image is displayed as on the home page with my name, the date
        and a list of comments. Each image also has a comment form."""

        (password, nick, avatar) = self.users[0]

        self.doLogin(nick, password)
        response = self.app.get('/')

        # expect to see link to my images
        links = response.html.find_all('a', string='My Images')  # breaks in BS 4.3, need text=
        self.assertEqual(len(links), 1, "can't find link to My Images in page")
        imagelink = links[0]

        # follow the link
        response = self.app.get(imagelink['href'])

        # on the page returned I expect to see all my images

        flowtows = response.html.find_all(class_='flowtow')

        # each contains the username and an image
        for div in flowtows:

            # our nick  should be mentioned
            self.assertIn(nick, div.text)

            # look for just one image
            img = div.find_all('img')
            self.assertEqual(1, len(img))

            # check for a comment form
            self.assertGreater(len(div.find_all('form')), 0)

            # can we actually get the image
            # find the URL
            url = img[0]['src']
            # try requesting it and test the content-type header returned
            resp = self.app.get(url)
            self.assertEqual('image/jpeg', resp.content_type)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(warnings='ignore')
