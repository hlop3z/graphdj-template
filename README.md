# Django GraphDJ Project Template

Welcome to **Django's GraphDJ Template!**

## Installation
```sh
django-admin startproject \
  --template=https://github.com/hlop3z/graphdj-template/archive/master.zip \
  --name=Procfile \
  new_django_project
```

## Then — Recreate in **Development**
```sh
python -m pipenv install --dev
```

## Then — Move file **.env**
```sh
mv .env_example.cfg .env.cfg
```

## Then — Create a **Secret-Key**
> After creating the **Secret-Key** add it inside the **.env** file in the **DJANGO_SECRET_KEY** variable.

> **Optionally**: You can pass a size parameter for example —> `keygen.sh 64`
```sh
sh scripts/keygen.sh
```

## Run Server — Development Mode
```sh
sh rundevops.sh
```

<br/><br/>

## Pre-Commit — Check All-Files.
```sh
pre-commit run --all-files
```

## Watcher — black, isort & pylint
```sh
python -m pipenv run python scripts/watcher.py
```

<br/><br/>

## Recreate in **Production**
```sh
python -m pipenv install --ignore-pipfile
```

<br/><br/>

## Links
* [Pre-Commit](https://github.com/pre-commit/pre-commit)
