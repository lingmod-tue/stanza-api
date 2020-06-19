# stanza-api
FastAPI-based web-service to the [Stanford Stanza NLP toolkit](https://github.com/stanfordnlp/stanza). Useful for integrating Stanza into non-Python applications.

To use, run the following (substitute languages for the ones you are interested in):

`docker run --name stanza-api -e STANZA_LANGUAGES="en de" -d -p 8000:80 ramonziai/stanza-api`

After that, the API is available at localhost on port 8000. Check out the FastAPI docs at http://localhost:8000/docs to see what endpoints are available. You can stop the container using `docker stop stanza-api` and start it again with `docker start stanza-api`.
