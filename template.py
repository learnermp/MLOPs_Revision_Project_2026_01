import os
from pathlib import Path
'''
🔹 os

Used for:

Creating directories

Checking if file exists

Checking file size

🔹 Path (from pathlib)

Used to handle file paths
'''

project_name = "visa_project"

list_of_files = [ 
        f"{project_name}/__init__.py",
        f"{project_name}/components/__init__.py",
        f"{project_name}/components/data_ingestion.py",
        f"{project_name}/components/data_validation.py",
        f"{project_name}/components/data_transformation.py",
        f"{project_name}/components/model_trainer.py",
        f"{project_name}/components/model_evaluation.py",
        f"{project_name}/components/model_pusher.py",
        f"{project_name}/configuration/__init__.py",
        f"{project_name}/constants/__init__.py",
        f"{project_name}/entity/__init__.py",
        f"{project_name}/entity/config_entity.py",
        f"{project_name}/entity/artifact_entity.py",
        f"{project_name}/exception/__init__.py",
        f"{project_name}/logger/__init__.py",
        f"{project_name}/pipeline/training_pipeline.py",
        f"{project_name}/pipeline/prediction_pipeline.py",
        f"{project_name}/utils/__init__.py",
        f"{project_name}/utils/main.py",
        "app.py",
        "requirements.txt",
        "Dockerfile",
        ".dockerignore",
        "demo.py",
        "setup.py",
        "config/model.yaml",
        "config/schema.yaml"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        '''
        Now:

        If folder does not exist → it creates it.

        If folder already exists → it does nothing.

        No error.

        '''
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        '''
        This checks:

        ✔ File does not exist
                OR
        ✔ File exists but is empty
        '''
        with open(filepath, "w") as f:
            pass
        '''
        This:

        Opens file in write mode

        Creates it if not present

        Leaves it empty (pass does nothing)
    '''
    else:
        print(f"file is already present at : {filepath}")