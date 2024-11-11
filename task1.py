import os

def print_file_paths(directory_name, filename):
    """
    Recursively search for and print paths of a specified file in a given directory and its subdirectories.

    Args:
        directory_name (str): The directory path where the search starts.
        filename (str): The name of the file to search for.

    Returns:
        bool: True if at least one file was found, otherwise False.
    """
    if not os.path.isdir(directory_name):
        print(f"Error: '{directory_name}' is not a valid directory.")
        return False

    found_files = False
    try:
        for file in os.listdir(directory_name):
            full_path = os.path.join(directory_name, file)
            if filename == file:
                print(full_path)
                found_files = True
            elif os.path.isdir(full_path):
                if print_file_paths(full_path, filename):
                    found_files = True
    except PermissionError:
        print(f"Permission denied: '{directory_name}'")
    except Exception as e:
        print(f"Error accessing '{directory_name}': {e}")

    return found_files

# Running the function
directory_to_search = '/Users/misc/Documents/Semester'
filename_to_find = 'script.js'
if not print_file_paths(directory_to_search, filename_to_find):
    print("No files found")
