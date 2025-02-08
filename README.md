
# 📂 File Management Automation Script

A Python script to **automate file organization** by sorting files into categorized folders based on their extensions. This script helps keep your directories clean and organized.

---

## 🚀 Features

- 📁 Automatically moves files into relevant categories (Images, Documents, Videos, etc.).  
- 🔄 Handles common file types like `.jpg`, `.pdf`, `.mp4`, `.zip`, etc.  
- 📌 Creates missing category folders automatically.  
- 🛠️ Easily customizable for additional file extensions or categories.  

---

## 🛠️ Installation

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/yourusername/file-management-automation.git
   cd file-management-automation
   ```

2. **Run the script:**  
   ```bash
   python file_management.py
   ```

---

## 📂 How It Works

1. **Define the source directory**  
   - By default, the script organizes files from the `Downloads` folder. You can modify the `source_directory` variable to any directory of your choice.

2. **File Categorization:**  
   - **Images:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`  
   - **Documents:** `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`  
   - **Videos:** `.mp4`, `.mov`, `.avi`, `.mkv`  
   - **Audio:** `.mp3`, `.wav`, `.aac`  
   - **Archives:** `.zip`, `.rar`, `.tar`, `.gz`  
   - **Others:** All other unlisted file types  

3. **Execution:**  
   - The script scans the directory and moves files into their corresponding folders.
   - If the required folders do not exist, they are created automatically.

---

## 🎯 Customization

- Modify the `file_categories` dictionary in `file_management.py` to add or remove file types as needed.
- Change `source_directory` to specify a different directory for organization.

---

## 🤝 Contributing

Want to improve this script? Fork the repository, make your changes, and submit a Pull Request!

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

_“Automate the boring stuff and keep your files neat!”_ 🚀
```
