import os

# ID dict for each category.
folders = {
    'Bread': 0,
    'Dairy': 1,
    'Dessert': 2,
    'Egg': 3,
    'Fried': 4,
    'Meat': 5,
    'Noodles': 6,
    'Produce': 7,
    'Rice': 8,
    'Seafood': 9,
    'Soup': 10
}

# Dict for the number of images in each folder/category. Counted these by looking in the file explorer.
counts = {
    'train': {
        'Bread': 994,
        'Dairy': 429,
        'Dessert': 1500,
        'Egg': 986,
        'Fried': 848,
        'Meat': 1325,
        'Noodles': 440,
        'Produce': 709,
        'Rice': 280,
        'Seafood': 855,
        'Soup': 1500
    },
    'test': {
        'Bread': 362,
        'Dairy': 144,
        'Dessert': 500,
        'Egg': 327,
        'Fried': 326,
        'Meat': 449,
        'Noodles': 147,
        'Produce': 232,
        'Rice': 96,
        'Seafood': 347,
        'Soup': 500
    },
    'eval': {
        'Bread': 368,
        'Dairy': 148,
        'Dessert': 500,
        'Egg': 335,
        'Fried': 287,
        'Meat': 432,
        'Noodles': 147,
        'Produce': 231,
        'Rice': 96,
        'Seafood': 303,
        'Soup': 500
    }
}


def fix_numbers():
    """
    Adjust the file names of images in the 'test' and 'val' folders to avoid duplicate filenames found in 'train'.
    """

    # Path to local version of database
    root = 'H:\\food_db\\val'

    # Walk through all files in dataset
    for subdir, dirs, files in os.walk(root):
        for file in files:
            old_path = os.path.join(subdir, file)  # Get the original path
            category = os.path.split(subdir)[1]  # Get the category name from current sub-folder

            file_split = file.split('.')  # '123.jpg' into ['123', 'jpg']

            # Calculate which number the eval or test image should be, to be unique
            # new_number = counts['train'][category] + int(file_split[0])  # For 'test'
            new_number = counts['train'][category] + counts['test'][category] + int(file_split[0])  # For 'val'

            formatted_file = f'{new_number}.{file_split[1]}'  # Create new file name with correct number
            new_path = os.path.join(subdir, formatted_file)  # Recombine new filename with path

            print(f'{old_path}   {new_number}')  # Debug output
            os.rename(old_path, new_path)  # Rename file


def format_names():
    """
    Formats the filenames of all images to include a numerical ID at the beginning, and a standard number length.

    For example: '00_0000.jpg' is the first image in the "Bread" category.
    """

    # Path to local version of database
    root = 'H:\\food_db'

    # Walk through all files in dataset
    for subdir, dirs, files in os.walk(root):
        for file in files:
            old_path = os.path.join(subdir, file)  # Get the original path
            category = os.path.split(subdir)[1]  # Get the category name from current sub-folder

            file_split = file.split('.')  # '123.jpg' into ['123', 'jpg']
            formatted_file = f'{int(file_split[0]):04d}.{file_split[1]}'  # Add leading zeroes
            formatted_file = f'{folders[category]:02d}_{formatted_file}'  # Prepend the category number
            new_path = os.path.join(subdir, formatted_file)  # Recombine new filename with path

            print(f'{old_path}   {new_path}')  # Debug output
            os.rename(old_path, new_path)  # Rename file


if __name__ == '__main__':
    # fix_numbers()
    # format_names()
    pass
