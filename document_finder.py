#!/usr/bin/env python3
"""Checks that all the files defined in the index file exist"""
import re
import os.path


def exists(location, filename):
    """Checks if a file exists"""
    if os.path.exists(location+'/'+filename):
        print('FOUND: ' + filename)
    else:
        print('ERROR: ' + filename)


def parse_index(location, index_file):
    """Loops through the index file specified"""
    with open(location+'/'+index_file) as file_handler:
        for line in file_handler:
            search = re.match(
                '^([0-9]{6})\t'
                '([a-z0-9/]+)\t'
                '([0-9]{2})/([0-9]{2})/(20[0-9]{2})\t'
                '([a-z0-9]+)', line)
            index = search.group(1)
            folder = search.group(2)
            day = search.group(3)
            month = search.group(4)
            year = search.group(5)
            vendor = search.group(6)
            document_file = f'{folder}/{index}-{year}{month}{day}-{vendor}.pdf'
            exists(location, document_file)


if __name__ == "__main__":
    parse_index(os.getcwd(), 'document-index.txt')
