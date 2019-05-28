#!/usr/bin/bash

cd "$(git rev-parse --show-toplevel)"
files=$(find recursos -mindepth 2 -maxdepth 2 -name '*.py')

for file in $files
do
    echo $file
    python3 $file
done
