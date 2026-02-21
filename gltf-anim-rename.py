import sys
import os
from pygltflib import GLTF2 # install with: pip install pygltflib

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

def main():

    # Ensure at least Python 3.8
    if sys.version_info < (3, 8):
        print("Error: This script requires Python 3.8 or higher.")
        print(f"You are currently using Python {sys.version_info.major}.{sys.version_info.minor}")
        sys.exit(1)
    
    # Usage: python glb-animation-renamer.py <file.glb> <old_anim> <new_anim>
    if len(sys.argv) == 4:
        script_name = sys.argv[0]
        glb_file = sys.argv[1]
        original_anim = sys.argv[2]
        replacement_anim = sys.argv[3]

        validate_file(glb_file, extension=".glb")
        
        print(f"--- Excecution script {script_name} ---")
        print(f"Target File:      {glb_file}")
        print(f"Original Anim:    {original_anim}")
        print(f"Replacement Anim: {replacement_anim}")
        
        try:
            # Load the GLB file
            gltf = GLTF2.load(glb_file)
            
            # Get list of all animation names for verification
            available_anims = [anim.name for anim in gltf.animations if anim.name]
            
            found = False
            for anim in gltf.animations:
                if anim.name == original_anim:
                    anim.name = replacement_anim
                    found = True
            
            if found:
                # Generate output filename (e.g., model_renamed.glb)
                base, ext = os.path.splitext(glb_file)
                output_file = f"{base}-anim-renamed{ext}"
                
                # Save the changes
                gltf.save(output_file)
                print(f"Success: Original animation '{original_anim}' has been renamed to '{replacement_anim}' in {output_file}")
            else:
                print(f"Error: Animation '{original_anim}' not found.")
                if available_anims:
                    print(f"Available animations in this file: {', '.join(available_anims)}")
                else:
                    print("This GLB file contains no named animations.")
                sys.exit(1)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            sys.exit(1)
        
    else:
        print("Error: Missing or too many parameters.")
        print("Usage: python glb-animation-renamer.py <file.glb> <original_animation_name> <replacement_animation_name>")
        sys.exit(1)

if __name__ == "__main__":
    main()

