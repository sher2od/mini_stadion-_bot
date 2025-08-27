import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_TOKEN=os.getenv("DB_TOKEN")
    DB_HOST=os.getenv("DB_HOST")
    DB_PORT=os.getenv("DB_PORT")
    DB_PASSWORD=os.getenv("DB_PASSWORD")
    DB_NAME=os.getenv("DB_NAME")

config = Config()
