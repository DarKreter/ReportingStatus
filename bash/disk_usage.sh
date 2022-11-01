#!/bin/bash

# Print the disk usage of SSD with  columns titles
df -h / 

# Print usage of pools
df -h | grep mnt