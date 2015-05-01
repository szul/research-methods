
from ..base import BaseForm, TextField, PasswordField, HiddenField, Checkbox, DateTimeField, TextArea
from ..validations import Validation

class PersonForm(BaseForm):

    def __init__(self):
        BaseForm.__init__(self)
        self.data = "User.Person"
        self.field_id = "PersonForm"
        self.name = "PersonForm"
        self.action = '.'
        self.method = 'POST'
        self.fields = [
            HiddenField(
                data = 'Id',
                field_id = 'Id' + self.field_id,
                name = 'Id' + self.name,
                label = 'Id',
            ),
            Checkbox(
                data = 'Active',
                field_id = 'Active' + self.field_id,
                name = 'Active' + self.name,
                label = 'Active',
            ),
            Checkbox(
                data = 'Hidden',
                field_id = 'Hidden' + self.field_id,
                name = 'Hidden' + self.name,
                label = 'Hidden',
            ),
            Checkbox(
                data = 'ReadOnly',
                field_id = 'ReadOnly' + self.field_id,
                name = 'ReadOnly' + self.name,
                label = 'ReadOnly',
            ),
            DateTimeField(
                data = 'DateCreated',
                field_id = 'DateCreated' + self.field_id,
                name = 'DateCreated' + self.name,
                label = 'DateCreated',
                class_name = 'form-control'
            ),
            DateTimeField(
                data = 'DateModified',
                field_id = 'DateModified' + self.field_id,
                name = 'DateModified' + self.name,
                label = 'DateModified',
                class_name = 'form-control'
            ),
            HiddenField(
                data = 'US',
                field_id = 'US' + self.field_id,
                name = 'US' + self.name,
                label = 'US',
                class_name = 'form-control'
            ),
            HiddenField(
                data = 'RS',
                field_id = 'RS' + self.field_id,
                name = 'RS' + self.name,
                label = 'RS',
                class_name = 'form-control'
            ),
            TextField(
                data = 'Code',
                field_id = 'Code' + self.field_id,
                name = 'Code' + self.name,
                label = 'Code',
                class_name = 'form-control'
            ),
            TextField(
                data = 'Name',
                field_id = 'Name' + self.field_id,
                name = 'Name' + self.name,
                label = 'Name',
                class_name = 'form-control',
                validation = Validation(required = True)
            ),
            TextArea(
                data = 'Description',
                field_id = 'Description' + self.field_id,
                name = 'Description' + self.name,
                label = 'Description',
                class_name = 'form-control'
            ),
            TextField(
                data = 'Email',
                field_id = 'Email' + self.field_id,
                name = 'Email' + self.name,
                label = 'Email',
                class_name = 'form-control',
                validation = Validation(required = True, email = True)
            ),
            PasswordField(
                data = 'Password',
                field_id = 'Password' + self.field_id,
                name = 'Password' + self.name,
                label = 'Password',
                class_name = 'form-control',
                validation = Validation(required = True)
            )
        ]
