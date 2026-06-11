#!/bin/bash

case "$1" in
  build_generator)
    docker build -t cat-generator ./generator
    ;;
  run_generator)
    docker run -v $(pwd)/data:/data cat-generator
    ;;
  create_local_data)
    mkdir -p local_data
    python generator/generate.py local_data
    ;;
  build_reporter)
    docker build -t cat-reporter ./reporter
    ;;
  run_reporter)
    docker run -v $(pwd)/data:/data cat-reporter
    ;;
  structure)
    find . -not -path './.git/*' | sort
    ;;
  clear_data)
    rm -f data/*.csv data/*.html
    echo "папка data очищена!"
    ;;
  inside_generator)
    docker run -v $(pwd)/data:/data cat-generator ls /data
    ;;
  inside_reporter)
    docker run -v $(pwd)/data:/data cat-reporter ls /data
    ;;
esac
