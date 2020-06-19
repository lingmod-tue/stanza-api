from fastapi import FastAPI
from pydantic import BaseModel
import stanza
import os

# ASGI app variable
app = FastAPI()

# this is where our configured pipelines go, one per language
pipelines = {}
languages = None
if 'STANZA_LANGUAGES' in os.environ.keys():
    languages = os.environ['STANZA_LANGUAGES'].split()
else:
    # fallback
    languages = ['en', 'de', 'pt']

def setup_lang(lang: str):
    # download to make sure we have the model
    stanza.download(lang)
    # construct pipeline
    pipelines[lang] = stanza.Pipeline(lang)
    return f"Successfully set up model for {lang}!"

for lang in languages:
    setup_lang(lang)

# data to be sent for analysis requests
class AnalysisRequest(BaseModel):
    text: str
    lang: str


@app.post("/analyze")
def analyze(req: AnalysisRequest):
    # process and return resulting document as dict
    return pipelines[req.lang](req.text).to_dict()
