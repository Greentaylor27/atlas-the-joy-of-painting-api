import csv
import os
import os.path
import re
from datetime import datetime

class JoysOfPaintingCleanUp:

    def __init__(self, folder_path):
        self.folder_path = folder_path

    def load_csv(self, file_name):
        file_path = os.path.join(self.folder_path, file_name)
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            return list(reader)

    def clean_date(self, date_str):
        try:
            date_obj = datetime.strptime(date_str, "%B %d %Y")
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            return date_str

    def clean_episode(self):
        clean_list = []
        data = self.load_csv('The Joy Of Painting - Episode Dates')

        for row in data:
            row_string = "".join(row)

            match_title = re.search(r"^(.*?)(?=\()", row_string)
            match_date = re.search(r"\(([A-Za-z]+\s+\d{1,2}\s+\d{4})\)", row_string)

            title = ""
            formatted_date = ""
            note = ""

            if match_title:
                title = match_title.group(1).strip()

            if match_date:
                raw_date = match_date.group(1)
                formatted_date = self.clean_date(raw_date)

                end_of_date_indx = match_date.end()
                after_date_text = row_string[end_of_date_indx:].strip()

                if after_date_text:
                    note = after_date_text

            if title:
                clean_list.append([title, formatted_date, note])

        return clean_list

    # def clean_subject(self):
    # def clean_color(self):

    def export_episode(self):

        output_file = os.path.join(self.folder_path, 'cleaned_episodes.csv')
        header = ['Episode', 'Date (y-m-day)', 'Notes (optional)']

        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(self.clean_episode())

        print('CSV should have been sucessfully written')

    # def export_subject(self):
    # def export_color(self):
