#!/bin/bash

value=$(zpool status | grep --before-context=1 state | awk '{print $2}')

while IFS= read -r line; do
    if [ "$line" != "" ]; then
        echo "$line"
    fi
done <<< "$value"
