from dotenv import load_dotenv
from os import path

dotenv_path = path.join(path.dirname(__file__), '.env')
load_dotenv(dotenv_path)