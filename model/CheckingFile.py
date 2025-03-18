import os
# Get the list of all files and directories
class CheckingFile:
    def __init__(self, path):
        self.__path = path
        
    def show_files(self):
        dir_list = os.listdir(self.__path)
        print("Files and directories in '", self.__path, "' :")
        # prints all files
        return dir_list