from typing import Union
import uvicorn

from fastapi import Request, FastAPI
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/GetPractice")
def read_item(name, intensity,agility):
    
    return rf"Pictcher's data: {name}, {intensity}, {agility}"



@app.post("/PostPractice")
async def get_body(request: Request):
    print(request)
    #clientDict= await request.body()
    clientDict= await request.json()
    return clientDict["name"]+" Loves CT! Taiwan NO.1"



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)