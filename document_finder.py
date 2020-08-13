#!/usr/bin/env python3
"""Checks that all the files defined in the index file exist"""
import re
import os.path


class Document:
    """Class describing a document location"""
    # pylint: disable=too-many-instance-attributes
    # Number of attributes are required to describe the document.
    def __init__(self, line):
        search = re.match(
            '^([0-9]{6})\t'
            '([a-z0-9/]+)\t'
            '([0-9]{2})/([0-9]{2})/(20[0-9]{2})\t'
            '([a-z0-9]+)\t'
            '([a-z0-9 ]+)'
            '(\\([a-z0-9]+\\))?', line)
        self.number = search.group(1)
        self.folder = search.group(2)
        self.day = int(search.group(3))
        self.month = int(search.group(4))
        self.year = int(search.group(5))
        self.vendor = search.group(6)
        self.description = search.group(7)
        self.reference = search.group(8)
        if self.reference:
            self.reference = self.reference

    def __str__(self):
        return (f'{self.number}\t'
                f'{self.folder}\t'
                f'{self.day}/{self.month}/{self.year}\t'
                f'{self.vendor}\t'
                f'{self.description}\t'
                f'{self.reference}'
                )

    def get_file(self):
        """Return the expected filename of the file"""
        return (
            f'{self.folder}/'
            f'{self.number}-'
            f'{self.year}{self.month}{self.day}-'
            f'{self.vendor}.pdf'
            )


def exists(location, filename):
    """Checks if a file exists"""
    if os.path.exists(location+'/'+filename):
        print('FOUND: ' + filename)
    else:
        print('ERROR: ' + filename)


def parse_index(location, index_file, year='all'):
    """Loops through the index file specified"""
    with open(location+'/'+index_file) as file_handler:
        for line in file_handler:
            document = Document(line)
            if (
                    year == 'all' or
                    (year.isnumeric() and int(year) == document.year)):
                exists(location, document.get_file())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        parse_index(os.getcwd(), 'document-index.txt', year=sys.argv[1])
    else:
        parse_index(os.getcwd(), 'document-index.txt')
