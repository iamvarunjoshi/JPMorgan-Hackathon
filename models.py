from flask.ext.sqlalchemy import SQLAlchemy
from random import random
import requests
import json

db = SQLAlchemy()

user_identifier = db.Table('user_identifier',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('projects.id'))
)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(40))
    address = db.Column(db.String(120))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    phone = db.Column(db.String(20))
    interests = db.Column(db.String(120), default='')

    def __init__(self, first_name, last_name, email, password, address, phone, interests=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.address = address
        self.phone = phone

        if interests:
            self.interests = interests

        if "lasgow" not in address:
            address += ", Glasgow"

        r = requests.get(url="http://maps.googleapis.com/maps/api/geocode/json?address=" + address)
        data=json.loads(r.text)
        bounds = data["results"][0]["geometry"]["bounds"]
        self.lat = bounds["southwest"]["lat"] + random()*(bounds["northeast"]["lat"]-bounds["southwest"]["lat"])
        self.lng = bounds["southwest"]["lng"] + random()*(bounds["northeast"]["lng"]-bounds["southwest"]["lng"])

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.first_name, self.last_name, self.email, self.password)

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.Text)
    image = db.Column(db.Text, default='')
    address = db.Column(db.String(120))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    num_people = db.Column(db.Integer)
    date = db.Column(db.String(100), default='')

    users = db.relationship("User",secondary=user_identifier)

    def __init__(self, name, description, address, num_people, image=None, date=None):
        self.name = name
        self.description = description
        self.address = address
        self.num_people = num_people

        if "lasgow" not in address:
            address += ", Glasgow"

        r = requests.get(url="http://maps.googleapis.com/maps/api/geocode/json?address=" + address)
        data=json.loads(r.text)

        self.lat = data["results"][0]["geometry"]["location"]["lat"]
        self.lng = data["results"][0]["geometry"]["location"]["lng"]

        if image:
            self.image = image

        if date:
            self.date = date

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.name, self.description, self.address, self.num_people, self.image) 

class Issue(db.Model):
    __tablename__ = 'issues'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    kind = db.Column(db.String(80))
    image = db.Column(db.String(80),default='')
    date = db.Column(db.String(100),default='')

    def __init__(self, description, lat, lng, kind, image=None, date=None):
        self.description = description
        self.lat = float(lat)
        self.lng = float(lng)
        self.kind = kind
        if image:
            self.image = image
        if date:
            self.date = date