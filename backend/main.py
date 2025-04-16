from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/hello")
def read_hello():
    return {"message": "Hello, MyWallet!"}
