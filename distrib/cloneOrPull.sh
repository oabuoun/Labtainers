#!/bin/bash
if [[ ! -d Labtainers ]]; then
    git clone https://github.com/oabuoun/Labtainers.git
    cd Labtainers
else
    cd Labtainers
    # avoid conflicts
    rm README.md
    git pull
fi
git checkout premaster
