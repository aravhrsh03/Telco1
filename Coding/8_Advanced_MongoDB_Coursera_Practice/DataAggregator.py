import pymongo
import configparser
import os
import logging


class DataAggregator:

    def __init__(self):
        config = configparser.ConfigParser()

        ini_file_path = os.path.join(
            os.path.dirname(__file__),
            "config",
            "DataAggregator.ini"
        )

        config.read(ini_file_path)

        log_file = config["DEFAULT"]["LOG_FILENAME"]

        if not os.path.isabs(log_file):
            log_file = os.path.join(
                os.path.dirname(__file__),
                log_file
            )

        os.makedirs(
            os.path.dirname(log_file),
            exist_ok=True
        )

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )

        self.logger = logging.getLogger("DataAggregator")

        self.CONNECTION_NAME = config["MONGODB"]["CONNECTION_NAME"]
        self.CONNECTION_STRING = config["MONGODB"]["CONNECTION_STRING"]
        self.DBNAME = config["MONGODB"]["DBNAME"]
        self.USERNAME = config["MONGODB"]["USERNAME"]
        self.PASSWORD = config["MONGODB"]["PASSWORD"]
        self.SOURCE_COLLECTION = config["MONGODB"]["SOURCE_COLLECTION"]

        self.client = None
        self.db = None
        self.collection = None

    def connect_to_mongodb(self):
        try:
            self.logger.info(
                f"Connecting to MongoDB collection '{self.CONNECTION_NAME}'"
            )

            self.client = pymongo.MongoClient(
                self.CONNECTION_STRING,
                username=self.USERNAME,
                password=self.PASSWORD,
            )

            self.client.admin.command("ping")

            self.db = self.client[self.DBNAME]
            self.collection = self.db[self.SOURCE_COLLECTION]

            self.logger.info(
                f"Connected to MongoDB database '{self.DBNAME}'"
            )

            return True

        except Exception as e:
            self.logger.exception(
                f"MongoDB connection failed: {e}"
            )
            return False

    def close_mongodb(self):
        if self.client:
            self.client.close()
            self.logger.info("MongoDB connection closed")


if __name__ == "__main__":

    data_aggregator = DataAggregator()

    if data_aggregator.connect_to_mongodb():
        data_aggregator.logger.info(
            "MongoDB Connected Successfully"
        )
    else:
        data_aggregator.logger.error(
            "MongoDB Connection Failed"
        )

    data_aggregator.close_mongodb()
