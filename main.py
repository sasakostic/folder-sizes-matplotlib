import os
import matplotlib.pyplot as plt

FOLDER_PATH = "D:/.NET"

def get_directory_size(directory_path):
    directory_size = 0
    for directory_path, directory_names, file_names in os.walk(directory_path):
        for file_ in file_names:
            try:
                file_path = os.path.join(directory_path, file_)
                directory_size += os.path.getsize(file_path)
            except Exception:
                pass
    return directory_size

def get_subfolder_sizes(root_path):
    subfolder_sizes = {}        
    for folder_name in os.listdir(root_path):
        full_path = os.path.join(root_path, folder_name)
        if os.path.isdir(full_path):
            directory_size = get_directory_size(full_path)
            if directory_size > 0:
                subfolder_sizes[folder_name] = directory_size
    return subfolder_sizes

def plot_folder_sizes(folder_sizes_dict):
    labels = list(folder_sizes_dict.keys())
    folder_sizes = list(folder_sizes_dict.values())

    folder_sizes_mb = [size_ / (1024 * 1024) for size_ in folder_sizes]

    plt.figure(figsize=(8, 8))
    plt.pie(folder_sizes_mb, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Folder Sizes (MB)')
    plt.axis('equal')
    plt.show()

if os.path.exists(FOLDER_PATH):
    folder_sizes = get_subfolder_sizes(FOLDER_PATH)
    if folder_sizes:
        plot_folder_sizes(folder_sizes)
    else:
        print("No directories with files.")
else:
    print("Path doesn't exist.")
