from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class PromptData(BaseModel):
    prompt: str


@app.post("/generate")
def generate_response(data: PromptData):

    prompt = data.prompt

    response = "AI enables computers to perform tasks that normally require human intelligence."

    return {
        "prompt": prompt,
        "response": response
    }