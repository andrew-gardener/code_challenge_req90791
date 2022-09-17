# code_challenge_req90791

## Prerequisites

- docker install (I used [docker-desktop](https://www.docker.com/products/docker-desktop/))

## Setup

For first time setup start `postgres` a bit early since it takes a a few seconds to init the db

    docker compose up -d db
    docker compose logs -f db

Wait until initialization is complete then you can build the backend and frontend images

    docker-compose up -d --build


# Notes of decisions, observations, and assumptions

## Decisions

- Going with [Django](https://www.djangoproject.com/) backend since it should be quick and I have previous experience
- Going with [Vue.js](https://vuejs.org/) frontend to try it out (meaning to try it out and this is a good opportunity)
- Going to use [GitHub Actions](https://github.com/features/actions) for CI/CD since the repo is on github and its build in and easy
- Going to deploy the backend on [Heroku](https://www.heroku.com/) since its free
- Going to deploy the frontend on [GitHub Pages](https://pages.github.com/) since its free and easy for static content

## Observations

- 

## Assumptions

- Its okay to seed default swimlanes mentioned in the instructions context into the database and there is no need to add/edit/remove the swimlanes dynamically (they are static).
- 