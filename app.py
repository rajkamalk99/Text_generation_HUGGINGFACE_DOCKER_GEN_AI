from fastapi import FastAPI
from transformers import pipeline


## create a new FASTAPI app instance
app = FastAPI()

pipe = pipeline("text2text-generation", model="google/flan-t5-small")

@app.get("/")
def home():
    return {"message": "Hello world"}

@app.get("/generate")
def generate(text:str):

    # use the pipelien to generate text from the given input

    output= pipe(text)

    #return the generated output in JSON format
    return {"output": output[0]["generated_text"]}