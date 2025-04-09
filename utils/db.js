import pkg from 'mongodb';
const { MongoClient, ObjectId } = pkg;

class DBClient {
    constructor() {
        const host = process.env.DB_HOST || 'localhost';
        const port = process.env.DB_PORT || '27017';
        const database = process.env.DB_DATABASE || 'Joy_of_Painting';

        const url = `mongodb://${host}:${port}`;

        this.connected = false;
        this.client = new MongoClient(url, { useUnifiedTopology: true });

        this.client.connect()
            .then(() => {
                this.connected = true;
                this.db = this.client.db(database);
            })
            .catch((error) => {
                console.error(`Error establishing connect to DB: ${error}`)
            });
    }

    isAlive() {
        return this.connected;
    }
}

const dbClient = new DBClient;

export default dbClient;
