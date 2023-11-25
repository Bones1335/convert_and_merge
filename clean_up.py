import os
import sys
from shutil import move

def clean_up(working_directory):
    delete = 'to_be_deleted'
    if os.path.isdir(delete) == False:
        os.mkdir(delete)

    for filename in os.listdir(working_directory):
        
        if filename != sys.argv[1]:
            move(filename, delete)