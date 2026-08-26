import os
from pathlib import Path
import shutil
import hashlib
#create a dictionary with the file types with a list of the file extensions needed

file_types = {"Images": [".png",".jpg",".jpeg", ".gif"],
              "Videos": [".mov",".mp4",".m4v", ".qt",".webm",".wmv",".avi",".flv",".f4v"],
              "Documents": [".pdf", ".docx",".txt",".csv",".doc",".rtf"],
              "Code": [".py",".html",".css",".js"]}
 

target_dir = Path.home() / "Documents" # find the correct files

def scan_file(file):
    if not file.is_file():
        return None
    file_ext = file.suffix.lower()
    return file_ext
    
def get_category(file_ext):     # get the category the file belongs to
    for category, value in file_types.items():
        if file_ext in value:
            return category
    return None

def move_file(category,file): # create category
    new_folder = target_dir / category
    if not os.path.exists(new_folder):   # if folder images/ video etc doesnt exist create one
        os.makedirs(new_folder)
    shutil.move(file, new_folder)
    print(f"{file} has been moved into {new_folder}")
    

    
for file in target_dir.iterdir():
    file_ext = scan_file(file)
    if file_ext:
        category = get_category(file_ext)
        if category:
            move_file(category,file)
    
    
    
    

