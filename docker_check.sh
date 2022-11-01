#!/bin/bash

docker ps -a --format="{{.Image}}~ {{.Status}}"