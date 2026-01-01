import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import bcrypt
import uuid
from datetime import datetime, timezone
import os
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).parent.parent / "backend"
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ['MONGO_URL']
db_name = os.environ['DB_NAME']

async def create_admin():
    client = AsyncIOMotorClient(mongo_url)
    db = client[db_name]
    
    existing_admin = await db.users.find_one({"username": "admin"}, {"_id": 0})
    if existing_admin:
        print("Admin user already exists!")
        client.close()
        return
    
    password_hash = bcrypt.hashpw("admin123".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    admin_doc = {
        "id": str(uuid.uuid4()),
        "username": "admin",
        "password_hash": password_hash,
        "mobile_number": "9999999999",
        "role": "admin",
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    
    await db.users.insert_one(admin_doc)
    print("Admin user created successfully!")
    print("Username: admin")
    print("Password: admin123")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(create_admin())
