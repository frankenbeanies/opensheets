class CreateBusinessRequest():
    def __init__(self, params):
        self.name = params.get("name")
        self.email = params.get("email")
        self.email_confirmation = params.get("email_confirmation")
        self.password = params.get("password")
        self.password_confirmation = params.get("password_confirmation")

    def validate(self):
        errors = []

        if self.name == "":
            errors.append("name cannot be empty")
        elif self.name == None:
            errors.append("name is required")
 
        if self.email == "":
            errors.append("email cannot be empty")
        elif self.email == None:
            errors.append("email is required")
        
        if self.email_confirmation == "":
            errors.append("email_confirmation cannot be empty")
        elif self.email_confirmation == None:
            errors.append("email_confirmation is required")

        if self.email != self.email_confirmation:
            errors.append("email must match email_confirmation")

        if self.password == "":
            errors.append("password cannot be empty")
        elif self.password == None:
            errors.append("password is required")

        if self.password_confirmation == "":
            errors.append("password_confirmation cannot be empty")
        elif self.password_confirmation == None:
            errors.append("password_confirmation is required")

        if self.password != self.password_confirmation:
            errors.append("password must match password_confirmation")

        return errors