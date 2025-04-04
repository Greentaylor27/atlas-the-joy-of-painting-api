from Cleanup import JoysOfPaintingCleanUp

if __name__ == "__main__":
    cleaner = JoysOfPaintingCleanUp("CSVs")
    cleaner.load_csv("The Joy Of Painiting - Colors Used")
    cleaner.clean_episode()

    cleaner.export_episode()
