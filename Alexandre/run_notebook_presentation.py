import subprocess
import os

cwd = os.getcwd()
file_name = "test.ipynb"
file_path = os.path.join("Alexandre", "notebook")

command = [f"jupyter notebook {file_name}"]
process = subprocess.run(command, cwd=file_path, shell=True)