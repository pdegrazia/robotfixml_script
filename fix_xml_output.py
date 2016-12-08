__author__ = 'paolo'
import glob
from robotfixml import fixml
import shutil
import sys


def is_valid(xml_file):
    with open(xml_file,'r') as file:
        file_lines = file.readlines()
        my_string  = ''.join(file_lines)
        from xml.etree import ElementTree as ET
        try:
            x = ET.fromstring(my_string)
            file.close()
            return True

        except Exception:
            print 'file %s is corrupted!!!' % xml_file
            file.close()
            return False


def main():
    reports_list = glob.glob(sys.argv[1]+'/*.out.xml')
    '''FIX FOR REBOT'''
    print 'Fixing malformed outputs'
    for my_file in reports_list:
        if is_valid(my_file):
            shutil.copyfile(my_file,my_file.replace('.out.xml','.fixed.out.xml'))
        else:
            fixml(my_file,my_file.replace('.out.xml','.fixed.out.xml'))

if __name__ == '__main__':
    main()
