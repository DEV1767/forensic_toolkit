from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = None
db = None
users_collection = None
reports_collection = None

if not MONGO_URI:
    print("⚠️ MONGO_URI not found. Please add it to .env file.")
else:
    try:
        client = MongoClient(MONGO_URI)
        client.admin.command('ping')
        print("✅ MongoDB Connected Successfully")
        db = client["audio_notary"]
        users_collection = db["users"]
        reports_collection = db["reports"]
    except Exception as e:
        print(f"❌ MongoDB Connection Failed: {e}")