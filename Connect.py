from ParentClass import JoyOfCoding
import os
import csv

class JoyOfPaintingConnect(JoyOfCoding):
    def __init__(self, folder_path):
        super().__init__(folder_path)

    def build_color_map(self):
        data = self.load_csv('clean_color.csv')
        header, *rows = data
        return {row[1].strip(): row[0] for row in rows}

    def connect_episode_to_color(self):
        color_meta_data = self.load_csv('The Joy Of Painiting - Colors Used')
        header, *rows = color_meta_data
        color_name = header[10:]

        episode_ids = self.extract_episode_id()

        output_row = []

        for episode_id, row in zip(episode_ids, rows):
            binary_flags = header[10:]

            for indx, val in enumerate(binary_flags):
                if val == '1':
                    color_name = color_name[indx].strip()
                    color_id = self.build_color_map.get(color_name)
                    if color_id:
                        output_row.append([episode_id, color_id])
                    else:
                        print(f"[WARN] color not found in map: {color_name}")
        return output_row

    def connect_episode_to_subject(self):
        pass

    def export_EpisodeColor(self):
        output_file = os.path.join(self.folder_path, 'EpisodeColor.csv')
        header = ['episode_id', 'color_id']
        episodecolor = self.connect_episode_to_color()

        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerows(episodecolor)

        print('EpisodeColor.csv should have been successfully written')


if __name__ == "__main__":
    Connecter = JoyOfPaintingConnect("CSVs")

    Connecter.export_EpisodeColor()
