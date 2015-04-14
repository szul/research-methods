import pyodbc
import json
import calendar
import datetime
import xml.etree.cElementTree as et

class Base:

    def __init__(self, connection_string):
        self.connection_string = connection_string

    def __str__(self):
        return self.to_xmlstring()

    #This feels like a kludge
    def __double_params__(self, params):
        parameters = []
        for para in params:
            parameters.append(para)
            parameters.append(para)
        return parameters

    def __execute_select__(self, params, sql):
        db = pyodbc.connect(self.connection_string)
        cursor = db.cursor()
        cursor.execute(sql, params)
        row = cursor.fetchone()
        for prop in vars(self):
            if prop != 'connection_string':
                try:
                    self.__dict__[prop] = row.__getattribute__(prop) 
                except IndexError:
                    pass
        cursor.close()
        del cursor
        db.close()

    def to_xml(self):
        doc = et.Element(self.__class__.__name__)
        for key, value in { k: v for k, v in self.__dict__.iteritems() if k != 'connection_string' }.iteritems():
            child = et.SubElement(doc, key)
            #Need to convert bytearray from timestamp into a string
            child.text = str('' if key == 'TS' or value == None else value)
        return doc

    def to_xmlstring(self):
        xml = self.to_xml()
        return et.tostring(xml, encoding='utf8', method='xml')

    def to_json(self):
        def default(obj):
            if isinstance(obj, datetime.datetime):
                if obj.utcoffset() is not None:
                    obj = obj - obj.utcoffset()
                milliseconds = int(calendar.timegm(obj.timetuple()) * 1000 + obj.microsecond / 1000)
                return milliseconds
        return json.dumps({ k: v for k, v in self.__dict__.iteritems() if k != 'connection_string' }, default = default)

class BaseCollection:
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.Collection = []
    
    def to_xml(self):
        pass
    
    def to_json(self):
        pass
