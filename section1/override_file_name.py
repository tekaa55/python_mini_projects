import os
from datetime import datetime

# name of the directory where the files are to rename
directory = 'files'
filenames = os.listdir(directory)

for filename in filenames:
    # currently only .txt files are considered
    if not filename.endswith('.txt'):
        print('Only files with .txt extension are considered in this exercise')
        continue

    raw_filename = filename.replace('.txt', '')
    filepath = os.path.join(directory, filename)
    today = datetime.today().strftime('%Y-%m-%d')
    new_filename = f'{raw_filename}-{today}.txt'
    new_filepath = os.path.join(directory, new_filename)

    print(f'Renaming {filepath} to {new_filepath}')

    os.rename(filepath, new_filepath)
