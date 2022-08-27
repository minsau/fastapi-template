#!/usr/bin/env bash

cd /opt/app
# image can run in multiple modes
if [[ "${RUNTYPE}" == "bash" ]]; then
    printf "started Docker container as runtype \e[1;93mbash\e[0m\n"
    exec /bin/bash

else
    printf "started Docker container as runtype \e[1;93mweb\e[0m\n"
    # run web server TODO: Improve this command for production
    exec uvicorn app.main:app --host=0.0.0.0 --port=80 --reload
fi