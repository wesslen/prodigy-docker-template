import srsly
import os
from dotenv import load_dotenv

# Make sure variables from `.env` are available via `os.environ`
load_dotenv()

# Load configuration file
config = srsly.read_json("prodigy.json")

# Ensure postgres variables in `prodigy.json`
config["db_settings"]["postgresql"]["user"] = os.environ['POSTGRES_USER']
config["db_settings"]["postgresql"]["password"] = os.environ['POSTGRES_PWD']
config["db_settings"]["postgresql"]["host"] = os.environ['POSTGRES_HOST']
config["db_settings"]["postgresql"]["port"] = os.environ['POSTGRES_PORT']
config["db_settings"]["postgresql"]["dbname"] = os.environ['POSTGRES_DB_NAME']

# Write configuration file
config = srsly.write_json("prodigy.json", config)