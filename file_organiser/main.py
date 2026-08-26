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
for file in target_dir.iterdir():
    if file.is_file():
        file_ext = file.suffix.lower()
        for key, values in file_types.items():
            for ext in values:
                if file_ext == ext:
                    new_path = target_dir / key
                    if not os.path.exists(new_path):
                        os.makedirs(new_path)
                    shutil.move(file, new_path)
                    
                    
                
                

    