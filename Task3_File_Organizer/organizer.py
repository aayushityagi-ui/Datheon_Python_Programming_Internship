
import os
import shutil
from pathlib import Path

# File extension categories
FILE_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".webm"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".php"],
}


def get_category(file_extension):
    """Return a folder name based on the file extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category

    return "Others"


def get_unique_path(destination):
    """Avoid overwriting files with the same name."""
    if not destination.exists():
        return destination

    base_name = destination.stem
    extension = destination.suffix
    parent = destination.parent
    counter = 1

    while True:
        new_name = f"{base_name}_{counter}{extension}"
        new_path = parent / new_name

        if not new_path.exists():
            return new_path

        counter += 1


def organize_files(folder_path):
    """Organize files into category folders."""

    folder = Path(folder_path)

    if not folder.exists():
        print("Error: The folder does not exist.")
        return

    if not folder.is_dir():
        print("Error: The given path is not a folder.")
        return

    moved_count = 0
    skipped_count = 0
    error_count = 0

    print("\nStarting File Organizer...")
    print(f"Target folder: {folder}")

    try:
        files = list(folder.iterdir())
    except PermissionError:
        print("Error: Permission denied while reading the folder.")
        return

    for file in files:

        # Skip directories
        if not file.is_file():
            continue

        # Detect category
        category = get_category(file.suffix)

        # Create category folder
        destination_folder = folder / category

        try:
            destination_folder.mkdir(exist_ok=True)

            # Prevent moving files into themselves
            destination = destination_folder / file.name

            # Handle duplicate filenames
            destination = get_unique_path(destination)

            # Move file safely
            shutil.move(str(file), str(destination))

            print(f"Moved: {file.name} -> {category}/{destination.name}")
            moved_count += 1

        except PermissionError:
            print(f"Permission denied: {file.name}")
            error_count += 1

        except (OSError, shutil.Error) as error:
            print(f"Error moving {file.name}: {error}")
            error_count += 1

    # Final summary
    print("\n========== ORGANIZATION SUMMARY ==========")
    print(f"Files moved successfully : {moved_count}")
    print(f"Files skipped          : {skipped_count}")
    print(f"Errors                : {error_count}")
    print("File organization completed!")
    print("=====================================")


def main():
    print("===================================")
    print("   AUTOMATED FILE ORGANIZER")
    print("===================================")

    folder_path = input("Enter the folder path to organize: ").strip()

    # Remove quotes if the user pastes a path from Windows Explorer
    folder_path = folder_path.strip('"').strip("'")

    if not folder_path:
        print("No folder path entered.")
        return

    organize_files(folder_path)


# Run the program
if __name__ == "__main__":
    main()
