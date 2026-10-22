import os
import shutil

home_path = os.path.expanduser("~")

def_directions = {".png" : os.path.join(home_path, "Pictures"),
                  ".jpg" : os.path.join(home_path, "Pictures"),
                  ".jpeg" : os.path.join(home_path, "Pictures"),
                  ".mp3" : os.path.join(home_path, "Music"),
                  ".mp4" : os.path.join(home_path, "Videos") }

def move_file(file_path, destination_path):
    shutil.move(file_path, destination_path)    #moved to a secondary function in case you want to change shutil for os.replace() or similar

def organize_directory(directory):
    for element in os.listdir(directory):
        element_path = os.path.join(directory, element)
        if os.path.isfile(element_path):
            name, extension = os.path.splitext(element)
            extension = extension.lower()

            if extension == "":
                continue

            if extension in def_directions:
                destination_directory = def_directions[extension]
                move_file(element_path, destination_directory)
                print("Moved " + element + " to " + destination_directory)
            else :
                folder_name = extension[1:]
                boolean = False
                final_destination = os.path.join(home_path, "Documents", folder_name)

                for subdirectory in os.listdir(os.path.join(home_path, "Documents")):
                    if subdirectory == folder_name:
                        boolean = True
                        move_file(element_path, final_destination)
                        print("Moved " + element + " to " + final_destination)
                if boolean == False:
                    os.makedirs(final_destination, exist_ok=True)
                    move_file(element_path, final_destination)

organize_directory(os.path.join(home_path, "Downloads"))