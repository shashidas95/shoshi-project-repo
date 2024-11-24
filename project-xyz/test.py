import os

folders = input("write a folders name with space:  ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("please provide a valid folder name")
        continue
    for file in files:
          print(file)


