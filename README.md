# File Organizer 📁 🐍
## Description
This project is a simple file organizer that automates the task of organizing files in a folder by moving them into subfolders based on their extensions. It´s useful for users who want to keep their directories organized effortlessly, avoiding the clutter caused by accumulating different types of files in one location.

## How it works
*Step 1*: The user places all the files they want to organize into a specific folder.

*Step 2*: When the script is executed, it identifies the files in the folder, checks each file’s extension, and creates corresponding subfolders for those extensions (if they do not already exist).

*Step 3*: The script then moves the files into the appropriate subfolders, automatically organizing the directory.

## Technologies 
- Python: the programming language used to develop the script 🐍
- `os` Module: used to navigate and manipulate the file system
- `shutil`Module: used to move files between directories

## Usage
Imagine you have a folder with the following files:
```
my_files/
├── document.pdf
├── image.jpg
├── spreadsheet.xlsx
├── script.py
```
After running the organizing script, the folder will look like this:
```
my_files/
├── PDF/
│   └── document.pdf
├── JPG/
│   └── image.jpg
├── XLSX/
│   └── spreadsheet.xlsx
├── PY/
│   └── script.py
```
## How to use
1. Clone this repo
```
git clone https://github.com/carolfons/file-organizer.git
```
2. Navigate to the project directory:
```
cd file-organizer
```
3. Create a folder and name it `pasta-exemplo` and place the files you want to organize
4. Run the `organizer.py` script
```
python src/organizer.py
```
5. Done. Now check the `pasta-exemplo/` to see your files organized into subfolders
