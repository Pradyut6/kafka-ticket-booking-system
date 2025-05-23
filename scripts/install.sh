#!/bin/bash
sudo apt update && sudo apt install -y docker.io docker-compose python3-pip
pip3 install fastapi uvicorn kafka-python pydantic