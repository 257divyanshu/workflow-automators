# A simple script to batch rename image files in a folder to a specific format.
# Usage: python simple_renamer.py <keyword> --path <folder_path>

import os
import argparse

def rename_images_sequentially(keyword, folder_path="."):
    """
    Batch renames image files in a directory to the format 'keyword_XX.ext'.

    Args:
        keyword (str): The base name for the files.
        folder_path (str): The path to the directory containing the images.
                           Defaults to the current directory.
    """
    # Ensure the provided path is a valid directory
    if not os.path.isdir(folder_path):
        print(f"❌ Error: The path '{folder_path}' is not a valid directory.")
        return

    print(f"🔍 Scanning folder: {os.path.abspath(folder_path)}")
    print(f"📝 Renaming files with keyword: '{keyword}'")
    print("-" * 50)

    # A counter for numbering the files
    counter = 1
    
    # A list of common image file extensions to look for
    supported_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    
    # Sort the files to ensure a consistent renaming order
    try:
        files_in_directory = sorted(os.listdir(folder_path))
    except FileNotFoundError:
        print(f"❌ Error: Could not access the directory '{folder_path}'.")
        return

    for filename in files_in_directory:
        # Check if the file has one of the supported image extensions
        if filename.lower().endswith(supported_extensions):
            # Get the original file extension (e.g., '.png')
            file_extension = os.path.splitext(filename)[1]
            
            # Create the new filename, padding the number with a leading zero if needed (e.g., 01, 02)
            new_filename = f"{keyword}_{counter:02d}{file_extension}"
            
            # Get the full old and new file paths
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            try:
                os.rename(old_path, new_path)
                print(f"✓ Renamed '{filename}' to '{new_filename}'")
                counter += 1 # Increment the counter for the next file
            except Exception as e:
                print(f"❌ Could not rename '{filename}'. Error: {e}")

    print("-" * 50)
    print(f"✨ Done! Successfully renamed {counter - 1} files.")

def main():
    """Parses command-line arguments and runs the renaming function."""
    parser = argparse.ArgumentParser(
        description="Batch rename image files in a folder to 'keyword_01', 'keyword_02', etc.",
        epilog="Example: python simple_renamer.py my_vacation --path ./photos"
    )
    
    parser.add_argument("keyword", help="The keyword to use as the base for new filenames.")
    
    parser.add_argument("--path", default=".", help="The path to the folder containing the images. Defaults to the current directory.")
    
    args = parser.parse_args()
    
    rename_images_sequentially(args.keyword, args.path)

if __name__ == "__main__":
    main()
