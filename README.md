# Python script for renaming animations in a GLB file

Some GLB files end up exported with animations associated with the wrong animation name (my issue when exported my GLB from [Meshy AI](https://www.meshy.ai)).
This python script allows you to rename them.

## Pre-requisites

- Minimum python version required : Python version 3.8
- pygltflib==1.16.5 

### Tip 

For easy installation, use the [Python package manager UV](https://docs.astral.sh/uv/guides/install-python/)

## How to use

**NB :**  Please check prerequisites first.

### With UV

For a single replacement, run the following command :

```
uv run gltf_anim_rename.py example/model.glb Jump_Over_Obstacle_2 Idle
```

For multiplements, provide a mapping file (see [mapping.txt](example/mapping.txt)) :

```
uv run gltf_anim_rename.py example/model.glb example/mapping.txt
```

### Without UV 

For a single replacement, run the following command :

```
gltf_anim_rename.py example/model.glb Jump_Over_Obstacle_2 Idle
```

For multiplements, provide a mapping file (see [mapping.txt](example/mapping.txt)) :

```
gltf_anim_rename.py example/model.glb example/mapping.txt
```

### Run the script with UV 

Install the [UV](https://docs.astral.sh/uv/guides/install-python/) package manager. 

Run the following : 

```
uv run gltf_anim_rename.py example/model.glb Jump_Over_Obstacle_2 Idle
```
