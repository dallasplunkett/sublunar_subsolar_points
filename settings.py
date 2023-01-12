import os
from dotenv import load_dotenv

load_dotenv('.env')

URL = os.environ['URL']
HOST = os.environ['HOST']
ADMIN_USER = os.environ['ADMIN_USER']
PASSWORD = os.environ['PASSWORD']
DATABASE = os.environ['DATABASE']