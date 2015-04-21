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
                        ORDER BY [DateCreated] DESC
                """
        BaseRecord.select(self, parameters, sql)

    def save(self, items):
        def __insert__(self, items):
            parameters = [items['Active'], items['Hidden'], items['ReadOnly'], items['DateCreated'], items['DateModified'], items['US'], items['Code'], items['Name'], items['Description'], items['Email'], items['Password']]
            sql = """
                    INSERT
                        INTO [User].[Person]
                        (
                            [Active],
                            [Hidden],
                            [ReadOnly],
                            [DateCreated],
                            [DateModified],
                            [US],
                            [Code],
                            [Name],
                            [Description],
                            [Email],
                            [Password]
                        )
                        SELECT
                            ISNULL(NULLIF(?, 'None'), 0),
                            ISNULL(NULLIF(?, 'None'), 0),
                            ISNULL(NULLIF(?, 'None'), 0),
                            ISNULL(NULLIF(?, 'None'), GETDATE()),
                            ISNULL(NULLIF(?, 'None'), GETDATE()),
                            NULLIF(?, ''),
                            NULLIF(?, ''),
                            NULLIF(?, ''),
                            NULLIF(?, ''),
                            NULLIF(?, ''),
                            NULLIF(?, '')
                    """
            return (parameters, sql)
        def __update__(self, items):
            parameters = [items['Active'], items['Hidden'], items['ReadOnly'], items['DateCreated'], items['DateModified'], items['US'], items['Code'], items['Name'], items['Description'], items['Email'], items['Password'], items['Id']]
            sql = """
                    UPDATE [User].[Person]
                        SET [Active] = ISNULL(NULLIF(?, 'None'), 0),
                            [Hidden] = ISNULL(NULLIF(?, 'None'), 0),
                            [ReadOnly] = ISNULL(NULLIF(?, 'None'), 0),
                            [DateCreated] = NULLIF(?, 'None'),
                            [DateModified] = ISNULL(NULLIF(?, 'None'), GETDATE()),
                            [US] = NULLIF(?, ''),
                            [Code] = NULLIF(?, ''),
                            [Name] = NULLIF(?, ''),
                            [Description] = NULLIF(?, ''),
                            [Email] = NULLIF(?, ''),
                            [Password] = NULLIF(?, '')
                        FROM [User].[Person]
                        WHERE [Id] = ?
                    """
            return (parameters, sql)
        BaseRecord.save(self, items, __insert__, __update__)

    def delete(self, guid):
        parameters = [guid]
        sql = """
                DELETE 
                    FROM [User].[Person]
                    WHERE [RS] = ?
                """
        BaseRecord.delete(self, parameters, sql)

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
                        WHERE (NULLIF(?, 'None') IS NULL OR [Id] = NULLIF(?, 'None'))
                            AND (NULLIF(?, 'None') IS NULL OR [Active] = NULLIF(?, 'None'))
                            AND (NULLIF(?, 'None') IS NULL OR [Hidden] = NULLIF(?, 'None'))
                            AND (NULLIF(?, 'None') IS NULL OR [ReadOnly] = NULLIF(?, 'None'))
                            AND (NULLIF(?, 'None') IS NULL OR [DateCreated] = NULLIF(?, 'None'))
                            AND (NULLIF(?, 'None') IS NULL OR [DateModified] = NULLIF(?, 'None'))
                            AND (NULLIF(?, 'None') IS NULL OR [US] = NULLIF(?, 'None'))
                            AND (NULLIF(?, 'None') IS NULL OR [RS] = NULLIF(?, 'None'))
                            AND (NULLIF(?, 'None') IS NULL OR [Code] = NULLIF(?, 'None'))
                            AND (NULLIF(?, 'None') IS NULL OR [Name] = NULLIF(?, 'None'))
                            AND (NULLIF(?, 'None') IS NULL OR [Description] = NULLIF(?, 'None'))
                            AND (NULLIF(?, 'None') IS NULL OR [Email] = NULLIF(?, 'None'))
                            AND (NULLIF(?, 'None') IS NULL OR [Password] = NULLIF(?, 'None'))
                        ORDER BY [DateCreated] DESC"""
        self.__execute_select__(parameters, sql, Person)
