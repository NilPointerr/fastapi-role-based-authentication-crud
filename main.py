from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import MYSQL_API
from config import DATABASE_CONFIG
from router import user, auth_routes
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database connection on startup
    db = MYSQL_API(**DATABASE_CONFIG)
    print('Creating tables...')
    db.create_tables()
    
    yield  
    
    # Cleanup logic on shutdown (if needed)
    # db.close_connection()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(auth_routes.router, prefix="/auth")
app.include_router(user.router, prefix="/users")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
