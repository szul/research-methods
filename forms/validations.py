class Validator:

    def __init__(self):
        self.valid = True
    
    def validate(self, fields):
        for field in fields:
            if field.validation:
                for requirement in field.validation:
                    if requirement == REQUIRED and (field.value is None or field.value.strip() == ''):
                        field.error_message = '%s is a required value' % field.name
                        self.valid = False

        return self.valid

REQUIRED = 'required'
EMAIL = 'email'
PHONE = 'phone'
NUMBER = 'number'
