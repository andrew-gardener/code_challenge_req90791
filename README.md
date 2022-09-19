# code_challenge_req90791

## Prerequisites

- docker install (I used [docker-desktop](https://www.docker.com/products/docker-desktop/))

## Setup

For first time setup start `postgres` a bit early since it takes a a few seconds to init the db

    docker compose up -d db
    docker compose logs -f db

Wait until initialization is complete then you can build the backend and frontend images

    docker compose up -d --build

Next setup tables & seed the database

    docker compose exec -it backend ./manage.py migrate
    docker compose exec -it backend ./manage.py loaddata seed

## Run tests

### Backend

    docker compose up -d
    docker compose exec -it backend ./manage.py test

### Frontend

    docker compose up -d
    docker compose exec -it frontend yarn test:unit

## Deployment

Uses Heroku for the backend and github pages for the frontend. Deployment is automatic via github actions. The deployment runs can be seen [here](https://github.com/andrew-gardener/code_challenge_req90791/actions/workflows/deploy.yml).

### Backend Heroku deployment notes

Uses straight docker container deployment and a (free) Heroku Postgres add-on. Otherwise it just has some environment variables set in the app.

    ALLOWED_HOSTS=code-challenge-req90791.herokuapp.com
    CORS_ALLOWED_ORIGINS=https://code-challenge-req90791.herokuapp.com,https://req90791.andrewgardener.com
    DATABASE_URL=<CONTAINS SECRETS>
    POSTGRES_HOST=ec2-52-200-5-135.compute-1.amazonaws.com
    POSTGRES_PORT=5432
    POSTGRES_NAME=<CONTAINS SECRETS>
    POSTGRES_USER=<CONTAINS SECRETS>
    POSTGRES_PASSWORD=<CONTAINS SECRETS>
    SECRET_KEY=<CONTAINS SECRETS>

`DATABASE_URL` is set automatically by heroku

Otherwise I just seeded the database with `heroku run ./manage.py loaddata seed`

### Frontend github pages deployment notes

`frotnend/.env.production` is hardcoded to point to the heroku backend which will populate. Otherwise it just uses a custom domain `req90791.andrewgardener.com` that I already had setup for my personal website.

# Notes of decisions, observations, and assumptions

## Decisions

- Going with [Django](https://www.djangoproject.com/) backend since it should be quick and I have previous experience
- Going with [Vue.js](https://vuejs.org/) frontend to try it out (meaning to try it out and this is a good opportunity)
- Going to use [GitHub Actions](https://github.com/features/actions) for CI/CD since the repo is on github and its build in and easy
- Going to deploy the backend on [Heroku](https://www.heroku.com/) since its free
- Going to deploy the frontend on [GitHub Pages](https://pages.github.com/) since its free and easy for static content
- Decided on `Swimlane` and `Boat` for the models/tables
  - Went with shortened uuid4 for primary keys
    - normally I'd have both auto increment integer for id primary key and unique shortened uuid for frontend consumption but I went with just shortened uuid4 for simplicity sake
  - Used a [random name generator](https://www.fantasynamegenerators.com/ship-names.php) for the seeded boat names

## Observations

- Instead of a restful api backend, GraphQL could be an interesting alterative due to simple nature and no authorization/property level permission complexity.
- I only did a small amount of TDD for the backend tests as most of the endpoints creation was heavily using

## Assumptions

- That it would be okay to seed default swimlanes mentioned in the instructions context into the database and there is no need to add/edit/remove the swimlanes dynamically (they are static).
- Since its a small app, no pagination is needed for the backend api endpoints

## Mistakes/bad assumptions that I fixed

- I at first assumed that guides needed to be included in the application. While it would probably be part of a more robust complete solution, it was explicitly art of the requirements so I ultimately removed it to simplify the application development.