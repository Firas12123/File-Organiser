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
default_directories = ["Downloads","Documents","Videos","Pictures","Music","Desktop"]
score = 0
def get_directory(score):
    while score == 0:
        for directory in default_directories:
            print(directory, end = ", ")
        dir_input = input("\nEnter a valid default library from the list above or input your own directory you want to sort!\n\n")
        if dir_input in default_directories:   # if user inputs a default directory then returns target_dir
            target_dir = Path.home() / dir_input
            score+=1
            return target_dir
        else:
            dir_input_path = Path(dir_input)
            if dir_input_path.is_dir():   # if user input is a directory return the input as target_dir
                target_dir = dir_input_path
                score +=1
                return target_dir
            else:
                print("Sorry this path wasnt found\nMake sure to check for any spelling and punctuation!\n")
            



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
target_dir = get_directory(score)
if target_dir:
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
                    delete_input = input(f"Found {score} {word}. Press [Q] to delete or [Any Other Key] to move to 'Duplicates'\n").lower()
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
    
    