import os

include_data_dirs = bool("{{ cookiecutter.include_data_dirs }}")
include_scripts = bool("{{ cookiecutter.include_scripts }}")

if include_data_dirs:
    folder_names = ["data", "export"]
    for folder in folder_names:
        os.makedirs(
            os.path.join(
                os.getcwd(),
                folder,
            )
        )

if include_scripts:
    os.makedirs(
        os.path.join(
            os.getcwd(),
            "scripts",
        )
    )
