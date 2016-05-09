# -*- coding: utf-8 -*-
'''
@author:
'''
import database


def list_images(db, n, usernick=None):
    """Return a list of dictionaries for the first 'n' images in
    order of timestamp. Each dictionary will contain keys 'filename', 'timestamp', 'user' and 'likes'.
    The 'likes' value will be a count of the number of likes for this image as returned by count_likes.
    If usernick is given, then only images belonging to that user are returned."""
    flowTowCursor = db.cursor()
    if usernick:
        SQL = """SELECT filename, timestamp, usernick user,
                    (SELECT COUNT(*) FROM likes WHERE filename=images.filename) likes
                     FROM images WHERE images.usernick = ? ORDER BY timestamp DESC LIMIT ?"""
        flowTowCursor.execute(SQL, [usernick, n])
    else:
        SQL = """SELECT filename, timestamp, usernick user,
                    (SELECT COUNT(*) FROM likes WHERE filename=images.filename) likes
                 FROM images ORDER BY timestamp DESC LIMIT ?"""
        flowTowCursor.execute(SQL, [n])
    res = flowTowCursor.fetchall()
    columns = [column[0] for column in flowTowCursor.description]
    return [dict(zip(columns, row)) for row in res]


def add_image(db, filename, usernick):
    """Add this image to the database for the given user"""
    flowTowCursor = db.cursor()
    SQL = """INSERT INTO images(filename, timestamp, usernick) VALUES (?, datetime('now'), ?)"""
    flowTowCursor.execute(SQL, [filename, usernick])

def imageExist(db, filename):
    """
    判断图片是否已经存在在image表中
    :param db: 数据库对象
    :param filename: 文件相对于images文件夹的路径名
    :return: 如果存在返回True，否则返回False
    """
    flowTowCursor = db.cursor()
    flowTowCursor.execute("SELECT * FROM images WHERE filename = ?", [filename])
    return True if flowTowCursor.fetchall() else False

def userExist(db, usernick):
    """
    判断用户是否已经存在在user表中
    :param db: 数据库对象
    :param usernick: 用户名
    :return: 如果存在返回True，否则返回False
    """
    flowTowCursor = db.cursor()
    flowTowCursor.execute("SELECT * FROM users WHERE nick = ?", [usernick])
    return True if flowTowCursor.fetchall() else False

def add_like(db, filename, usernick=None):
    """Increment the like count for this image"""
    flowTowCursor = db.cursor()
    if imageExist(db=db, filename=filename):
        if usernick:
            if userExist(db=db, usernick=usernick):
                SQL = """INSERT INTO likes(filename, usernick) VALUES (?, ?)"""
                flowTowCursor.execute(SQL, [filename, usernick])
                db.commit()
        else:
            SQL = """INSERT INTO likes(filename) VALUES (?)"""
            flowTowCursor.execute(SQL, [filename])
            db.commit()

def count_likes(db, filename):
    """Count the number of likes for this filename"""
    flowTowCursor = db.cursor()
    flowTowCursor.execute("SELECT COUNT(*) FROM likes WHERE filename=?", [filename])
    return flowTowCursor.fetchone()[0]