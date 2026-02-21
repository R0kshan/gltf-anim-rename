#!/bin/bash
# If venv doesn't exist, create it and install requirements
if [ ! -d "venv" ]; then
    python -m venv venv
    ./venv/bin/pip install -r requirements.txt
fi

# Run the python script using the venv's python directly
./venv/bin/python gltf-anim-rename.py "$@"