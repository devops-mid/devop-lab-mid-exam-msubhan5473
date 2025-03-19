#!/bin/bash
echo "Building the application..."
# TODO: Add commands to install dependencies and build the app

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running unit tests..."
pytest
