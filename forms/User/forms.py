
from ..base import BaseForm, TextField, PasswordField

class PersonForm(BaseForm):

    def __init__(self):
        BaseForm.__init__(self)
        self.field_id = "PersonForm"
        self.name = "PersonForm"
        self.action = '.'
        self.method = 'POST'
        self.fields = [
            TextField(
                data = 'Email',
                field_id = 'Email' + self.field_id,
                name = 'Email' + self.name,
                label = 'Email'
            ),
            PasswordField(
                data = 'Password',
                field_id = 'Password' + self.field_id,
                name = 'Password' + self.name,
                label = 'Password'
            )
        ]
