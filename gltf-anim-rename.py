import sys
import os
from pygltflib import GLTF2 # install with: pip install pygltflib

def validate_python_version():
    if sys.version_info < (3, 8):
        print("Error: This script requires Python 3.8 or higher.")
        print(f"You are currently using Python {sys.version_info.major}.{sys.version_info.minor}")
        sys.exit(1)

def validate_parameters(num_args):
    if num_args not in [3, 4]:
        script_name = sys.argv[0]
        print("Usage:")
        print(f"  Single: {script_name} <file.glb> <old_anim> <new_anim>")
        print(f"  Map:    {script_name} <file.glb> <mapping_file.txt>")
        sys.exit(1)

def validate_file(filepath, extension=None):
    
    if not os.path.exists(filepath):
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit(1)
    
    if extension and not filepath.lower().endswith(extension):
        print(f"Error: '{filepath}' is not a valid {extension.upper()} file.")
        sys.exit(1)

def load_mapping(filepath):
    """Parses a file with 'old_name->new_name' syntax."""
    mapping = {}
    try:
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or "->" not in line:
                    continue
                old, new = line.split("->", 1)
                mapping[old.strip()] = new.strip()
        return mapping
    except Exception as e:
        print(f"Error reading mapping file: {e}")
        sys.exit(1)

def generate_output_file(gltf,glb_file):
    base, ext = os.path.splitext(glb_file)
    output_file = f"{base}-anim-renamed{ext}"
    gltf.save(output_file)
    print(f"\nSuccess: Original animations have been renamed in {output_file}")

def main():

    validate_python_version()
    validate_parameters(len(sys.argv))

    script_name = sys.argv[0]
    glb_file = sys.argv[1]

    validate_file(glb_file, extension=".glb")
       
    if len(sys.argv) == 4:
        original_anim = sys.argv[2]
        replacement_anim = sys.argv[3]
        mapping = {}
        mapping[original_anim] = replacement_anim
        
        print(f"--- Excecution script {script_name} ---")
        print(f"Target File:      {glb_file}")
        print(f"Original Anim:    {original_anim}")
        print(f"Replacement Anim: {replacement_anim}")
    else:
        mapping_file = sys.argv[2]
        mapping = load_mapping(mapping_file)

        print(f"--- Execution script {script_name} ---")
        print(f"Target File:      {glb_file}")
        print(f"Mapping File:     {mapping_file}")
        

    print("\nAnimations to be renamed:")
    for old, new in mapping.items():
        print(f"  {old} -> {new}")

    try:
        # Load the GLB file
        gltf = GLTF2.load(glb_file)
        
        # Get list of all animation names for verification
        available_anims = [anim.name for anim in gltf.animations if anim.name]
        print(f"\nAvailable animations before renaming : {', '.join(available_anims)}")
        
        found = False
        for anim in gltf.animations:
            if anim.name in mapping:
                anim.name = mapping[anim.name]
                found = True
        
        if not found:
            print(f"\nError: Animations defined in {mapping} not found.")
            if available_anims:
                print(f"Available animations in this file: {', '.join(available_anims)}")
            else:
                print("This GLB file contains no named animations.")
            sys.exit(1)
    
        generate_output_file(gltf,glb_file)

        anims_after_rename = [anim.name for anim in gltf.animations if anim.name]
        print(f"\nAvailable animations after renaming: {', '.join(anims_after_rename)}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
        
    

if __name__ == "__main__":
    main()

