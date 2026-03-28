# Cookiecutter template for jupyter notebooks

Coockiecutter template for creating new Jupyter Notbooks project.

## Installation

You'll need to have [cookiecutter](https://cookiecutter.readthedocs.io/) installed. I recommend pipx for this:
```bash
pipx install cookiecutter
```
Regular `pip` will work OK too.

## Usage

Run `cookiecutter gh:cheleleiva/jn-template` and then answer the prompts.

If running with [uv](https://docs.astral.sh/uv/):

```bash
uvx cookiecutter https://github.com/cheleleiva/jn-template.git
```

Example run:

```bash
uvx cookiecutter https://github.com/cheleleiva/jn-template.git
  [1/5] app_name (): Jupyter notebook demo
  [2/5] description (): Demo of the template https://github.com/cheleleiva/jn-template.git
  [3/5] hyphenated (jupyter-notebook-demo):
  [4/5] underscored (jupyter-notebook-demo):
  [5/5] author_name (): Oscar Leiva
  [6/7] Select include_data_dirs
    1 - y
    2 - n
    Choose from [1/2] (1): 1
  [7/7] Select include_scripts
    1 - y
    2 - n
    Choose from [1/2] (1): 1
```

It recommened to accept the suggested value for "hyphenated" and "underscored" by hitting enter on those prompts.

This will create a directory called `jupyter-notebook-demo` - the tool name you enter is converted to lowercase and uses hyphens instead of spaces.

See https://github.com/cheleleiva/jupyter-notebook-demo for the output of this example.

## Work with the generated template

After running the command you will have a new folder called `jupyter-notebook-demo`

```bash
cd jupyter-notebook-demo
# Sync the enviroment with uv this will install the basic dependencies
uv sync
```

If you need to add more dependencies you can run

```bash
uv add numpy
```


## Creating a Git repository for your tool

You can initialize a Git repository for your tool like this:
```bash
cd jupyter-notebook-demo
git init
git add .
git commit -m "Initial structure from template"
# Rename the 'master' branch to 'main':
git branch -m master main
```

## Publishing your tool to GitHub

Use https://github.com/new to create a new GitHub repository sharing the same name as your tool, which should be something like `jupyter-notebook-demo`.

Push your `main` branch to GitHub like this:
```bash
git remote add origin git@github.com:YOURNAME/jupyter-notebook-demo.git
git push -u origin main
```