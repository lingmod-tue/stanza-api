# stanza-api
FastAPI-based web-service to the [Stanford Stanza NLP toolkit](https://github.com/stanfordnlp/stanza). Useful for integrating Stanza into non-Python applications.

To use, run the following (substitute languages and packages for the ones you are interested in):

`docker run --name stanza-api -e STANZA_LANGUAGES="en de" [STANZA_PACKAGES="partut default"] -d -p 8000:80 ramonziai/stanza-api`

- `STANZA_PACKAGES` is optional. If provided, number of packages must match the number of languages. Use `default` if package for corresponding language does not need to be 
specified.

After that, the API is available at localhost on port 8000 once language packages have finished downloading (check status with `docker logs stanza-api`). Check out the FastAPI docs at 
http://localhost:8000/docs to see what endpoints are available. You can stop the container using `docker stop stanza-api` and start it again with `docker start stanza-api`.
