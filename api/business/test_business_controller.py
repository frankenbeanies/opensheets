import json
import unittest

from flask import Flask 

from business_controller import business_controller

app = Flask(__name__)

app.register_blueprint(business_controller, url_prefix="/")

class TestBusinessController(unittest.TestCase):
    def setUp(self): 
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_create_empty_returns_400(self):
        d = json.dumps({})
        response = self.app.post("/", data = d, content_type="application/json")

        self.assertEqual(response.status_code, 400)

    def test_create_invalid_returns_400(self):
        d = json.dumps({
            "name": "ABCIndustries",
            "email": "example@domain.com",
            "email_confirmation": "eample@domain.com",
            "password": "Password1",
            "password_confirmation": "Password1"
        })
        response = self.app.post("/", data = d, content_type="application/json")

        self.assertEqual(response.status_code, 400)

    def test_create_valid_returns_200(self):
        d = json.dumps({
            "name": "ABCIndustries",
            "email": "example@domain.com",
            "email_confirmation": "example@domain.com",
            "password": "Password1",
            "password_confirmation": "Password1"
        })
        response = self.app.post("/", data = d, content_type="application/json")

        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()