import pyodbc, json, calendar, datetime
import xml.etree.cElementTree as et

from config import CONNECTION_STRING

class Base:

    def __init__(self, connection_string = None):
        if connection_string is not None:
            self.connection_string = connection_string
        else:
            try:
                self.connection_string = CONNECTION_STRING
            except:
                raise Exception("Connection string not provided!")
        
    #This feels like a kludge
    def __double_params__(self, params):
        parameters = []
        for para in params:
            parameters.append(para)
            parameters.append(para)
        return parameters
    
    def __get_cursor__(self, sql, params):
        db = pyodbc.connect(self.connection_string)
        cursor = db.cursor()
        cursor.execute(sql, params)
        return (db, cursor)
    
    def __cleanup_db__(self, db, cursor):
        cursor.close()
        del cursor
        db.close()

class BaseRecord(Base):

    def __init__(self, connection_string):
        Base.__init__(self, connection_string = None)

    def __str__(self):
        return self.to_xmlstring()

    def __execute_select__(self, params, sql):
        db, cursor = self.__get_cursor__(sql, params)
        row = cursor.fetchone()
        for prop in vars(self):
            if prop != 'connection_string':
                try:
                    self.__dict__[prop] = row.__getattribute__(prop) 
                except IndexError:
                    pass
        self.__cleanup_db__(db, cursor)

    def save(self, items, insert, update):
        if items['Id'] is not None and items['Id'] != '':
            return update(self, items)
        else:
            return insert(self, items)

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

class BaseCollection(Base):
    
    def __init__(self, connection_string = None):
        Base.__init__(self, connection_string)
        self.Collection = []
    
    # def __str__(self):
    #     return self.to_xmlstring()

    def __execute_select__(self, params, sql, Entry):
        db, cursor = self.__get_cursor__(sql, params)
        rows = cursor.fetchall()
        for row in rows:
            entry = Entry()
            for prop in vars(entry):
                if prop != 'connection_string':
                    try:
                        entry.__dict__[prop] = row.__getattribute__(prop) 
                    except IndexError:
                        pass
            self.Collection.append(entry)
        self.__cleanup_db__(db, cursor)

    # def to_xml(self):
    #     doc = et.Element(self.__class__.__name__)
    #     for key, value in { k: v for k, v in self.__dict__.iteritems() if k != 'connection_string' }.iteritems():
    #         child = et.SubElement(doc, key)
    #         #Need to convert bytearray from timestamp into a string
    #         child.text = str('' if key == 'TS' or value == None else value)
    #     return doc
    # 
    # def to_xmlstring(self):
    #     xml = self.to_xml()
    #     return et.tostring(xml, encoding='utf8', method='xml')
    # 
    # def to_json(self):
    #     def default(obj):
    #         if isinstance(obj, datetime.datetime):
    #             if obj.utcoffset() is not None:
    #                 obj = obj - obj.utcoffset()
    #             milliseconds = int(calendar.timegm(obj.timetuple()) * 1000 + obj.microsecond / 1000)
    #             return milliseconds
    #     return json.dumps({ k: v for k, v in self.__dict__.iteritems() if k != 'connection_string' }, default = default)
