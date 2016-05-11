# -*- coding: utf-8 -*-
"""
@author: Zhiyu Shen
"""

import bottle
import os
import interface

#if on Windows
UPLOAD_DIR = os.path.join(os.path.dirname(__file__), 'static', 'images').replace('\\','/')

def uploadImage(db, userNick):
    """
    文件上传处理模块
    :param db: 数据库对象
    :param userNick: 用户名
    :return: None
    """
    newfile = bottle.request.files.get("imagefile")
    # save uploaded image to UPLOAD_DIR
    savePath = os.path.join(UPLOAD_DIR, newfile.filename)
    newfile.save(savePath)

    # update database table "images"
    interface.add_image(db=db, filename=newfile.filename, usernick=userNick)