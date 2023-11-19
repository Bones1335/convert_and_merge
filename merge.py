import os, sys
from pypdf import PdfWriter

merger = PdfWriter()

workingDirectory = input('Input desired directory to merge: ')
os.chdir(workingDirectory)

for pdf in os.listdir(workingDirectory):
    merger.append(pdf)


merger.write(sys.argv[1])
merger.close()
