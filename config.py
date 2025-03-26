import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read API key and database path
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH")
