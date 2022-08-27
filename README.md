# FastAPI Template

The purpose of this project is to be used as base boiler plate for future web application built with `Fast API`

## Development


**Requirements**

- Pyenv: Tool to allow live together multiple python installations at the same time, [install](https://github.com/pyenv/pyenv)
- Virtualenv: Bring us the possibility of create multiple isolated group of requirements to avoid clash between projects modules.
- Poetry: Package manager, it comes with some utilities out of the box that are pretty good for projects
- Docker: Platform to deploy containers straightaway

### 1. Create and activate a Virtual env

Install python 3.10 (minimum) and create a new virtual env for our project
```bash
pyenv install 3.10.4
pyenv virtualenv 3.10.4 fastapi-template
```
Once the initial required modules are installed, you need to install project dependencies for that we need poetry and then the dependencies

```bash
pip install poetry
poetry install
```

### 2. Up docker containers

In order to work properly the project needs some satellital applications for this we are using docker (the standar way).

Firstly create `.env` file from the example `.env.dist` it should works without a modification but feel free if you need to do adjustments

```bash
cp .env.dist .env
```

Once we have the `.env` ready we should launch our docker containers

```bash
docker compose up -d
```