#!/usr/bin/env python3
"""
File Organization Automation Script

This script automatically organizes files in a specified directory by:
- File type (images, documents, videos, etc.)
- Creation date
- File size categories

Usage:
    python file_organizer.py [directory_path]
"""

import os
import shutil
import argparse
from datetime import datetime
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('file_organizer.log'),
        logging.StreamHandler()
    ]
)

class FileOrganizer:
    def __init__(self, source_dir):
        self.source_dir = Path(source_dir)
        self.file_types = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.tiff'],
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.pages'],
            'Spreadsheets': ['.xls', '.xlsx', '.csv', '.ods', '.numbers'],
            'Presentations': ['.ppt', '.pptx', '.odp', '.key'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
            'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
            'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.go'],
            'Executables': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm', '.app']
        }
    
    def get_file_category(self, file_path):
        """Determine the category of a file based on its extension."""
        extension = file_path.suffix.lower()
        for category, extensions in self.file_types.items():
            if extension in extensions:
                return category
        return 'Others'
    
    def create_organized_structure(self):
        """Create the organized folder structure."""
        organized_dir = self.source_dir / 'Organized'
        organized_dir.mkdir(exist_ok=True)
        
        # Create category folders
        for category in self.file_types.keys():
            (organized_dir / category).mkdir(exist_ok=True)
        (organized_dir / 'Others').mkdir(exist_ok=True)
        
        return organized_dir
    
    def organize_by_type(self):
        """Organize files by their type/category."""
        if not self.source_dir.exists():
            logging.error(f"Source directory {self.source_dir} does not exist!")
            return
        
        organized_dir = self.create_organized_structure()
        moved_count = 0
        
        for file_path in self.source_dir.iterdir():
            if file_path.is_file() and file_path.name != '.DS_Store':
                category = self.get_file_category(file_path)
                destination = organized_dir / category / file_path.name
                
                # Handle duplicate names
                counter = 1
                original_destination = destination
                while destination.exists():
                    name_parts = original_destination.stem, counter, original_destination.suffix
                    destination = original_destination.parent / f"{name_parts[0]}_{name_parts[1]}{name_parts[2]}"
                    counter += 1
                
                try:
                    shutil.move(str(file_path), str(destination))
                    logging.info(f"Moved {file_path.name} to {category}/")
                    moved_count += 1
                except Exception as e:
                    logging.error(f"Error moving {file_path.name}: {e}")
        
        logging.info(f"Successfully organized {moved_count} files!")
    
    def organize_by_date(self):
        """Organize files by creation date."""
        if not self.source_dir.exists():
            logging.error(f"Source directory {self.source_dir} does not exist!")
            return
        
        organized_dir = self.source_dir / 'Organized_by_Date'
        organized_dir.mkdir(exist_ok=True)
        moved_count = 0
        
        for file_path in self.source_dir.iterdir():
            if file_path.is_file() and file_path.name != '.DS_Store':
                # Get file creation date
                creation_time = datetime.fromtimestamp(file_path.stat().st_ctime)
                year_month = creation_time.strftime('%Y-%m')
                
                # Create year-month folder
                date_folder = organized_dir / year_month
                date_folder.mkdir(exist_ok=True)
                
                destination = date_folder / file_path.name
                
                # Handle duplicates
                counter = 1
                original_destination = destination
                while destination.exists():
                    name_parts = original_destination.stem, counter, original_destination.suffix
                    destination = original_destination.parent / f"{name_parts[0]}_{name_parts[1]}{name_parts[2]}"
                    counter += 1
                
                try:
                    shutil.move(str(file_path), str(destination))
                    logging.info(f"Moved {file_path.name} to {year_month}/")
                    moved_count += 1
                except Exception as e:
                    logging.error(f"Error moving {file_path.name}: {e}")
        
        logging.info(f"Successfully organized {moved_count} files by date!")
    
    def clean_empty_folders(self):
        """Remove empty folders in the source directory."""
        removed_count = 0
        for folder_path in self.source_dir.iterdir():
            if folder_path.is_dir() and not any(folder_path.iterdir()):
                try:
                    folder_path.rmdir()
                    logging.info(f"Removed empty folder: {folder_path.name}")
                    removed_count += 1
                except Exception as e:
                    logging.error(f"Error removing folder {folder_path.name}: {e}")
        
        logging.info(f"Removed {removed_count} empty folders!")

def main():
    parser = argparse.ArgumentParser(description='Organize files automatically')
    parser.add_argument('directory', nargs='?', 
                       default=str(Path.home() / 'Downloads'),
                       help='Directory to organize (default: ~/Downloads)')
    parser.add_argument('--mode', choices=['type', 'date'], default='type',
                       help='Organization mode: by type or date (default: type)')
    parser.add_argument('--clean', action='store_true',
                       help='Remove empty folders after organizing')
    
    args = parser.parse_args()
    
    organizer = FileOrganizer(args.directory)
    
    print(f"🚀 Starting file organization in: {args.directory}")
    print(f"📊 Organization mode: {args.mode}")
    
    if args.mode == 'type':
        organizer.organize_by_type()
    elif args.mode == 'date':
        organizer.organize_by_date()
    
    if args.clean:
        organizer.clean_empty_folders()
    
    print("✅ File organization complete!")
    print("📝 Check file_organizer.log for detailed information")

if __name__ == "__main__":
    main()
