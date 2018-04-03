#!/bin/bash

code="$(cat code.txt)"

for ((i=0; i<16; i++)); do
    code="$(echo "$code" | base64 --decode)"
done

echo "$code" | uudecode -o /dev/stdout
