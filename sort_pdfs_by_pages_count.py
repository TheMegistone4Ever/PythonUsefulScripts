import os
import re
import PyPDF2


directory = "."
pages_dict = dict()
target_extension = ".pdf"
for fn in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, fn)):
        file_name, extension = os.path.splitext(fn)
        if extension == target_extension:
            with open(os.path.join(directory, fn), "rb") as pdf_file:
                pages_dict[fn] = len(PyPDF2.PdfReader(pdf_file).pages)
                print(f"Counted and added to sort: '{fn}'...")
print(f"\nSorted '{target_extension}' files by pages count:")
for i, (file_name, pages_count) in enumerate(dict(sorted(pages_dict.items(), key=lambda item: item[1])).items()):
    print(f"#{i + 1}\t{pages_count = },\t{file_name = }")
print(f"\nTotal '{target_extension}' files:\t{i + 1}")
