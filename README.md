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
- make updates from the email (page updates)
- implement /todo.html links
- 404 page???
- promotions popup???
- make top nav to have an active item (link of different color that corresponds to the current page)
- add request estimate to the header
- add a map?
- add popup promitional banner?
- add search engine texts


# REFS
- for icons [google fonts](https://fonts.google.com/icons?icon.query=time&icon.size=24&icon.color=%231f1f1f)

# FROM Vadim Email
https://metro-plumbing.ca

We need to make changes on the main page.

1. Below the first photo of the guy there are three tabs
"PLUMBING SERVICES
From leaky faucets to major repairs, we handle all your plumbing needs.
DRAIN CLEANING
Our expert drain cleaning services, will restore flow and function to your home.
DRAIN REPAIR
We deliver top-quality drain repair services that provide lasting value."
These tabs lead to another page, the same one, which has a lot of nonsense.
We leave the three tabs on the main page, but so that they do not lead anywhere, and we also need to remove the words "Learn more"

2, Remove from the top of the site: "Locations" and "Blog"

3, The map needs to be removed from the main page to a tab "Contact us"

4.At the very bottom of the site there are tabs
"Popular Services
Furnace Inspection
Dry Sanitation
Water Filter
Basic Sanitation

Emergency Tips
Pipe Leaking
Bathroom Drain Cleaning
Garden Irrigation
Law Drainage"
All this needs to be removed from the site (there is some nonsense described there and sometimes not in English))

5.At the bottom of the site change Email info@metroplumbingdrain.com and address 11 Superior Ave Toronto Ontario M8V 0A7

 Thank you so much for your help