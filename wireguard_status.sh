#!/bin/bash

state=$(sudo wg | head -1)

if [ -z "$state" ]
then
    echo "Wireguard is down!"
else
    echo "Wireguard is up!"
    temp=$(sudo wg | grep handshake --before-context=1 --after-context=1)
    if [ -z "$temp" ]
    then
        exit
    fi
    i=0

    while IFS= read -r line; do
        if [ "$line" != "--" ]; then
            i=$((i + 1))
            if (( i%3 == 1 )); then
                set -- $line
                name=$(sudo cat /etc/wireguard/wg0.conf | grep $3 --before-context=2)
                j=0
                while IFS= read -r line2; do
                if [ "$line2" != "" ]; then
                    # echo "$line2"
                    j=$((j + 1))
                    if (( j%3 == 1 )); then
                        echo ${line2:2}
                    fi
                fi
                done <<< "$name"
            else
                echo $line
            fi
        fi
    done <<< "$temp"
fi