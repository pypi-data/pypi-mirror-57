# majorly_funny
## setup
1. Things to add to .gitignore
```
# Compiled python modules.
*.pyc

# Setuptools distribution folder.
/dist/

# Python egg metadata, regenerated from source files by setuptools.
/*.egg-info
```
2. setup env variables
```
TWINE_USERNAME
TWINE_PASSWORD
```

## update published package
after making changes to the project (write new code, add resource files, etc...)
1. remove old packages
```
rm dist/*
```

2. bump the version in setup.py

3. build new package
```
python3 setup.py sdist
```

4. check new package
```
twine check
```

5. test publish new package
```
twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose
```

6. publish real package
```
twine upload --repository-url https://upload.pypi.org/legacy/ dist/* --verbose
```
