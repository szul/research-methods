import re

class Validation:

    def __init__(self, required = False, email = False, phone = False, number = False):
        self.required = required
        self.email = email
        self.number = number

class Validator:

    def __init__(self):
        self.valid = True

    def __is_number__(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    #Basic validation for email.
    #Make this more in-depth later.
    def __is_email__(self, email):
        pattern = '[\.\w]{1,}[@]\w+[.]\w+'
        if re.match(pattern, email):
            return True
        else:
            return False

    def validate(self, fields):
        for field in fields:
            if field.validation is not None:
                if field.validation.required and (field.value is None or field.value.strip() == ''):
                    field.error_messages.append('%s is a required value.' % field.name)
                    self.valid = False
                if field.validation.email and (field.value is None or not self.__is_email__(self, field.value)):
                    field.error_messages.append('%s requires a valid email address.' % field.name)
                    self.valid = False
                if field.validation.number and (field.value is None or not self.__is_number__(self, field.value)):
                    field.error_messages.append('%s must be a number.' % field.name)
                    self.valid = False
        return self.valid
