# Bulk File Renamer - app.py

## Overview

This Python script (`app.py`) is developed by **Hina** and allows users to **bulk rename files** in a specified directory using various customization options such as adding prefixes, suffixes, replacing text, and changing letter case.

## Features

- Add a **prefix** to filenames.
- Add a **suffix** to filenames.
- Replace specific text in filenames.
- Convert filenames to **lowercase** or **uppercase**.
- Ensures no duplicate filenames exist.
- Skips renaming if the filename remains unchanged.

## Requirements

- Python 3.x
- OS module (built-in in Python)

## Usage

Run the script from the terminal or command prompt:

```sh
python app.py
```

The script will prompt for user input:

1. **Enter the directory path:** *(Folder where the files are located)*
2. **Enter a prefix:** *(Text to add at the beginning of filenames, leave blank for none)*
3. **Enter a suffix:** *(Text to add at the end, before the extension, leave blank for none)*
4. **Enter text to replace:** *(Specific text to find in filenames, leave blank for none)*
5. **Enter new text to replace with:** *(New text to replace the old one, leave blank for none)*
6. **Convert filenames to lowercase? (y/n)**
7. **Convert filenames to uppercase? (y/n)**

## Example Scenarios

### **1. Adding a Prefix and Suffix**

#### **Before:**

```
file1.txt
document.pdf
```

#### **User Input:**

```
Prefix: new_
Suffix: _final
```

#### **After:**

```
new_file1_final.txt
new_document_final.pdf
```

### **2. Replacing Text in Filenames**

#### **Before:**

```
project_v1.txt
project_v2.txt
```

#### **User Input:**

```
Replace 'project' with 'task'
```

#### **After:**

```
task_v1.txt
task_v2.txt
```

### **3. Convert Filenames to Lowercase**

#### **Before:**

```
Report.DOCX
MyFile.PDF
```

#### **User Selects 'Convert to Lowercase'**

#### **After:**

```
report.docx
myfile.pdf
```

## Notes

- The script **does not rename directories**, only files.
- If a file with the new name **already exists**, renaming is skipped.
- If both lowercase and uppercase options are selected, **uppercase takes priority**.

## License

This project is open-source and free to use.

---

🚀 *Happy Renaming! - Hina*
