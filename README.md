# Python script for renaming animations in a GLB file

Some GLB files end up exported with animations associated with the wrong animation name (my issue when exported my GLB from [Meshy AI](https://www.meshy.ai)).
This python script allows you to rename them.

## How to use

**NB :**  Please check prerequisites first.

First make the script executable : `chmod +x run.sh`
Running the script : `./run.sh example/model.glb Jump_Over_Obstacle_2 Idle` will produce model-anim-renamed.glb with the desired change.

## Pre-requisites

Run the installation script [install-prereqs.sh](install-prereqs.sh) using :

**NB :**

- Python version 3.6 (verified using [vermin](https://github.com/netromdk/vermin))
- Checkout [requirements.txt](requirements.txt) generated using [pipreqs](https://github.com/bndr/pipreqs)

```
chmod +x install-prereqs.sh
./install-prereqs.sh
```

**NB :** This script installs :

- [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#a-getting-pyenv), a tool that simplifies switching between python versions.
- [venv](https://docs.python.org/3/library/venv.html), a virtual environnement with the required dependencies to run the script.

## Future developement

Renaming multiple animations at once with a file as input.
