from fastapi import FastAPI

app = FastAPI(title="Ticket Booking")


@app.get("/")
def home():
    return {"status": "True", "messgae": "Ticket Booking System"}
