import os
path=input("enter the folder path:")
for root, folders, files in os.walk(path):
    print("\nDirectory:", root)
    for folder in folders:
        print(folders, "folder")
    for file in files:
        print(files,"-files")