# encoding:utf-8

from . import main
from ..pjax import pjax


@main.route('/')
def index():
    """

    :return: 首页路由

    """

    return pjax('/index/index.html')
