#!/bin/bash

THRESHOLD=80
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Checking disk space..."

df -H | grep -vE '^Filesystem|tmpfs' | while read -r line; do
    USAGE=$(echo "$line" | awk '{print $5}' | sed 's/%//')
    MOUNT=$(echo "$line" | awk '{print $6}')

    if [ "$USAGE" -ge "$THRESHOLD" ]; then
        echo "[$DATE] ALERT: $MOUNT is at ${USAGE}% - Action needed!"
    else
        echo "[$DATE] OK: $MOUNT is at ${USAGE}%"
    fi
done
