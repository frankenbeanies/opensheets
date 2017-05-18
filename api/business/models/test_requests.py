import unittest

from requests import CreateBusinessRequest

class TestCreateBusinessRequest(unittest.TestCase):
    def getSut(self):
        d = {
            "name": "ABCIndustries",
            "email": "example@domain.com",
            "email_confirmation": "example@domain.com",
            "password": "Password1",
            "password_confirmation": "Password1"
        }

        return CreateBusinessRequest(d)

    def test_validate_valid_request(self):
        sut = self.getSut()
        self.assertTrue(sut.validate() == [])

    def test_validate_reports_name_empty(self):
        sut = self.getSut()
        sut.name = ""

        expected = "name cannot be empty"
        result = sut.validate()
        
        self.assertTrue(expected in result)

    def test_validate_reports_name_none(self):
        sut = self.getSut()
        sut.name = None

        expected = "name is required"
        result = sut.validate()

        self.assertTrue(expected in result)

    def test_validate_reports_email_empty(self):
        sut = self.getSut()
        sut.email = ""
        
        expected = "email cannot be empty"
        result = sut.validate()

        self.assertTrue(expected in result)

    def test_validate_reports_email_none(self):
        sut = self.getSut()
        sut.email = None

        expected = "email is required"
        result = sut.validate()

        self.assertTrue(expected in result)

    def test_validate_reports_email_confirmation_empty(self):
        sut = self.getSut()
        sut.email_confirmation = ""

        expected = "email_confirmation cannot be empty"
        result = sut.validate()

        self.assertTrue(expected in result)

    def test_validate_reports_email_confirmation_none(self):
        sut = self.getSut()
        sut.email_confirmation = None

        expected = "email_confirmation is required"
        result = sut.validate()

        self.assertTrue(expected in result)

    def test_validate_reports_emails_dont_match(self):
        sut = self.getSut()
        sut.email_confirmation = "name@domain.com"

        expected = "email must match email_confirmation"
        result = sut.validate()

        self.assertTrue(expected in result)

    def test_validate_reports_password_empty(self):
        sut = self.getSut()
        sut.password = ""

        expected = "password cannot be empty"
        result = sut.validate()

        self.assertTrue(expected in result)

    def test_validate_reports_password_none(self):
        sut = self.getSut()
        sut.password = None

        expected = "password is required"
        result = sut.validate()

        self.assertTrue(expected in result)

    def test_validate_reports_password_confirmation_empty(self):
        sut = self.getSut()
        sut.password_confirmation = ""

        expected = "password_confirmation cannot be empty"
        result = sut.validate()

        self.assertTrue(expected in result)

    def test_validate_reports_password_confirmation_none(self):
        sut = self.getSut()
        sut.password_confirmation = None

        expected = "password_confirmation is required"
        result = sut.validate()

        self.assertTrue(expected in result)

    def test_validate_reports_passwords_dont_match(self):
        sut = self.getSut()
        sut.password_confirmation = "Password2"

        expected = "password must match password_confirmation"
        result = sut.validate()

        self.assertTrue(expected in result)

if __name__ == "__main__":
    unittest.main()
