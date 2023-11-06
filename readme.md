## Docker compose / beginners course

## Main course doc
- https://tinyurl.com/yc43bxn5

### How to start
- docker-compose up
  - allows you to startup both web (python FastAPI webserver) & database (PostgreSQL) services
- Insert data into database
  - Connect with tool of your choice (ex: pgAdmin) to database.
    - Credentials (from your local) are : 
      - hostname: localhost
      - port: 5432 (Postgres default)
      - db name: john
      - user: john
      - pwd: example
  - Execute queries contained in ./init.sql
- Call (GET) http://localhost:8000/books endpoint, you should have 2 books returned.

### What's to see here
- API get info from database thanks to docker-compose (default) network, 
in which containers designated by a service name ("web" & "bdd").
- So, if we were to call the API from db, we could : 
  - connect into db container (`docker exec -it {api container id} bash`)
  - exec CLI : `curl http://web:8000/books`

### useful commands (docker-compose related)
- /!\ docker-compose commands must be executed in the folder containing the docker-compose.yml file
- `docker-compose down` : stop + remove containers
- `docker-compose up` : start every services contained in docker-compose.yml
- `docker-compose log {service name}` : see logs from a service
  - ex : `docker-compose log web`
- `docker-compose log {service name} -f` : see logs from a service & keep the log command running 
(to see logs as they are generated by the API)
- `docker-compose up --build --force-recreate` : rebuild images / containers in order to be sure that
latest changes aren't being hidden by any cache.
- `docker ps` : show containers running

### notes (docker-compose related)
- There is no persisting volume for bdd service, so destroying container will lead to loss of data stored
in Postgres. (Meaning that you'll have to re-run init.sql)

### docker commands
- `docker build -t {image name} .`
  - image name : will allow you to find your containers with `docker ps`, push your image to the container registry...
  - `.` : the dot part means the context (files/folders) you want to use to build your image
  - You must run it in the folder containing the "Dockerfile". Be careful with case & space.
    - the Dockerfile must be written as is, and not : "dockerfile", "dockerfile ", "DockerFile"
- `docker run -it {image name}` :
  - `-it` part allows you to see logs interactively in your terminal. Not using it (`docker run {image name}`)
will work, but the container will run in background.
- `docker ps` : see the list of containers running
- `docker stop {container id}`
  - You can stop a container by either killing it through a `ctrl + c` (with keyboard) or `docker stop` command
    - You need to grab the container id first, with `docker ps` command.
- `docker logs {container id} -f`
  - let's say you started your container in background (or you don't find the terminal where you started it up),
you can list logs.
- `docker system prune`
  - Docker relies on (heavy) storage needs. Sometimes, following your usage of Docker, it will
consume your computer storage. You'll need to clean it up.
  - Empty (cache) data created by docker, concerning containers / images / networks
  - `docker system prune -a` : will remove also volumes

### common mistakes :
- (source files) / Dockerfile misplaced 
  - (ex: Dockerfile in src instead of being at root). Note that Dockerfile isn't always at root, 
But in our case it is.
- case : 
  - Instructions in Dockerfile must be in uppercase (ex: FROM / RUN / CMD ...)
  - "Dockerfile", not dockerfile, DockerFile, etc...
- spaces, spelling : 
  - In development, you'll need to be precise. Dev tools can help you by underlining mistakes
  - Check your syntaxes ! 
- Path to files 

### Are we good ?
You want to see if you master these basics ? Reproduce this repository 
- start up a web API + a database,
- fill database with some data,
- create an endpoint that list the data
- all of this containerised.

/!\ Presentation (slides) of this course will be communicated on monday 06/11/2023, see you !