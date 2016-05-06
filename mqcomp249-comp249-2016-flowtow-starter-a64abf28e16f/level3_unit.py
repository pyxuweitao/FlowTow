'''
Created on Mar 26, 2012

@author: steve
'''

import unittest

from database import COMP249Db
from http.cookies import SimpleCookie
from bottle import request, response

# import the module to be tested
import users
import interface 

class Test(unittest.TestCase):

    
    def setUp(self):
        # open an in-memory database for testing
        self.db = COMP249Db(':memory:')
        self.db.create_tables()
        self.db.sample_data()
        self.users = self.db.users


    def test_list_images_user(self):
        """Test that list_images with the extra usernick argument
         returns the right list of images for a user"""
        
        for password, nick, avatar in self.users:

            # get the three most recent image entries
            image_list = interface.list_images(self.db, 3, nick)
        
            # image_list should be a list of dictionaries
            for img in image_list:
                self.assertEqual(dict, type(img), "returned element not a dictionary")
        

            # check that the images are in the right order
            dates = [img['timestamp'] for img in image_list]
            sorteddates = [img['timestamp'] for img in image_list]
            sorteddates.sort(reverse=True)
            self.assertListEqual(dates, sorteddates)

            # and the owners, dates and like count are correct
            for img in image_list:
                for refimage in self.db.images:
                    if img['filename'] == refimage[0]:
                        self.assertEqual(refimage[1], img['timestamp'])
                        self.assertEqual(refimage[2], img['user'])
                        self.assertEqual(len(refimage[3])+1, img['likes'])
        

    def test_check_login(self):

        for password, nick, avatar in self.users:
            # try the correct password
            self.assertTrue(users.check_login(self.db, nick, password), "Password check failed for user %s" % nick)

            # and now incorrect
            self.assertFalse(users.check_login(self.db, nick, "badpassword"), "Bad Password check failed for user %s" % nick)

        # check for an unknown email
        self.assertFalse(users.check_login(self.db, "whoisthis", "badpassword"), "Bad Password check failed for unknown user")

    def get_cookie_value(self, cookiename):
        """Get the value of a cookie from the bottle response headers"""

        headers = response.headerlist
        for h,v in headers:
            if h == 'Set-Cookie':
                cookie = SimpleCookie(v)
                if cookiename in cookie:
                    return cookie[cookiename].value

        return None

    def test_generate_session(self):
        """The generate_session procedure makes a new session cookie
        to be returned to the client
        If there is already a session active for this user, return the
        same session key in the cookie"""

        # run tests for all test users
        for password, nick, avatar in self.users:

            users.generate_session(self.db, nick)
            # get the sessionid from the response cookie

            sessionid = self.get_cookie_value(users.COOKIE_NAME)

            self.assertFalse(sessionid is None)

            cursor = self.db.cursor()
            cursor.execute('select usernick from sessions where sessionid=?', (sessionid,))

            query_result = cursor.fetchone()
            if query_result is None:
                self.fail("No entry for session id %s in sessions table" % (sessionid,))

            self.assertEqual(nick, query_result[0])

            # now try to make a new session for one of the users

            users.generate_session(self.db, nick)

            sessionid2 = self.get_cookie_value(users.COOKIE_NAME)

            # sessionid should be the same as before

            self.assertEqual(sessionid, sessionid2)

        # try to generate a session for an invalid user

        sessionid3 = users.generate_session(self.db, "Unknown")
        self.assertEqual(sessionid3, None, "Invalid user should return None from generate_session")


    def test_delete_session(self):
        """The delete_session procedure should remove all sessions for
        a given user in the sessions table.
        Test relies on working generate_session"""

        # run tests for all test users
        for passwd, nick, avatar in self.users:
            users.generate_session(self.db, nick)

            # now remove the session
            users.delete_session(self.db, nick)

            # now check that the session is not present

            cursor = self.db.cursor()
            cursor.execute('select sessionid from sessions where usernick=?', (nick,))

            rows = cursor.fetchall()
            self.assertEqual(rows, [], "Expected no results for sessions query from deleted session, got %s" % (rows,))



    def test_session_user(self):
        """The session_user procedure finds the name of the logged in
        user from the session cookie if present

        Test relies on working generate_session
        """

        # first test with no cookie
        nick_from_cookie = users.session_user(self.db)
        self.assertEqual(nick_from_cookie, None, "Expected None in case with no cookie, got %s" % str(nick_from_cookie))

        request.cookies[users.COOKIE_NAME] = 'fake sessionid'
        nick_from_cookie = users.session_user(self.db)

        self.assertEqual(nick_from_cookie, None, "Expected None in case with invalid session id, got %s" % str(nick_from_cookie))

        # run tests for all test users
        for password, nick, avatar in self.users:

            users.generate_session(self.db, nick)

            sessionid = self.get_cookie_value(users.COOKIE_NAME)

            request.cookies[users.COOKIE_NAME] = sessionid

            nick_from_cookie = users.session_user(self.db)

            self.assertEqual(nick_from_cookie, nick)




if __name__ == "__main__":
    unittest.main()