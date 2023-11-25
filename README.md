# Convert and Merge PDF files

This program converts and merges files from the desired directory into a single pdf file and moves the merged files into a new directory for later deletion by the user.

## Functionality

- run: `python main.py [merged_filename]`

- When prompted, input the desired directory you would like to merge into a single file. Make sure to write the entire directory path.

- If files to be merged are images, they will be converted to pdfs first before being merged.

- Files are merged and the merged file is saved to the working directory.

- After merging, a clean up function will move all merged files into a 'to_be_deleted' directory within the working directory, leaving behind only the merged file.
