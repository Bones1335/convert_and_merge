import os
import sys
from pypdf import PdfWriter

def merge(working_directory):
    merged_filename = sys.argv[1]
    merger = PdfWriter()

    for pdf in os.listdir(working_directory):
        merger.append(pdf)


    merger.write(merged_filename)
    merger.close()
    print(f'{merged_filename} created at {working_directory}')
