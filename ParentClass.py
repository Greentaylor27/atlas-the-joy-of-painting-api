import os
import csv

class JoyOfCoding:

    def __init__(self, folder_path):
        self.folder_path = folder_path

    def load_csv(self, file_name):
        file_path = os.path.join(self.folder_path, file_name)
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            return list(reader)
        
    def extract_episode_id(self):
        data = self.load_csv('The Joy Of Painiting - Colors Used')
        header, *rows = data

        episode_ids = []

        for row in rows:
            season = int(row[4])
            episode = int(row[5])

            id = f"S{season:02}E{episode:02}"
            episode_ids.append(id)

        return episode_ids
