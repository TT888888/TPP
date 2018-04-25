from flask_restful import Api, Resource, fields, marshal_with, reqparse, marshal
from flask.ext import restful
import json
from flask import Blueprint,redirect,request

from flask import render_template


from App.models import Person, Letter, City

from App.ext import db

import os
from flask import url_for

# 用来生成json


APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC_TXT = os.path.join(APP_ROOT, '') #设置一个专门的类似全局变量的东西

blue = Blueprint('blue',__name__)

api = restful.Api(blue)
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


# 首页
@blue.route('/index/')
def indexs():
    return render_template('index.html')


# 向表里插数据
@blue.route('/shuju1/')
def shuju():
    with open(os.path.join(APP_STATIC_TXT, './area.json')) as datas:
        json_dict = json.load(datas)
        returnValue = json_dict.get("returnValue")
        # print(returnValue)
        letters = returnValue.keys()
        # print(letters)

        num = 0
        for let in letters:
            # le = Letter()
            # le.letter=let
            # db.session.add(le)
            # db.session.commit()

            letter_cities = returnValue.get(let)

            # print(letter_cities)
            num+=1
            # print(num)

            for letter_city in letter_cities:

                # cit=City()
                #
                # cit.letter=num
                # cit.id=letter_city.get('id')
                # cit.pinYin=letter_city.get("pinYin")
                # cit.regionName= letter_city.get("regionName")
                # cit.cityCode=letter_city.get("cityCode")
                #
                # db.session.add(cit)
                # db.session.commit()

                # print(letter_city["regionName"])
                # print(letter_city["id"])
                # print(letter_city["cityCode"])
                # print(letter_city["pinYin"])
                print("")

    return 'su'




# 生成json

city_fields = {
    "id": fields.Integer,
    "regionName": fields.String,
    "pinYin": fields.String,
    "cityCode": fields.Integer
}


letter_fields = {
    "A": fields.List(fields.Nested(city_fields)),
}


result_fields = {
    "returnCode": fields.String,
    "returnValue": fields.Nested(letter_fields)
}



class CityResource(Resource):
    @marshal_with(result_fields)
    def get(self):

        returnValue = {}

        letters = Letter.query.all()

        for letter in letters:

            cities = City.query.filter_by(letter=letter.id)

            # print(cities)

            for city in cities:
                print("123213")
                print(city.regionName)

            returnValue[letter.letter] = cities

        return {"returnCode": "0", "returnValue": returnValue}


api.add_resource(CityResource,'/c/')








