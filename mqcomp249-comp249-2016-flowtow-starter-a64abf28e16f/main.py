# -*- coding: utf-8 -*-
'''
@author:ZhiyuShen
'''

from bottle import Bottle, template, debug, static_file, request, redirect
import interface
import users
from database import COMP249Db

COOKIE_NAME = 'sessionid'

application = Bottle()


@application.route('/')
def index():
    """
    首页
    :return: 首页标题
    """
    imagesNumber = 3
    flowTowDataBase = COMP249Db()
    imagesList = interface.list_images(db=flowTowDataBase, n=imagesNumber)
    renderDict = {"title": "FlowTow!",
                  "homeActive": True,
                  "aboutActive": False,
                  "imagesList": imagesList,
                  "imagesNumber": imagesNumber}
    return template('index', renderDict)


@application.route('/about')
def about():
    """
    About页面
    :return:模板渲染网页标题
    """
    renderDict = {"title": "FlowTow!",
                  "homeActive": False,
                  "aboutActive": True}
    return template('about', renderDict)


@application.route('/like', method='POST')
def like():
    filename = request.POST.get('filename')
    flowTowDataBase = COMP249Db()
    interface.add_like(db=flowTowDataBase, filename=filename)
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
