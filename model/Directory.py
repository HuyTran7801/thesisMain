import os

# Specify the absolute path for the directory
class Directory:
    
    def __init__(self, course, user_id):
        self.__user_id = user_id
        self.__course = course
        # self.__filename = None
        self.__specific_path = f"/Admin/Thesis/data/{course}/user{user_id}" 
        self.__files_path = f"/Admin/Thesis/static/files{user_id}" 
        self.__files_path_temp = f"/Admin/Thesis/static/filestemp{user_id}"

    # Create the directory
    def create_directory(self):
        try:
            os.mkdir(self.__specific_path)
            print(f"Directory '{self.__specific_path}' created successfully.")
        except FileExistsError:
            print(f"Directory '{self.__specific_path}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{self.__specific_path}'.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def create_file_directory(self):
        try:
            os.mkdir(self.__files_path)
            print(f"Directory '{self.__files_path}' created successfully.")
        except FileExistsError:
            print(f"Directory '{self.__files_path}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{self.__files_path}'.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
    def create_file_temp_directory(self):
        try:
            os.mkdir(self.__files_path_temp)
            print(f"Directory '{self.__files_path_temp}' created successfully.")
        except FileExistsError:
            print(f"Directory '{self.__files_path_temp}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{self.__files_path_temp}'.")
        except Exception as e:
            print(f"An error occurred: {e}")
            
    def get_vectorDB(self):
        return f'./data/{self.__course}/user{self.__user_id}'
    
    def get_file(self):
        return f'static/filestemp{self.__user_id}'
    
    def remove_file(self, filename):
        if os.path.exists(f"./static/filestemp{self.__user_id}/{filename}"):
            print('Deleted file successfully')
            os.remove(f"./static/filestemp{self.__user_id}/{filename}")
        else:
            print("The file does not exist")

