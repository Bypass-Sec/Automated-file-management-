import os, shutil

path = r"C:\Users\omers\Downloimport os" #replace with your path destination
import shutil
import tkinter as tk
from tkinter import filedialog


def sort_files():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1]
            destination_folder = os.path.join(folder_path, file_import os


            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            shutil.move(file_path, os.path.join(destination_folder, filename))

# Set up the GUI
root = tk.Tk()
root.title('File Sorter')

sort_button = tk.Button(root, text='Sort Files', command=sort_files
