import os
import shutil

include_data_dirs = {{cookiecutter.include_data_dirs}}
include_scripts = {{cookiecutter.include_scripts}}

print("Running post-gen-project hook...")


def remove(path):
    if os.path.isdir(path):
        shutil.rmtree(path)
    elif os.path.isfile(path):
        os.remove(path)


if not include_data_dirs:
    folder_names = ["data", "export"]
    for folder in folder_names:
        remove(folder)
    print("Removed the data and export folders since you chose not to include them.")

if not include_scripts:
    remove("scripts")
    print("Removed the scripts folder since you chose not to include it.")

print("Post-gen-project hook completed.")
print(
    "Don't forget to update the README.md file with instructions on how to use the project."
)
print(
    "cd into the project directory and run 'uv sync' to install the dependencies and set up the virtual environment"
)
