import os
#you'll need the os module for renaming files

os.chdir('C:/Users/You/folderYouAreEditing')
#this sets your directory to the folder containing the files you want to rename

newName = input("Enter file name add-on:")
#calls the input function so it will ask for your new word or number etc.

for f in os.listdir():
  f_name, f_ext = os.path.splitext(f)
  os.rename(f, newName + f_name + f_ext)
#splits the filenames of all files in the directory into separate parts, so you can put the newName word where you like
