from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from services import text_grading


class Input(BaseModel):
    context: str


app = FastAPI()


@app.post("/length")
async def length(input: Input):
    return len(input.context)


@app.post("/words")
async def words(input: Input):
    return len(input.context.split())


@app.post("/ARI")
async def ARI(input: Input):
    return text_grading.ARI(input.context)


@app.post("/FK")
async def FK(input: Input):
    return text_grading.flesch_kincaid(input.context)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
