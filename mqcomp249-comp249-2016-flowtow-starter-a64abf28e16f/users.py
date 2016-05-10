'''
@author:
'''

import bottle
import uuid

# this variable MUST be used as the name for the cookie used by this application
COOKIE_NAME = 'sessionid'


def check_login(db, usernick, password):
    """returns True if password matches stored"""
    flowTowCursor = db.cursor()
    flowTowCursor.execute("SELECT password FROM users WHERE nick = ?", [usernick])
    passwordStored = flowTowCursor.fetchone()
    if passwordStored:
        return True if db.encode(password) == passwordStored[0] else False
    else:
        return False


def generate_session(db, usernick):
    """create a new session and add a cookie to the response object (bottle.response)
    user must be a valid user in the database, if not, return None
    There should only be one session per user at any time, if there
    is already a session active, use the existing sessionid in the cookie
    """
    flowTowCursor = db.cursor()
    flowTowCursor.execute("SELECT * FROM users WHERE nick = ?", [usernick])
    if flowTowCursor.fetchone():
        flowTowCursor.execute("SELECT sessionid FROM sessions WHERE  usernick = ?", [usernick])
        sessionStored = flowTowCursor.fetchone()
        if sessionStored:
            key = sessionStored[0]
        else:
            key = unicode(uuid.uuid4())
            flowTowCursor.execute("INSERT INTO sessions(sessionid, usernick) VALUES (?, ?)", [key, usernick])
            db.commit()
        bottle.response.set_cookie(COOKIE_NAME, key)
        return key
    else:
        return None


def delete_session(db, usernick):
    """remove all session table entries for this user"""
    flowTowCursor = db.cursor()
    flowTowCursor.execute("DELETE FROM sessions WHERE usernick = ?", [usernick])
    db.commit()


def session_user(db):
    """try to
    retrieve the user from the sessions table
    return usernick or None if no valid session is present"""
    cookie = bottle.request.get_cookie(COOKIE_NAME)
    flowTowCursor = db.cursor()
    flowTowCursor.execute("SELECT usernick FROM sessions WHERE sessionid = ?", [cookie])
    sessionStored = flowTowCursor.fetchone()
    return sessionStored[0] if sessionStored else None
