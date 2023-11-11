import sys
import os

#It is desiable that argument 'downloaded_filepath_at_first' must be empty.
def execute_rename_file(save_path, new_file_name, extension):
    fullpaths= []
    # get downloaded_filename with fullpath
    a = os.listdir(save_path)
    for file in a:
        if extension in file:
            fullpaths.append(os.path.join(save_path,file))  
            print(fullpaths)
    
    old_file_path = fullpaths[0]
    new_file_path = os.path.join(save_path,new_file_name)
    #execute rename function
    os.rename(old_file_path, new_file_path) 
    
def main():
    save_path = 'C://Users\\Owner\\OneDrive\\デスクトップ\\LOCAL\\Python\\os_functions'
    execute_rename_file(save_path = save_path,new_file_name = '簡単検索.csv',extension='.csv')

main()

