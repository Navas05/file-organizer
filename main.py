import os
import shutil

home_path = os.path.expanduser("~")

def_directions = {".pdf" : os.path.join(home_path, "Documents"),
                  ".doc" : os.path.join(home_path, "Documents"),
                  ".docx" : os.path.join(home_path, "Documents"),
                  ".txt" : os.path.join(home_path, "Documents"),
                  ".zip" : os.path.join(home_path, "Documents"),
                  ".ods" : os.path.join(home_path, "Documents"),
                  ".png" : os.path.join(home_path, "Pictures"),
                  ".jpg" : os.path.join(home_path, "Pictures"),
                  ".jpeg" : os.path.join(home_path, "Pictures"),
                  ".mp3" : os.path.join(home_path, "Music"),
                  ".mp4" : os.path.join(home_path, "Videos") }

def organize_directory(directory):
    for element in os.listdir(directory):
        element_path = os.path.join(directory, element)
        if os.path.isfile(element_path):
            name, extension = os.path.splitext(element)
            extension = extension.lower()

            if extension in def_directions:
                direction = def_directions[extension]
                destination_directory = os.path.join(directory, direction)

                shutil.move(element_path, os.path.join(destination_directory, element))
                print("Moved " + element + " to " + destination_directory)
            else :
                print("Direction unknown, unable to move: " + element)

organize_directory(os.path.join(home_path, "Downloads"))