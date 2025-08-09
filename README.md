# Automation Scripts

A collection of automation scripts to enhance daily tasks and productivity.

## 📁 File Organizer

The File Organizer is a powerful Python script that automatically organizes files in a directory based on different criteria.

### Features

#### 🗂️ Organization by File Type
Automatically categorizes files into organized folders based on their extensions:

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp`, `.tiff`
- **Documents**: `.pdf`, `.doc`, `.docx`, `.txt`, `.rtf`, `.odt`, `.pages`
- **Spreadsheets**: `.xls`, `.xlsx`, `.csv`, `.ods`, `.numbers`
- **Presentations**: `.ppt`, `.pptx`, `.odp`, `.key`
- **Videos**: `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`, `.webm`, `.m4v`
- **Audio**: `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.wma`, `.m4a`
- **Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`, `.xz`
- **Code**: `.py`, `.js`, `.html`, `.css`, `.java`, `.cpp`, `.c`, `.php`, `.rb`, `.go`
- **Executables**: `.exe`, `.msi`, `.dmg`, `.pkg`, `.deb`, `.rpm`, `.app`
- **Others**: Files that don't match any category

#### 📅 Organization by Date
Organizes files into folders based on their creation date in `YYYY-MM` format.

#### 🧹 Clean Empty Folders
Removes empty directories after organization to keep your file system tidy.

### Functions

#### Core Functions

- **`get_file_category(file_path)`**: Determines the category of a file based on its extension
- **`create_organized_structure()`**: Creates the organized folder structure with category folders
- **`organize_by_type()`**: Organizes files by their type/category into respective folders
- **`organize_by_date()`**: Organizes files by creation date into year-month folders
- **`clean_empty_folders()`**: Removes empty folders in the source directory

#### Key Features

- **Duplicate Handling**: Automatically renames files if duplicates exist (e.g., `file_1.txt`, `file_2.txt`)
- **Comprehensive Logging**: All operations are logged to `file_organizer.log` with timestamps
- **Error Handling**: Graceful error handling with detailed error messages
- **Safe Operation**: Creates organized folders without modifying original structure until files are moved

### Usage

#### Basic Usage
```bash
# Organize Downloads folder by file type (default)
python automation/file_organizer.py

# Organize a specific directory
python automation/file_organizer.py /path/to/directory
```

#### Advanced Options
```bash
# Organize by creation date
python automation/file_organizer.py --mode date

# Organize by type and clean empty folders
python automation/file_organizer.py --clean

# Combine options
python automation/file_organizer.py /path/to/directory --mode date --clean
```

#### Command Line Arguments

- **`directory`**: Directory to organize (optional, defaults to `~/Downloads`)
- **`--mode`**: Organization mode - `type` (default) or `date`
- **`--clean`**: Remove empty folders after organizing

### Example Output

When organizing files, you'll see output like:
```
🚀 Starting file organization in: /Users/username/Downloads
📊 Organization mode: type
✅ File organization complete!
📝 Check file_organizer.log for detailed information
```

The log file will contain detailed information about each file moved:
```
2025-08-09 14:23:23,416 - INFO
2025-08-09 14:23:23,417 - INFO
2025-08-09 14:23:23,418 - INFO
2025-08-09 14:23:23,419 - INFO
```

### Installation & Requirements

#### Prerequisites
- Python 3.6 or higher
- Standard library modules (no additional packages required)

#### Setup
1. Clone or download the repository
2. Navigate to the project directory
3. Run the script directly with Python

### File Structure After Organization

#### By Type
```
Original Directory/
├── Organized/
│   ├── Images/
│   ├── Documents/
│   ├── Videos/
│   ├── Audio/
│   ├── Archives/
│   ├── Code/
│   ├── Executables/
│   └── Others/
└── file_organizer.log
```

#### By Date
```
Original Directory/
├── Organized_by_Date/
│   ├── 2025-01/
│   ├── 2025-02/
│   ├── 2025-03/
│   └── ...
└── file_organizer.log
```

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd automation-scripts
   ```

2. **Run the file organizer**:
   ```bash
   python automation/file_organizer.py
   ```

3. **Check the results**:
   - View organized files in the created folders
   - Check `file_organizer.log` for detailed operation log

## 📝 Logging

All operations are logged with timestamps to `file_organizer.log` including:
- Files moved and their destinations
- Errors encountered during operations
- Summary statistics of operations performed

## 🛡️ Safety Features

- **Non-destructive**: Creates new organized folders without modifying original files
- **Duplicate protection**: Automatically handles filename conflicts
- **Error recovery**: Continues operation even if individual files fail to move
- **Comprehensive logging**: Track all operations for audit purposes

## 🔧 Customization

The script can be easily customized by modifying the `file_types` dictionary in the `FileOrganizer` class to add new categories or file extensions.

## 📋 Future Enhancements

Potential improvements and additional scripts:
- Size-based organization
- Batch file renaming utilities
- Duplicate file detection and removal
- Automated backup scripts
- System maintenance automation

---

*This automation toolkit is designed to save time and maintain organized file systems. Always backup important files before running organization scripts.*
