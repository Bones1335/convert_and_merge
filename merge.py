import os
import sys
from pypdf import PdfWriter

def merge():
    merged_filename = sys.argv[1]
    merger = PdfWriter()

    working_directory = input('Input desired directory to merge: ')
    os.chdir(working_directory)

    for pdf in os.listdir(working_directory):
        merger.append(pdf)


    merger.write(merged_filename)
    merger.close()
    print(f'{merged_filename} created at {working_directory}')
