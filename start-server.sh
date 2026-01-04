#!/bin/bash
# Simple script to start the local development server

cd "$(dirname "$0")"

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    echo "Starting server with Python..."
    python3 server.py
elif command -v python &> /dev/null; then
    echo "Starting server with Python..."
    python server.py
else
    echo "Python not found. Please install Python 3 or use Node.js:"
    echo "  npm install -g http-server"
    echo "  http-server frontend -p 8000"
    exit 1
fi

