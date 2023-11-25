import os
from PIL import Image

def convert(working_directory):
    for filename in os.listdir(working_directory):
        if filename.endswith('.jpeg') or filename.endswith('.jpg') or filename.endswith('.png'):
            img_path = os.path.join(working_directory, filename)
            img = Image.open(img_path)
            pdf_path = os.path.join(working_directory, filename[:-4] + '.pdf')
            img.save(pdf_path, 'PDF', resolution=100.0)