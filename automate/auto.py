import shutil
from pathlib import Path
import json

# Function to move a file to a specified destination
def move_file(file, destination):
    try:
        if not destination.exists():
            destination.mkdir(parents=True, exist_ok=True)
        shutil.move(file, destination)
    except shutil.Error as e:
        print(e)


def sort_folder(folder_path):
    # Load the categories and extensions from the config file
    with open('config.json', encoding='utf-8') as f:
        categories = json.load(f)

    extensions_map = {}
    # Create a mapping of extensions to folder names
    for category in categories:
        folder_name = category['name']
        for extension in category['extensions']:
            extensions_map[extension] = folder_name

    for file in folder_path.iterdir():
        if file.is_file() and not file.name.startswith('.'):
            destination = extensions_map.get(file.suffix, 'Other')
            move_file(file, file.parent.joinpath(destination))


if __name__ == '__main__':
    # Get the user's home directory and Downloads folder path
    home_directory = str(Path.home())
    downloads_path = Path(f'{home_directory}/Downloads')

    # Sort the files in the Downloads folder
    sort_folder(downloads_path)