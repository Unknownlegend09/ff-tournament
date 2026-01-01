import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import bcrypt
import uuid
from datetime import datetime, timezone

async def create_admin():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    db = client["test_database"]
    
    # Delete existing Legend admin if exists
    await db.users.delete_one({"username": "Legend"})
    
    password_hash = bcrypt.hashpw("thelegend5703".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    admin_doc = {
        "id": str(uuid.uuid4()),
        "username": "Legend",
        "password_hash": password_hash,
        "mobile_number": "9999999999",
        "role": "admin",
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    
    await db.users.insert_one(admin_doc)
    print("✓ Legend admin created successfully!")
    print("  Username: Legend")
    print("  Password: thelegend5703")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(create_admin())
