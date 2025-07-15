import os
import shutil

# Path to the main docs folder
BASE_PATH = "contextmapper"

# List all folders in BASE_PATH
for item in os.listdir(BASE_PATH):
    folder_path = os.path.join(BASE_PATH, item)
    # Check if item is a directory and not a file
    if os.path.isdir(folder_path):
        md_file = os.path.join(BASE_PATH, f"{item}.md")
        index_md = os.path.join(folder_path, "index.md")
        # If markdown file does not exist but index.md exists, copy it
        if not os.path.exists(md_file) and os.path.exists(index_md):
            shutil.copy(index_md, md_file)
            print(f"Created {md_file} from {index_md}")
