# Friendo_Site
A website for managing Friendo bot and the Friendo API

### start docker
`docker-compose -f docker-compose.yml -f docker-compose.dev.yml up`

### Public Dev Server
At the moment the `docker-compose.dev.yml` debug variable must be edited for the dev deployment.
Use the dev deployment command in detached mode in order to run the dev server on port 8000 
(This is where apache is redirecting dev.friendo.us). This should not require editing the `.env` file debug
as that one is not used in dev mode.
