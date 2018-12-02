#!/bin/bash

ID=1
while [ -d "$(basename "$1" .poly).$ID" ]; do
  ID=$(($ID + 1))
done
DIR=$(basename "$1" .poly).$ID
mkdir "$DIR"
./triangle "$@"
mv $(basename "$1" .poly).1.* "$DIR"
./gtikz.py "$DIR"/$(basename "$1" .poly).1 -o "$DIR"/$(basename "$1" .poly).1 --width=5000 --height=5000 --svg
