# BOOKS MANAGER
### Doc version : v1 - 06/11/2023
## Project description
Create, list... books for Amazon.

## Technical info / folder architecture
- infra : every files linked to deployment in test/production (devops only.)
- src : source code
- ...

## Prerequisites
- Docker
- docker-compose (Install Docker Desktop, it's easier ;) )
- pgAdmin (or else) : read data in postgres
- Python 3.13

## How to dev
- Start API + Database : 
  - `docker-compose up` (API will be reloaded when files are edited)
    - API local address : http://localhost:8000
    - Route example : GET http://localhost:8000/books
- Shutdown API + db :
  - `docker-compose down`
- Connect to database (PostgreSQL) :
  - hostname : localhost
  - port : 5432
  - db name : john
  - id : john
  - password : example
- Check file content in container :
  - List containers running : `docker ps`,
  - Copy container id,
  - Run : `docker exec -it {container id} bash`
- [Cheatsheet docker / docker-compose / k8s](./readme_old.md)


## How to test
- ...
   

## Annex
- Markdown langage : https://www.markdownguide.org/