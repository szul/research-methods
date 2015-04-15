
from ..base import BaseForm, TextField, PasswordField

class LoginForm(BaseForm):

    def __init__(self):
        self.field_id = "login"
        self.name = "login"
        self.action = '.'
        self.method = 'POST'
        self.fields = [
            TextField(
                field_id = 'email',
                name = 'email',
                label = 'Email'
            ),
            PasswordField(
                field_id = 'password',
                name = 'password',
                label = 'Password'
            )
        ]
