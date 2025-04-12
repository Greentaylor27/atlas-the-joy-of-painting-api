import csv
import os
import os.path
import re
from datetime import datetime
from ParentClass import JoyOfCoding

class JoysOfPaintingCleanUp(JoyOfCoding):

    def __init__(self, folder_path):
        super().__init__(folder_path)


    def clean_date(self, date_str):
        try:
            date_obj = datetime.strptime(date_str, "%B %d %Y")
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            return date_str

    def clean_episode(self, episode_ids):
        clean_list = []
        data = self.load_csv('The Joy Of Painting - Episode Dates')

        for idx, row in enumerate(data):
            row_string = "".join(row)

            match_title = re.search(r"^(.*?)(?=\()", row_string)
            match_date = re.search(r"\(([A-Za-z]+\s+\d{1,2}\s+\d{4})\)", row_string)

            title = ""
            formatted_date = ""
            note = ""
            ep_id = episode_ids[idx] if idx < len(episode_ids) else ""

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
                clean_list.append([ep_id,title, formatted_date, note])

        return clean_list

    def clean_subject(self):
        data = self.load_csv('The Joy Of Painiting - Subject Matter')

        if not data:
            return []
        else:
            header = data[0]

        subject_matter = header[2:]

        subject_row = [[i + 1, subject] for i, subject in enumerate(subject_matter)]

        return subject_row

    def clean_color(self):
        color_hex_map = {
            'Black_Gesso': '#000000-pr', # pr for Primer
            'Bright_Red': '#FF000D',
            'Burnt_Umber': '#6E260E',
            'Dark_Sienna': '#3C1414',
            'Cadmium_Yellow': '#FDDA0D',
            'Indian_Red': '#CD5C5C',
            'Indian_Yellow': '#E3A857',
            'Liquid_Black': '#000000-pa', # pa for Paint
            'Liquid_Clear': '#00FFFFFF',
            'Midnight_Black': '#0D0D0D',
            'Phthalo_Blue': '#000F89',
            'Phthalo_Green': '#123524',
            'Prussian_Blue': '#003153',
            'Sap_Green': '#507D2A',
            'Titanium_White': '#E4E4E4',
            'Van_Dyke_Brown': '#574739',
            'Yellow_Ochre': '#CC7722',
            'Alizarin_Crimson': '#E32636'
        }

        data = self.load_csv('The Joy Of Painiting - Colors Used')

        header = data[0]
        color_names = header[10:]

        cleaned_colors = []

        for name in color_names:
            name = name.strip()
            hex_code = color_hex_map.get(name)

            if hex_code:
                cleaned_colors.append([
                    hex_code,
                    name
                ])
            else:
                print(f"[WARN] No hex code found for: {name}")

        return cleaned_colors


    def export_episode(self):

        output_file = os.path.join(self.folder_path, 'cleaned_episodes.csv')
        header = ['ID', 'Episode (Title)', 'Date (y-m-day)', 'Notes (Optional)']

        episode_ids = self.extract_episode_id()
        cleaned_episode = self.clean_episode(episode_ids)

        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(cleaned_episode)

        print('cleaned_episodes.csv should have been sucessfully written')

    def export_subject(self):
        output_file = os.path.join(self.folder_path, 'cleaned_subject.csv')
        header = ['ID', 'Subject Matter']
        cleaned_subject = self.clean_subject()

        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(cleaned_subject)

        print('cleaned_subject.csv should have been sucessfully written')

    def export_color(self):
        output_file = os.path.join(self.folder_path, 'cleaned_colors.csv')
        header = ['ID', 'Color']
        cleaned_color = self.clean_color()

        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(cleaned_color)

        print('cleaned_color.csv should have been successfully written')


if __name__ == "__main__":
    cleaner = JoysOfPaintingCleanUp("CSVs")

    cleaner.export_color()
    cleaner.export_episode()
    cleaner.export_subject()
