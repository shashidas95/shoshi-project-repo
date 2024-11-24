import os

folders = input("write a folders name with space:  ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("please provide a valid folder name it looks like doesnot exists  " + folder )
        continue
    except PermissionError:
        print("currently you dont have permission to aceess the folder/file " + folder)
        continue
    for file in files:
          print(file)


