import uuid
from validations import Validator

class BaseField:
    
    def __init__(self, data = None, field_id = None, name = None, label = None, class_name = None, disabled = False, readonly = False):
        self.data = data
        self.field_id = field_id
        self.name = name
        self.label = label
        self.class_name = class_name
        self.disabled = disabled
        self.readonly = readonly
        self.validation = []
        self.value = None
        self.error_message = None
        
    def __concat_optional__(self):
        optional = []
        if self.disabled:
            optional.append('disabled="disabled"')
        if self.readonly:
            optional.append('readonly="readonly"')
        return '' if len(optional) == 0 else ' '.join(optional)

class TextField(BaseField):
    
    def __init__(self, data = None, field_id = None, name = None, label = None, class_name = '', disabled = False, readonly = False, maxlength = None):
        BaseField.__init__(self, data = data, field_id = field_id, name = name, label = label, class_name = class_name, disabled = disabled, readonly = readonly)
        self.type_name = "text"
        self.maxlength = maxlength

    def __concat_optional__(self):
        optional = []
        optional.append(BaseField.__concat_optional__(self))
        if self.maxlength:
            optional.append('maxlength="%s"' % self.maxlength)
        return '' if len(optional) == 0 else ' '.join(optional)
        
    def __str__(self):
        return  """
                <div>
                    <label for="{name}">{label}</label>
                    <input type="{type_name}" id="{field_id}" name="{name}" class="{class_name}" value="{value}" {optional} />
                </div>
                """.format(name = self.name, label = self.label, type_name = self.type_name, field_id = self.field_id, class_name = self.class_name, value = '' if self.value is None else self.value, optional = self.__concat_optional__())

class Checkbox(BaseField):
    
    def __init__(self, data = None, field_id = None, name = None, label = None, class_name = '', disabled = False, readonly = False, maxlength = None):
        BaseField.__init__(self, data = data, field_id = field_id, name = name, label = label, class_name = class_name, disabled = disabled, readonly = readonly)
        self.type_name = "checkbox"

    def __concat_optional__(self):
        return BaseField.__concat_optional__(self);
        
    def __str__(self):
        checked = ''
        if self.value is not None and self.value == True:
            checked = 'checked="checked"'
        return  """
                <div>
                    <label for="{name}">
                        <input type="{type_name}" id="{field_id}" name="{name}" class="{class_name}" {checked} {optional} /> {label}
                    </label>
                </div>
                """.format(name = self.name, label = self.label, type_name = self.type_name, field_id = self.field_id, class_name = self.class_name, checked = checked, optional = self.__concat_optional__())

class DateTimeField(TextField):

    def __init__(self, data = None, field_id = None, name = None, label = None, class_name = '', disabled = False, readonly = False, maxlength = None):
        TextField.__init__(self, data = data, field_id = field_id, name = name, label = label, class_name = class_name, disabled = disabled, readonly = readonly, maxlength = maxlength)
        self.type_name = "datetime-local"
    
    def __str__(self):
        value = None
        if self.value is not None:
            parts = str(self.value).split(' ')
            value = 'T'.join(parts)
        return  """
                <div>
                    <label for="{name}">{label}</label>
                    <input type="{type_name}" id="{field_id}" name="{name}" class="{class_name}" value="{value}" {optional} />
                </div>
                """.format(name = self.name, label = self.label, type_name = self.type_name, field_id = self.field_id, class_name = self.class_name, value = '' if value is None else value, optional = self.__concat_optional__())
                #2015-04-14 10:14:39.980000        

class PasswordField(TextField):

    def __init__(self, data = None, field_id = None, name = None, label = None, class_name = '', disabled = False, readonly = False, maxlength = None):
        TextField.__init__(self, data = data, field_id = field_id, name = name, label = label, class_name = class_name, disabled = disabled, readonly = readonly, maxlength = maxlength)
        self.type_name = "password"

class HiddenField(TextField):

    def __init__(self, data = None, field_id = None, name = None, label = None, class_name = '', disabled = False, readonly = False, maxlength = None):
        TextField.__init__(self, data = data, field_id = field_id, name = name, label = label, class_name = class_name, disabled = disabled, readonly = readonly, maxlength = maxlength)
        self.type_name = "hidden"
        
    def __str__(self):
        return  """
                <input type="{type_name}" id="{field_id}" name="{name}" class="{class_name}" value="{value}" {optional} />
                """.format(name = self.name, type_name = self.type_name, field_id = self.field_id, class_name = self.class_name, value = '' if self.value is None else self.value, optional = self.__concat_optional__())

class TextArea(BaseField):
    
    def __init__(self, data = None, field_id = None, name = None, label = None, class_name = '', disabled = False, readonly = False, maxlength = None):
        BaseField.__init__(self, data = data, field_id = field_id, name = name, label = label, class_name = class_name, disabled = disabled, readonly = readonly)
        self.type_name = "textarea"
        self.maxlength = maxlength

    def __concat_optional__(self):
        optional = []
        optional.append(BaseField.__concat_optional__(self))
        if self.maxlength:
            optional.append('maxlength="%s"' % self.maxlength)
        return '' if len(optional) == 0 else ' '.join(optional)
        
    def __str__(self):
        return  """
                <div>
                    <label for="{name}">{label}</label>
                    <textarea id="{field_id}" name="{name}" class="{class_name}" {optional}>{value}</textarea>
                </div>
                """.format(name = self.name, label = self.label, type_name = self.type_name, field_id = self.field_id, class_name = self.class_name, value = '' if self.value is None else self.value, optional = self.__concat_optional__())

class BaseForm:

    def __init__(self):
        self.field_id = None
        self.name = None
        self.class_name = ''
        self.action = '.'
        self.method = 'GET'
        self.fields = []
        
    def __concat_fields__(self):
        fields = []
        for field in self.fields:
            fields.append(str(field))
        return ' '.join(fields)

    def __str__(self):
        return """
                <form id="{field_id}" name="{name}" method="{method}" action="{action}" class="{class_name}">
                    {fields}
                    <input type="submit" id="submit" name="submit" value="Submit" />
                </form>
                """.format(field_id = self.field_id, name = self.name, method = self.method, action = self.action, class_name = self.class_name, fields = self.__concat_fields__())

    def fill(self, model, items = None):
        if items is not None:
            for item in items:
                model.__dict__[item.replace(self.name, '')] = '1' if items[item] == 'on' else items[item]
            self.fill(model)
        else:
            for field in self.fields:
                field.value = model.__dict__[field.data]

    def validation(self):
        validator = Validator()
        return validator.validate(self.fields)

    def expand_fn(self, item):
        return ''.join([item, self.name])

    def prepare(self, model = None):
        items = {}
        for field in self.fields:
            if field.name.replace(self.name, '') == 'US' and (field.value is None or field.value == ''):
                items[field.name.replace(self.name, '')] = uuid.UUID('{00000000-0000-0000-0000-000000000000}')
            items[field.name.replace(self.name, '')] = field.value
        return items
