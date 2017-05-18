from flask import Blueprint

business_controller = Blueprint('business_controller', __name__)

@business_controller.route('', methods=['POST'])
def create():
    return "Success"