import os
import merge

def main():
    working_directory = input('Input desired directory to merge: ')
    os.chdir(working_directory)
    
    merge.merge(working_directory)

if __name__ == '__main__':
    main()