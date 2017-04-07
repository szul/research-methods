import odbc
import pyodbc

from generator.config import *
from generator.sqlserver import *

class DataGenerator:
    def __init__(self, connection_string, g_sysobjects):
        self.connection_string = connection_string
        self.sysobjects = None
        self.__acquire_sysobjects__(g_sysobjects)
    def __acquire_sysobjects__(self, select):
        db = pyodbc.connect(self.connection_string)
        cursor = db.cursor()
        cursor.execute(select)
        self.sysobjects = cursor.fetchall()
        cursor.close()
        del cursor
        db.close()
    def generate(self):
        for row in self.sysobjects:
            print row

def test_odbc():
    source =  odbc.SQLDataSources(odbc.SQL_FETCH_FIRST)
    while source:
        print(source)
        source =  odbc.SQLDataSources(odbc.SQL_FETCH_NEXT)

def test_pyodbc():
    db = pyodbc.connect(CONNECTION_STRING)
    print db
    db.close()     

def print_sysobjects():
    db = pyodbc.connect(CONNECTION_STRING)
    cursor = db.cursor()
    cursor.execute(G_SYSOBJECTS)
    rows = cursor.fetchall()
    for row in rows:
        print row
    cursor.close()
    del cursor
    db.close()

if __name__ == '__main__':
    dg = DataGenerator(CONNECTION_STRING, G_SYSOBJECTS)
    dg.generate()
    print 'Testing, analysis, and generation complete.'
