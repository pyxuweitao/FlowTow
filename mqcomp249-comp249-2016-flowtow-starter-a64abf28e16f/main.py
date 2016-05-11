# -*- coding: utf-8 -*-
'''
@author:ZhiyuShen
'''

from bottle import Bottle, template, debug, static_file, request, redirect
import interface
import users
import uploads
from database import COMP249Db

COOKIE_NAME = 'sessionid'

application = Bottle()


@application.route('/')
def index():
    """
    首页
    :return: 页面渲染元素字典
    """
    imagesNumber = 3
    flowTowDataBase = COMP249Db()
    userNick = users.session_user(db=flowTowDataBase)
    imagesList = interface.list_images(db=flowTowDataBase, n=imagesNumber)
    renderDict = {"title": "FlowTow!",
                  "homeActive": True,
                  "aboutActive": False,
                  "imagesList": imagesList,
                  "imagesNumber": imagesNumber,
                  "userNick": userNick,
                  "myActive": False}
    return template('index', renderDict)


@application.route('/about')
def about():
    """
    About页面
    :return:模板渲染网页标题等
    """
    flowTowDataBase = COMP249Db()
    userNick = users.session_user(db=flowTowDataBase)
    renderDict = {"title": "FlowTow!",
                  "homeActive": False,
                  "aboutActive": True,
                  "userNick": userNick,
                  "myActive": False}
    return template('about', renderDict)


@application.route('/my')
def my():
    """
    My Images页面
    :return:模板渲染网页标题等
    """
    flowTowDataBase = COMP249Db()
    userNick = users.session_user(db=flowTowDataBase)
    if userNick:
        # 此处的n不起作用，因为指定了用户名
        imagesList = interface.list_images(db=flowTowDataBase, n=0, usernick=userNick)
        renderDict = {"title": "FlowTow!",
                      "homeActive": False,
                      "aboutActive": False,
                      "imagesList": imagesList,
                      "imagesNumber": len(imagesList),
                      "userNick": userNick,
                      "myActive": True}
        return template('index', renderDict)
    else:
        return redirect('/')


@application.route('/upload', method='POST')
def upload():
    """
    文件上传页面
    :return: 返回页面渲染字典
    """
    flowTowDataBase = COMP249Db()
    userNick = users.session_user(db=flowTowDataBase)
    if userNick:
        uploads.uploadImage(db=flowTowDataBase, userNick=userNick)
        return redirect('/my')
    else:
        return redirect('/')


@application.route('/like', method='POST')
def like():
    """
    处理喜欢图片的请求
    :return: 重定向至指定页面
    """
    filename = request.POST.get('filename')
    flowTowDataBase = COMP249Db()
    userNick = users.session_user(db=flowTowDataBase)
    interface.add_like(db=flowTowDataBase, filename=filename, usernick=userNick)
    return redirect('/')


@application.route('/login', method='POST')
def login():
    """
    处理登录
    :return:
    """
    userNick = request.POST.get('nick')
    password = request.POST.get('password')
    flowTowDataBase = COMP249Db()
    if users.check_login(db=flowTowDataBase, usernick=userNick, password=password):
        if users.generate_session(db=flowTowDataBase, usernick=userNick):
            return redirect('/')
    renderDict = {"title": "Login Failed!",
                  "homeActive": False,
                  "aboutActive": True,
                  "userNick": None}
    return template("loginFailed", renderDict)


@application.route('/logout', method='POST')
def logout():
    """
    处理登出
    :return:重定向至首页
    """
    flowTowDataBase = COMP249Db()
    requestUser = users.session_user(flowTowDataBase)
    users.delete_session(db=flowTowDataBase, usernick=requestUser)
    return redirect('/')


@application.route('/static/:fileName#.*#')
def server_static(fileName):
    """
    静态文件serve的路由配置
    :param fileName:文件名
    :return:静态文件路径的配置信息
    """
    return static_file(fileName, root='./static')


if __name__ == '__main__':
    debug()
    application.run()
