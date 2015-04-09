import os
import csv
import xml.etree.cElementTree as et

class ResearchData:

    def __init__(self, format):
        self.format = format
        self.data = None
        self.data_format = None

    def __csv_to_xml__(self, data, dtype):
        if dtype == 'file':
            with open(data, 'rb') as csvfile:
                headers = []
                #Need to create an XML Schema for research.
                doc = et.Element('Data')
                r = csv.reader(csvfile, delimiter=',')
                for idx, row in enumerate(r):
                    if idx == 0:
                        headers = row
                    childrow = et.SubElement(doc, 'Row')
                    for idx2, col in enumerate(row):
                        child = et.SubElement(childrow, headers[idx2])
                        child.text = col
            self.data = doc
            self.data_format = 'xml'
        return self.data

    def to_xml(self, data, dtype = 'file'):
        if self.format == 'csv':
            return self.__csv_to_xml__(data, dtype)
