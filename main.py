import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def sort_files():
    folder_path = filedialog.askdirectory(title='Select Folder to Sort')
    if not folder_path:
        return
    
    file_count = 0
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1].lower() or 'others'
            destination_folder = os.path.join(folder_path, file_extension)
            
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            
            shutil.move(file_path, os.path.join(destination_folder, filename))
            file_count += 1
    
    status_label.config(text=f"Sorted {file_count} files successfully!", fg='green')

def clear_sorted_files():
    folder_path = filedialog.askdirectory(title='Select Folder to Clear')
    if not folder_path:
        return
    
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
    for subfolder in subfolders:
        subfolder_path = os.path.join(folder_path, subfolder)
        for file in os.listdir(subfolder_path):
            shutil.move(os.path.join(subfolder_path, file), folder_path)
        os.rmdir(subfolder_path)
    
    status_label.config(text='Cleared sorted files successfully!', fg='blue')

def exit_program():
    root.destroy()

# Set up the GUI
root = tk.Tk()
root.title('File Sorter')
root.geometry('400x250')
root.resizable(False, False)

tk.Label(root, text='File Sorting Tool', font=('Arial', 14, 'bold')).pack(pady=10)

sort_button = tk.Button(root, text='Sort Files', command=sort_files, width=20, bg='lightblue')
sort_button.pack(pady=5)

clear_button = tk.Button(root, text='Clear Sorted Files', command=clear_sorted_files, width=20, bg='lightcoral')
clear_button.pack(pady=5)

exit_button = tk.Button(root, text='Exit', command=exit_program, width=20, bg='gray')
exit_button.pack(pady=5)

status_label = tk.Label(root, text='', font=('Arial', 10))
status_label.pack(pady=10)

root.mainloop()
