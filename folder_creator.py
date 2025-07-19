import os
import sys
import argparse

def create_folders(folder_prefix, num_folders, base_path="."):
    """
    Create numbered subfolders in the specified directory.
    
    Args:
        folder_prefix (str): The prefix for folder names (e.g., "chapter")
        num_folders (int): Number of folders to create
        base_path (str): Base directory where folders will be created (default: current directory)
    
    Returns:
        list: List of created folder paths
    """
    created_folders = []
    
    # Get the current working directory name to extract module number
    current_dir = os.path.basename(os.path.abspath(base_path))
    
    # Extract module number from directory name (e.g., "module05" -> "5")
    module_num = ""
    if current_dir.startswith("module"):
        module_num = current_dir.replace("module", "").lstrip("0") or "0"
    
    try:
        for i in range(1, num_folders + 1):
            if module_num:
                folder_name = f"{folder_prefix}{module_num}.{i}"
            else:
                folder_name = f"{folder_prefix}{i}"
            
            folder_path = os.path.join(base_path, folder_name)
            
            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                created_folders.append(folder_path)
                print(f"✓ Created folder: {folder_name}")
            else:
                print(f"⚠ Folder already exists: {folder_name}")
                
    except Exception as e:
        print(f"❌ Error creating folders: {e}")
        return []
    
    return created_folders

def main():
    parser = argparse.ArgumentParser(description="Create numbered subfolders in current directory")
    parser.add_argument("prefix", help="Folder name prefix (e.g., 'chapter')")
    parser.add_argument("count", type=int, help="Number of folders to create")
    parser.add_argument("--path", default=".", help="Base path (default: current directory)")
    
    args = parser.parse_args()
    
    # Validate inputs
    if args.count <= 0:
        print("❌ Number of folders must be positive")
        sys.exit(1)
    
    if not os.path.exists(args.path):
        print(f"❌ Path does not exist: {args.path}")
        sys.exit(1)
    
    print(f"Creating {args.count} folders with prefix '{args.prefix}' in: {os.path.abspath(args.path)}")
    print("-" * 50)
    
    created_folders = create_folders(args.prefix, args.count, args.path)
    
    print("-" * 50)
    print(f"✅ Successfully created {len(created_folders)} folders")

if __name__ == "__main__":
    main()