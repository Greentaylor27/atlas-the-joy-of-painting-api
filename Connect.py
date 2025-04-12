from ParentClass import JoyOfCoding

class JoyOfPaintingConnect(JoyOfCoding):
    def __init__(self, folder_path):
        super().__init__(folder_path)

    def connect_episode_to_color(self):
        color_meta_data = self.load_csv('The Joy Of Painiting - Colors Used')
        header, *rows = color_meta_data

        

        for rows in color_meta_data:
            print(rows[10:])

    def connect_episode_to_subject(self):
        pass


if __name__ == "__main__":
    Connecter = JoyOfPaintingConnect("CSVs")

    Connecter.connect_episode_to_color()
