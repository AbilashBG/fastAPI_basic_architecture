import uvicorn

# Script to run the FastAPI app
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=9000, reload=True)
