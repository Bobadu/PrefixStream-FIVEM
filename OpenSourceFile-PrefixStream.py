import os
from tkinter import filedialog
from tkinter import Tk

root = Tk()
root.withdraw()

print("Please select the folder with textures and models")

folder_path = filedialog.askdirectory()
prefix = input("Enter the phrase to add to the file name: ")

for filename in os.listdir(folder_path):
    new_filename = prefix + '^' + filename
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
    print(f'Renamed file {filename} to {new_filename}')

print('File renaming completed')
print('Thank you for using the program!')
print('Author: Bobadu - https://github.com/Bobadu')




