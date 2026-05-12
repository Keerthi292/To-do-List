from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "todo_db")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "todos")

if not MONGO_URI:
    raise ValueError("MONGO_URI is missing in .env file")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
todos_collection = db[COLLECTION_NAME]

def serialize_todo(todo):
    return {
        "id": str(todo["_id"]),
        "text": todo.get("text", ""),
        "completed": todo.get("completed", False),
        "important": todo.get("important", False)
    }

@app.get("/")
async def home():
    return {"message": "FastAPI MongoDB Todo Backend Running"}

@app.get("/todos")
async def get_todos():
    todos = list(todos_collection.find().sort("_id", -1))
    return [serialize_todo(todo) for todo in todos]

@app.post("/todos")
async def create_todo(request: Request):
    data = await request.json()

    text = data.get("text", "").strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")

    new_todo = {
        "text": text,
        "completed": data.get("completed", False),
        "important": data.get("important", False)
    }

    result = todos_collection.insert_one(new_todo)
    created_todo = todos_collection.find_one({"_id": result.inserted_id})

    return serialize_todo(created_todo)

@app.put("/todos/{todo_id}")
async def update_todo(todo_id: str, request: Request):
    data = await request.json()

    text = data.get("text", "").strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text is required")

    if not ObjectId.is_valid(todo_id):
        raise HTTPException(status_code=400, detail="Invalid todo id")

    existing_todo = todos_collection.find_one({"_id": ObjectId(todo_id)})
    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    updated_data = {
        "text": text,
        "completed": data.get("completed", False),
        "important": data.get("important", False)
    }

    todos_collection.update_one(
        {"_id": ObjectId(todo_id)},
        {"$set": updated_data}
    )

    updated_todo = todos_collection.find_one({"_id": ObjectId(todo_id)})
    return serialize_todo(updated_todo)

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str):
    if not ObjectId.is_valid(todo_id):
        raise HTTPException(status_code=400, detail="Invalid todo id")

    existing_todo = todos_collection.find_one({"_id": ObjectId(todo_id)})
    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    todos_collection.delete_one({"_id": ObjectId(todo_id)})
    return {"message": "Todo deleted successfully"}

@app.delete("/todos")
async def delete_all_todos():
    result = todos_collection.delete_many({})
    return {"message": f"{result.deleted_count} todos deleted successfully"}