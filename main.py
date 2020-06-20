from fastapi import FastAPI
from pydantic import BaseModel
import stanza
import os

# ASGI app variable
app = FastAPI()

# this is where our configured pipelines go, one per language
languages = os.getenv('STANZA_LANGUAGES', "en").split()
pipelines = {}

for lang in languages:
    # download to make sure we have the model
    stanza.download(lang)
    # construct pipeline
    pipelines[lang] = stanza.Pipeline(lang)

# data to be sent for analysis requests
class AnalysisRequest(BaseModel):
    text: str
    lang: str

# analysis endpoint
@app.post("/analyze")
def analyze(req: AnalysisRequest):
    # process and return resulting document as dict
    return pipelines[req.lang](req.text).to_dict()
