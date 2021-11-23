import os
import glob
 
directory = '/Users/yukihirakawa/Desktop/django/pdftext/'
file_type = '*.pdf'
path = directory + file_type

pdf_list = glob.glob(path)
for item in pdf_list:
    split_item = item.split("/")
    file_name = split_item[-1].replace(".pdf","")
    print(file_name)