import os
import shutil

include_data_dirs = bool("{{ cookiecutter.include_data_dirs }}")
include_scripts = bool("{{ cookiecutter.include_scripts }}")


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
