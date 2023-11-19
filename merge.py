import os, sys
from pypdf import PdfWriter

def merge():
    mergedFilename = sys.argv[1]
    merger = PdfWriter()

    workingDirectory = input('Input desired directory to merge: ')
    os.chdir(workingDirectory)

    for pdf in os.listdir(workingDirectory):
        merger.append(pdf)


    merger.write(mergedFilename)
    merger.close()
    print(f'{mergedFilename} created at {workingDirectory}')
