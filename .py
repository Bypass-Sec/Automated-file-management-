import os, shutil

path = r"C:\Users\omers\Downloads\Python" #replace this path with the path of the folder you want to organize
os.listdir(path) 
folder_names = ['Images', 'Python files', 'Text files', 'PDF files', 'Word files', 'Excel files', 'Powerpoint files', 'CSV files']

for loop in range(0,2):
   if os.path.exists(path +folder_names[loop]):
        print(path +folder_names[loop])
        os.makedirs(path +folder_names[loop])




