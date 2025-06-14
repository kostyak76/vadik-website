# vadik-website
=======

# Prepare environent

## General information
there are different groups of html files under '/src' folder:
- files to match generated files. they do not have `_` at the beginning
- files with underscore
   - components
   - template files


## Install python environment
[todo make me]
### Make virtual environment
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
## Install nodejs environment
[todo make me]

# Build
Use two step build to render this website

## step one - build html files from templates
### TLDR
have installed python3, staticjinja

run
```
$ python build.py
```
## step two - build css files from html files, assets, and src/tailwind.css
have nodejs installed and node packages

# Use cases
- Regenerate copyright date [todo make me]

# TODO
- what about social media links???
- implement /todo.html links
- add a map?
- add popup promitional banner?
- add search engine texts
- fix footer position on big screen
- rethink Contact-US section
- clean assets


# REFS
- for icons [google fonts](https://fonts.google.com/icons?icon.query=time&icon.size=24&icon.color=%231f1f1f)
