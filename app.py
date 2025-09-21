from fastapi import FastAPI
from controller import items,users,admin

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)
app.include_router(admin.router)

@app.get("/") # GET /
def root():
    return {"message": "Hello World"}