import json

from flask import Blueprint, request

from models.requests import CreateBusinessRequest

business_controller = Blueprint('business_controller', __name__)

@business_controller.route('', methods=['POST'])
def create():
    req = CreateBusinessRequest(request.get_json())
    errors = req.validate()
    if(errors != []):
        return json.dumps(errors), 400
    return "Success", 200