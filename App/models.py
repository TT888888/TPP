from App.ext import db


class Person(db.Model):

    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    p_name=db.Column(db.String(16))
    # 整数，默认值为1
    p_age=db.Column(db.Integer,default=1)


class Letter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    letter = db.Column(db.String(2))


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    regionName = db.Column(db.String(16))
    cityCode = db.Column(db.Integer)
    pinYin = db.Column(db.String(128))
    letter = db.Column(db.Integer, db.ForeignKey(Letter.id))