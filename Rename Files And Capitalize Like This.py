import os
import re


directory = "."
for fn in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, fn)):
        file_name, extension = os.path.splitext(fn)
        new_filename = " ".join(word.capitalize() for word in re.split(r"[ _.—-]", file_name)).replace("  ", " ").strip() + extension
        os.rename(os.path.join(directory, fn), os.path.join(directory, new_filename))
        print(f"Renamed {fn} to {new_filename}...")
