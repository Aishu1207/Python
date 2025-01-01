import os
import shutil

# Define file type categories
FILE_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".exe"],
    "Others": []
}

def organize_files(directory):
    """
    Organizes files in the given directory into categorized subfolders.
    """
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return
    
    # Create subfolders if they don't exist
    for category in FILE_CATEGORIES.keys():
        folder_path = os.path.join(directory, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Move files into appropriate folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get file extension
        _, file_extension = os.path.splitext(filename)
        
        # Find the category for the file
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension.lower() in extensions:
                shutil.move(file_path, os.path.join(directory, category, filename))
                print(f"Moved: {filename} -> {category}")
                moved = True
                break
        
        # If no matching category, move to "Others"
        if not moved:
            shutil.move(file_path, os.path.join(directory, "Others", filename))
            print(f"Moved: {filename} -> Others")

    print("File organization complete!")

if __name__ == "__main__":
    # Change 'YOUR_DIRECTORY_PATH' to the directory you want to organize
    directory_to_organize = r"C:\Users\91932\Desktop"
    organize_files(directory_to_organize)

