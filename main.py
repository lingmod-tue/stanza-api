from fastapi import FastAPI
from pydantic import BaseModel
import stanza
import os
import sys

# ASGI app variable
app = FastAPI()

# this is where our configured pipelines go, one per language
languages = os.getenv('STANZA_LANGUAGES', "en").split()
packages = os.getenv('STANZA_PACKAGES', 'default').split()

if len(packages) != len(languages):
    packages = ['default' for _ in languages]

pipelines = {}

for lang, pack in zip(languages, packages):
    # download to make sure we have the model
    stanza.download(lang, package=pack)
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
