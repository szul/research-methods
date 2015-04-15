
class BaseField:
    
    def __init__(self, field_id = None, name = None, label = None, class_name = None, disabled = False, readonly = False):
        self.field_id = field_id
        self.name = name
        self.label = label
        self.class_name = class_name
        self.disabled = disabled
        self.readonly = readonly

class TextField(BaseField):
    
    def __init__(self, field_id = None, name = None, label = None, class_name = None, disabled = False, readonly = False, maxlength = None):
        Base.__init__(self, field_id = field_id, name = name, label = label, class_name = class_name, disabled = disabled, readonly = readonly)
        self.type_name = "text"
        self.maxlength = maxlength

    def __concat_optional__(self):
        optional = []
        if self.disabled:
            optional.append('disabled="disabled"')
        if self.readonly:
            optional.append('readonly="readonly"')
        if self.maxlength:
            optional.append('maxlength="%s"' % self.maxlength)
        return '' if len(optional) == 0 else ' '.join(optional)
        
    def __str__(self):
        return  """
                <label for="{name}">{label}</label>
                <input type="{type_name}" id="{field_id}" name="{name}" class="{class_name}" {optional} />
                """.format(name = self.name, label = self.label, type_name = self.type_name, field_id = self.field_id, class_name = self.class_name, optional = self.__concat_optional__())

class PasswordField(TextField):

    def __init__(self, field_id = None, name = None, label = None, class_name = None, disabled = False, readonly = False, maxlength = None):
        Base.__init__(self, field_id = field_id, name = name, label = label, class_name = class_name, disabled = disabled, readonly = readonly, maxlength = maxlength)
        self.type_name = "password"

class BaseForm:

    def __init__(self):
        self.field_id = None
        self.name = None
        self.class_name = None
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
                </form>
                """.format(field_id = self.field_id, name = self.name, method = self.method, action = self.action, class_name = self.class_name, fields = self.__concat_fields__())
