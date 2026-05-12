# To-do List App

## Clone and Setup

### 1. Clone Repository
```bash
git clone https://github.com/Keerthi292/To-do-List.git
cd To-do-List
```

## System Setup

### 1. Install Requirements
- Docker & Docker Compose
- MongoDB Atlas account (create at [mongodb.com/atlas](https://mongodb.com/atlas))

### 2. Configure Database
Edit `backend/.env` and add your MongoDB Atlas connection:
```env
MONGO_URI=mongodb+srv://your_username:your_password@your-cluster.mongodb.net/
DB_NAME=todo_db
COLLECTION_NAME=todos
```

## Running Commands

### Start Application
```bash
docker compose up --build -d
```

### Stop Application
```bash
docker compose down
```

### Check Status
```bash
docker ps
docker compose logs
```

### Access Points
- **Web App**: http://localhost:8080
- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## App Usage

### Features
- Create new todos
- Mark todos as complete/incomplete  
- Mark todos as important
- View task statistics in sidebar
- Filter todos (all, active, completed)
- Delete individual todos or clear all

### How to Use
1. **Add Todo**: Type in the input field and press Enter or click Add
2. **Complete Todo**: Click the checkbox next to a todo
3. **Mark Important**: Click the star icon to mark as important
4. **Edit Todo**: Click on the todo text to edit
5. **Delete Todo**: Click the delete icon next to a todo
6. **Filter**: Use tabs to view all, active, or completed todos
7. **Clear**: Use sidebar options to clear completed or all todos
