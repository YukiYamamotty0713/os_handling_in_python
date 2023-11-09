import sys
import os

#It is desiable that argument 'downloaded_filepath_at_first' must be empty.
def rename_file(destination, new_file_name, cond):
    
    # get downloaded_filename with fullpath
    fullpaths = [os.join.path(destination,file) for file in os.listdir(destination)]
    for files in fullpaths:
        if cond in files:
            downloaded_filename_at_first = files

    #execute rename function
    os.rename(downloaded_filename_at_first,
              os.path.join(destination,new_file_name)) 
