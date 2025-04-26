# 🎨 Atlas: The Joy of Painting API
This project is an exploration of ETL (Extract, Transform, Load) processes, data modeling, and backend architecture. It’s centered around building an API to organize and explore metadata from Bob Ross’s The Joy of Painting episodes.

Though the project is unfinished, it taught me a lot about data pipelines, database design, and pivoting architectures mid-development.

## 🧩 What This Project Does
-Extracts data from multiple CSV files

-Transforms and cleans that data into a normalized structure

-(Intended to) Load data into a PostgreSQL database

-Provides a backend (in progress) for filtering and querying the dataset

## 🗺 ERD (Entity Relationship Diagram)
Here’s the [ERD diagram](./screenshots/ERD for Joys of painting project - Imgur.png) I created to guide the relational structure of the data.

## ⚙️ Project Steps
These scripts represent the steps of the ETL process:

1. Cleanup.py

- Extracts and transforms raw CSV data

- Normalizes the structure

- Outputs cleaned CSVs

2. Connect.py

- Builds junction tables for many-to-many relationships

- Creates intermediate CSVs to map associations

3. Import.py (planned but incomplete)

- Intended to import all CSVs into a PostgreSQL database

- Switched architectures mid-project and this step was never finalized

4. API backend (partially implemented)

- Planned to use Node.js/Express or Python to serve a RESTful API

- Filter and return painting metadata based on user queries

## 🚧 Challenges & Roadblocks
This project didn’t make it to full deployment, but here's where I hit friction (and what I learned):

- 🧱 Database architecture
Originally planned for PostgreSQL, then reconsidered for MongoDB midstream — a reminder to plan ahead!

- 📊 Entity design
Designing the ERD took serious thought and revealed how tricky many-to-many relationships can be in normalized databases.

- 🔁 Data pipeline complexity
Juggling CSVs, transformation logic, and relational mappings was a great intro to real-world ETL headaches.

## 🙋‍♂️ About the Developer
Hey, I’m Taylor Green – backend-focused full-stack developer with a love for clean data, great documentation, and miniatures on the weekend.

🔗 Connect with me:

[GitHub](https://github.com/Greentaylor27)

[LinkedIn](https://www.linkedin.com/in/greentaylor27/)

[Portfolio](https://github.com/Greentaylor27?tab=repositories)

## 🧠 Future Plans

- Complete the import step for PostgreSQL or switch fully to a NoSQL schema

- Finish the Express.js backend and expose filtering endpoints

- Deploy the API and build a simple frontend to explore the dataset

