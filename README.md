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
- Frontend can maintain order of boats within a swimlane (no need to validate ordering in backend)

## Mistakes/bad assumptions that I fixed

- I at first assumed that guides needed to be included in the application. While it would probably be part of a more robust complete solution, it was explicitly art of the requirements so I ultimately removed it to simplify the application development.