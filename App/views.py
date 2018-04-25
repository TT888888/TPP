
# 蓝图
from flask import Blueprint


from App.models import Person

from App.ext import db

blue = Blueprint('blue',__name__)


def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def index():
    return 'hello Index'


# # 创建表
# @blue.route('/createdb/')
# def create_db():
#     db.create_all()
#
#     return 'su'
#
#
# # 删除表
# @blue.route('/dropdb/')
# def drop_db():
#     db.drop_all()
#     return 'su'
#
#
#
#
# # 添加数据
# @blue.route('/addperson/')
# def add_person():
#     p = Person()
#
#     p.p_age=15
#     p.p_name="二狗"
#
#     # 存到数据库
#     db.session.add(p)
#     db.session.commit()
#     return 'su'