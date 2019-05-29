#!/usr/bin/bash

toplevel="$(git rev-parse --show-toplevel)/recursos"
cd "$toplevel"
files=$(find . -mindepth 2 -maxdepth 2 -name '*.py')

for file in $files
do
    echo $file

    cd "$(dirname $file)"
    python3 $(basename $file)

    cd "$toplevel"
done
