from pathlib import Path

import sys
# Input target folder as command line argument
directory = Path(sys.argv[1])

# Alternatively, preconfigure one or multiple paths to be sorted by removing comment below and entering path variables. Then uncomment line above
#directory = Path("/home/patrick/Downloads")

# The folders you want to have.
# The keys are what you refer to in the code
# The Values are the actual names of the folders that get creatad.
folders = {
    "Images": "Images",
    "Videos": "Videos",
    "Archives": "Archives",
    "Audio": "Audio",
    "Other": "Other"
}

# These are the "actions".
# The keys are the file extensions you want to move into the specified folder.
# The values are the folder you want the files with the extension to go in to.
actions = {
    ".png": folders["Images"],
    ".jpg": folders["Images"],
    ".gif": folders["Images"],

    ".mp4": folders["Videos"],
    ".mov": folders["Videos"],
    ".avi": folders["Videos"],

    ".rar": folders["Archives"],
    ".zip": folders["Archives"],
    ".7z": folders["Archives"],
    ".gz": folders["Archives"],
    ".tar.gz": folders["Archives"],
    ".tar.xz": folders["Archives"],
    ".tar.bz2": folders["Archives"],
    ".tar.lzma": folders["Archives"],
    
    ".wav": folders["Audio"],
    ".mp3": folders["Audio"],
    ".ogg": folders["Audio"],
    ".flac": folders["Audio"],
}


def create_directories(dir):
    for dir_name in folders.values():
        if dir.joinpath(dir_name) not in dir.iterdir():
            dir.joinpath(dir_name).mkdir()


def organize_folder(dir):
    dir = Path(dir)

    # dir.glob("*,*") is used to get all the files (and folders) in the directory.
    for file in dir.glob("*.*"):
        if file.is_file():
            # If the file has an extension that's in the actions and destination, move the file.
            try:
                dest_path = dir.joinpath(actions[file.suffix], file.name)
                file.rename(dest_path)
            
            # If the file doesn't have an extension, move it into the "Other" folder. 
            except KeyError:
                dest_path = dir.joinpath(folders["Other"], file.name)
                file.rename(dest_path)


if __name__ == "__main__":
    # This function checks if the sub-folders exists. If they don't, create them.
    create_directories(directory)
    
    organize_folder(directory)

