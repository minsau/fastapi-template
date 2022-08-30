# FastAPI Template

The purpose of this project is to be used as base boiler plate for future web application built with `Fast API`

## Development


**Requirements**

- Pyenv: Tool to allow live together multiple python installations at the same time, [install](https://github.com/pyenv/pyenv)
- Virtualenv: Bring us the possibility of create multiple isolated group of requirements to avoid clash between projects modules.
- Poetry: Package manager, it comes with some utilities out of the box that are pretty good for projects
- Docker: Platform to deploy containers straightaway

**Launch docker containers**

In order to work properly the project needs some satellital applications for this we are using docker (the standar way).

Firstly create `.env` file from the example `.env.dist` it should works without a modification but feel free if you need to do adjustments

```bash
cp .env.dist .env
```

Once we have the `.env` ready we should launch our docker containers

```bash
make up
```

Once inside container you should run init (just if is the first time) and then up
```bash
dev init
dev up
```
Now all the changes that you have in your host machine will be reflected on container code

**Extra: work with VS Code**

If as me you love Visual Studio code this project is configured to work with, just need one extension:

- [Remote Container](https://code.visualstudio.com/docs/remote/containers)

Once you have it installed just need to launch (with make up) the core project and then select the container in vs code
with this you can go to debug menu and click in green button to launch project.

When you are inside the container you could go to VS Code test section and you can appreciate that test discovery is active.

