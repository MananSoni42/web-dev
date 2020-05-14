#!/bin/bash

if [[ -z "${R_DB}" ]]; then
    python3 reset_db.py;
    export R_DB=1;
fi
