from flask import Blueprint, request
from models import User
import json

api = Blueprint('api', __name__, template_folder='templates')

@api.route("/authenticate", methods=['POST'])
def authenticate():
	print request
	user = json.loads(request.data)
	print user
	q = User.query.filter_by(email=user["email"], password=user["password"]).first()
	print q
	if q:
		return json.dumps({"result":True})
	else:
		return json.dumps({"result":False})

@api.route("/create_user", methods=['POST'])
def create_user():
	user = json.loads(request.data)
	user = User(user["first_name"], user["last_name"], user["email"], user["password"])
	db.session.add(user)
	q = db.session.commit()
	if q:
		return json.dumps({"result":True})
	else:
		return json.dumps({"result":False})