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


def parse_index(location, index_file, year='all'):
    """Loops through the index file specified"""
    with open(location+'/'+index_file) as file_handler:
        for line in file_handler:
            search = re.match(
                '^([0-9]{6})\t'
                '([a-z0-9/]+)\t'
                '([0-9]{2})/([0-9]{2})/(20[0-9]{2})\t'
                '([a-z0-9]+)', line)
            index_number = search.group(1)
            index_folder = search.group(2)
            index_day = search.group(3)
            index_month = search.group(4)
            index_year = search.group(5)
            index_vendor = search.group(6)
            if (
                    year == 'all' or
                    (year.isnumeric() and int(year) == int(index_year))):
                document_file = (
                    f'{index_folder}/'
                    f'{index_number}-'
                    f'{index_year}{index_month}{index_day}-'
                    f'{index_vendor}.pdf')
                exists(location, document_file)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        parse_index(os.getcwd(), 'document-index.txt', year=sys.argv[1])
    else:
        parse_index(os.getcwd(), 'document-index.txt')
