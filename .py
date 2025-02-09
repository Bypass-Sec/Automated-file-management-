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
            destination_folder = os.path.join(folder_path, file_extension)

          
