# need to import the library csv
# need to import os to read the files in the CSV folder

import csv
import os
import os.path

# make a class
class JoysOfPaintingCleanUp:

# within that class need to load whichever CSV file needs to be loaded in.
    def __init__(self, folder_path):
        self.folder_path = folder_path

# Each method with handle a different file.
    def load_csv(self, file_name):
        file_path = os.path.join(self.folder_path, file_name)
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
        print(reader)

# Each method will make the informaton uniform.

# the intention is to clean up all the data make it uniform here to update the CSV files.
