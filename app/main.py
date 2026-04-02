from fastapi import FastAPI
from app.routes.user import router as user_router
from app.database.database import engine, Base
from app.models.user import User  # ensures the model is imported so table gets created

app = FastAPI(
    title="Finance Backend",
    description="User Management API",
    version="1.0.0"
)

# Create all tables
Base.metadata.create_all(bind=engine)

# Include user routes
app.include_router(user_router)

@app.get("/")
def read_root():
    return {"message": "API is running"}