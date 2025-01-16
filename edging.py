import os
import ctypes
import subprocess

# Define the path to the Edge application directory
edge_dir = r"C:\Program Files (x86)\Microsoft\Edge\Application"

def check_admin_privileges():
    """Check if the script is running with administrative privileges."""
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        return is_admin
    except:
        return False

def list_directory_contents(path):
    """List the contents of a directory."""
    try:
        files = os.listdir(path)
        print(f"Contents of '{path}':")
        for file in files:
            print(f" - {file}")
    except Exception as e:
        print(f"Error accessing the directory: {e}")

def open_file_in_directory(path, filename):
    """Open a file in the directory."""
    try:
        file_path = os.path.join(path, filename)
        with open(file_path, 'r') as file:
            print(file.read())
    except Exception as e:
        print(f"Error opening the file: {e}")

def main():
    print(f"Checking directory: {edge_dir}")

    if not os.path.exists(edge_dir):
        print(f"Directory does not exist: {edge_dir}")
        return

    if not check_admin_privileges():
        print("This script requires administrative privileges.")
        print("Please restart it as an administrator.")
        return

    list_directory_contents(edge_dir)

    # Example: Open a specific file (change "example.txt" to an actual file in the directory)
    file_to_open = input("Enter the name of a file to read (or press Enter to skip): ")
    if file_to_open:
        open_file_in_directory(edge_dir, file_to_open)

if __name__ == "__main__":
    main()
