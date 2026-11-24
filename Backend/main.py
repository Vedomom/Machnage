import uvicorn

if __name__ == "__main__":
    uvicorn.run(app="src.app:app", reload=True)