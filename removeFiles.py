#CAUTION: This code may delete the entire root if it was created more than 30 days ago.
#That may involve your entire file system.
#Please use it responsibly at your own risk.

import time
import os
import shutil

path = input("Enter the folder destination where files older than 30 days should be deleted: ")
days = 30
seconds_in_days = time.time() - days*24*60*60
deletedFileCount = 0
deletedFolderCount = 0

if os.path.exists(path):
    list_of_files_and_dirs = os.walk(path)
    for root, dirs, files in list_of_files_and_dirs:
        if(seconds_in_days >= getDateCreated(root)):
            removeFolder(root)
            deletedFolderCount = deletedFolderCount + 1
            break

        else:
            for dir in dirs:
                dirPath = os.path.join(root, dir)
                if(seconds_in_days >= getDateCreated(dirPath)):
                    removeFolder(dirPath)
                    deletedFolderCount = deletedFolderCount + 1
            
            for file in files:
                filePath = os.path.join(root, file)
                if(seconds_in_days >= getDateCreated(file)):
                    removeFile(filePath)
                    deletedFileCount = deletedFileCount + 1

    else:
        if seconds_in_days >= getDateCreated(path):
            removeFile(path)
            deletedFileCount = deletedFileCount + 1

else:
    print("Path not found!")
    deletedFileCount = deletedFileCount + 1
    
print("Number of folders deleted: ", deletedFolderCount)
print("Number of files deleted: ", deletedFileCount)

def getDateCreated(path):
    ctime = os.stat(path).st_ctime
    return ctime

def removeFolder(path):
    if not shutil.rmtree(path):
        print(path + " has been removed successfully")

    else:
        print("Failed to delete " + path)

def removeFile(path):
    if not os.remove(path):
        print(path + " has been removed successfully")

    else:
        print("Failed to delete " + path)