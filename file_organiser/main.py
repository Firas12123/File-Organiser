import os
from pathlib import Path
import shutil
import hashlib

file_types = {"Images": [".png",".jpg",".jpeg", ".gif"],
              "Videos": [".mov",".mp4",".m4v", ".qt",".webm",".wmv",".avi",".flv",".f4v"],
              "Documents": [".pdf", ".docx",".txt",".csv",".doc",".rtf"],
              "Code": [".py",".html",".css",".js"],
              "Audio": [".mp3",".wav",".m4a",".flac",".aac",".ogg",".wma"],
              "Apps": [".exe",".app",".dmg",".msi"]}    # dictionary of file types and file extensions
 
target_dir = Path.home() / "Documents" # find the correct files

def scan_file(file):  # scan the file
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
    
def get_hash(file):
    with open(file, "rb") as f:
        contents = f.read()
        m = hashlib.sha256()
        m.update(contents)
        digest = m.hexdigest()
    return(digest)
score= 0
hash_list = []
files_cleaned = 0       # call functions
for file in target_dir.iterdir():
    file_ext = scan_file(file) # checks if file is a file or directory
    if file_ext:
        category = get_category(file_ext)
        if category:   # sorts the valid files into categories
            hash_key = get_hash(file)
            if hash_key not in hash_list:
                hash_list.append(hash_key)
            else:
                score +=1
                word = "duplicate" if score == 1 else "duplicates"    # asks if you want to delete or move duplicates to folder
                delete_input = input(f"Found {score} {word}. Press [Q] to delete or [Any Key] to move to 'Duplicates'\n").lower()
                if delete_input == "q":
                    delete_confirm = input("Press Q again to confirm your choice\n").lower()
                    if delete_confirm == "q":
                        pass
                else:
                    category = "Duplicates"
            move_file(category,file)
            files_cleaned +=1
            
if files_cleaned == 0:          # print success or fail message
    print(f"Your directory {target_dir} is all clean!")
else:
    word = "files" if files_cleaned >1 else "file"
    print(f"Nice we have cleaned up {files_cleaned} {word} from {target_dir}")
    
    