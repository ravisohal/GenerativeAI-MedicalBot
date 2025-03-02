import os
from pathlib import Path
import logging

# List of files to be created
list_of_files = [
    "./src/__init__.py",
    "./src/helper.py",
    "./src/prompt.py",
    "./.env",
    "./setup.py",
    "./app.py",
    "./research/trials.ipynb",
    "./test.py",
]

def create_project_structure(list_of_files):
    """Creates a project structure with src, research directories and specified files."""

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    if not os.path.exists("src"):
        Path("src").mkdir(parents=True, exist_ok=True)
        logging.info("Created src directory")

    if not os.path.exists("research"):
        Path("research").mkdir(parents=True, exist_ok=True) 
        logging.info("Created research directory")

    for file in list_of_files:
        filepath = Path(file)

        if filepath.exists():
            logging.info(f"{file} already exists")
            continue

        filepath.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(filepath, "w") as f:
                pass
            logging.info(f"Created {file}")
        except Exception as e:
            logging.error(f"Error creating {file}: {e}")
            return False
        
        logging.info(f"Created {file}")

    logging.info("Project structure created successfully!")
    return True

if __name__ == "__main__":
    create_project_structure(list_of_files)