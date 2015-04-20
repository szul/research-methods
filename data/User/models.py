import pyodbc

from ..base import BaseRecord, BaseCollection

class Person(BaseRecord):

    def __init__(self, connection_string = None):
        BaseRecord.__init__(self, connection_string)
        self.Id = None
        self.Active = None
        self.Hidden = None
        self.ReadOnly = None
        self.DateCreated = None
        self.DateModified = None
        self.US = None
        self.RS = None
        self.Meta = None
        self.Code = None
        self.Name = None
        self.Description = None
        self.TS = None
        self.Email = None
        self.Password = None

    def select(self, id = None, active = 'True', hidden = 'False', readonly = 'False', datecreated = None, datemodified = None, us = None, rs = None, code = None, name = None, description = None, email = None, password = None):
        #No Meta or TS for this.
        parameters = self.__double_params__([id, active, hidden, readonly, datecreated, datemodified, us, rs, code, name, description, email, password])
        sql = """
                SELECT TOP 1
                    [Id],
                    [Active],
                    [Hidden],
                    [ReadOnly],
                    [DateCreated],
                    [DateModified],
                    [US],
                    [RS],
                    [Meta],
                    [Code],
                    [Name],
                    [Description],
                    [TS],
                    [Email],
                    [Password]
                        FROM [User].[Person]
                        WHERE (NullIf(?, 'None') IS NULL OR [Id] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [Active] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [Hidden] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [ReadOnly] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [DateCreated] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [DateModified] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [US] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [RS] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [Code] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [Name] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [Description] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [Email] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [Password] = NullIf(?, 'None'))
                        ORDER BY [DateCreated] DESC"""
        self.__execute_select__(parameters, sql)

    def save(self, items):
        def __insert__(self, items):
            print items
        def __update__(self, items):
            print items
        BaseRecord.save(self, items, __insert__, __update__)

class PersonCollection(BaseCollection):
    
    def __init__(self, connection_string = None):
        BaseCollection.__init__(self, connection_string)

    def select(self, id = None, active = 'True', hidden = 'False', readonly = 'False', datecreated = None, datemodified = None, us = None, rs = None, code = None, name = None, description = None, email = None, password = None):
        #No Meta or TS for this.
        parameters = self.__double_params__([id, active, hidden, readonly, datecreated, datemodified, us, rs, code, name, description, email, password])
        sql = """
                SELECT
                    [Id],
                    [Active],
                    [Hidden],
                    [ReadOnly],
                    [DateCreated],
                    [DateModified],
                    [US],
                    [RS],
                    [Meta],
                    [Code],
                    [Name],
                    [Description],
                    [TS],
                    [Email],
                    [Password]
                        FROM [User].[Person]
                        WHERE (NullIf(?, 'None') IS NULL OR [Id] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [Active] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [Hidden] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [ReadOnly] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [DateCreated] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [DateModified] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [US] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [RS] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [Code] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [Name] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [Description] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [Email] = NullIf(?, 'None'))
                            AND (NullIf(?, 'None') IS NULL OR [Password] = NullIf(?, 'None'))
                        ORDER BY [DateCreated] DESC"""
        self.__execute_select__(parameters, sql, Person)
