
from ..base import BaseForm, TextField, PasswordField, HiddenField, Checkbox, DateTimeField, TextArea

class LoginForm(BaseForm):

    def __init__(self):
        BaseForm.__init__(self)
        self.data = "User.Person"
        self.field_id = "LoginForm"
        self.name = "LoginForm"
        self.action = '.'
        self.method = 'POST'
        self.fields = [
            TextField(
                data = 'Email',
                field_id = 'Email' + self.field_id,
                name = 'Email' + self.name,
                label = 'Email',
                class_name = 'form-control'
            ),
            PasswordField(
                data = 'Password',
                field_id = 'Password' + self.field_id,
                name = 'Password' + self.name,
                label = 'Password',
                class_name = 'form-control'
            )
        ]
