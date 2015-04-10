import os
import csv
import json
import xml.etree.cElementTree as et

class ResearchData:

    def __init__(self, format):
        self.format = format
        self.data = None
        self.data_format = None

    def __opencsvfile__(self, filetoopen):
        csvfile = open(filetoopen, 'rb')
        r = csv.reader(csvfile, delimiter=',')
        headers = []
        for idx, row in enumerate(r):
            if idx == 0:
                headers = row
                break
        return (r, headers)

    def __csv_to_xml__(self, data, dtype):
        if dtype == 'file':
            r, headers = self.__opencsvfile__(data)
            #Need to create an XML Schema for research.
            doc = et.Element('Data')
            for idx, row in enumerate(r):
                childrow = et.SubElement(doc, 'Row')
                for idx2, col in enumerate(row):
                    child = et.SubElement(childrow, headers[idx2])
                    child.text = col
            self.data = doc
            self.data_format = 'xml'
        return self.data

    def __csv_to_json__(self, data, dtype):
        if dtype == 'file':
            r, headers = self.__opencsvfile__(data)
            results = []
            for idx, row in enumerate(r):
                entry = {}
                for idx2, col in enumerate(row):
                    entry[headers[idx2]] = col
                results.append({ 'row' : entry })
            self.data = json.dumps({ 'data': results })
            self.data_format = 'json'
        return self.data

    def to_xml(self, data, dtype = 'file'):
        if self.format == 'csv':
            return self.__csv_to_xml__(data, dtype)

    def to_json(self, data, dtype = 'file'):
        if self.format == 'csv':
            return self.__csv_to_json__(data, dtype)
