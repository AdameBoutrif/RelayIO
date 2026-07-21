from backend.app_relay.database import SessionLocal

db = SessionLocal()

print("Connected Succesfully!")

db.close()