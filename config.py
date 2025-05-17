from dotenv import load_dotenv
import os

load_dotenv()

MYNAVI_EMAIL = os.getenv("MYNAVI_EMAIL")
MYNAVI_PASSWORD = os.getenv("MYNAVI_PASSWORD")