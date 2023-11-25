import os
import clean_up
import convert
import merge

def main():
    working_directory = input('Input desired directory to merge: ')
    os.chdir(working_directory)
    
    convert.convert(working_directory)
    merge.merge(working_directory)
    clean_up.clean_up(working_directory)

if __name__ == '__main__':
    main()