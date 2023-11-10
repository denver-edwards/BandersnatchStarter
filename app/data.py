from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    # Load environment variables and connect to the database
    load_dotenv()
    DB_URL = getenv("DB_URL")
    db = MongoClient(DB_URL, tlsCAFile=where())["Database"]

    def __init__(self):
        self.collection = self.db["collection"]

        # If the collection is empty, seed it with initial data
        if self.count() == 0:
            self.seed(2048)

    def seed(self, amount):
        monster_list = []

        for num in range(amount):
            monster_list.append(Monster().to_dict())

        self.collection.insert_many(monster_list)

    def reset(self):
        # Delete all documents in the collection
        self.collection.delete_many({})

    def count(self) -> int:
        # Return the number of documents in the collection
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        # Convert the collection documents to a pandas DataFrame
        docs = self.collection.find({})
        return DataFrame(list(docs))

    def html_table(self) -> str:
        # Generate an HTML table representation of the collection data
        if self.count() == 0:
            return None  # Return None if the collection is empty
        else:
            return self.dataframe().to_html(index=True, header=True,
                                            columns=["Name", "Type",
                                                     "Level", "Rarity",
                                                     'Damage', 'Health',
                                                     "Energy",
                                                     "Sanity",
                                                     "Timestamp"])
