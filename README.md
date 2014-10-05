Django Sass Template
====================

Setup
-----

1. Install Ruby (I use [RVM](http://rvm.io/rvm/install))
2. Install Sass Ruby gem

    `gem install sass`

3. Install [NodeJs](http://nodejs.org/)
4. Checkout this project and change into the directory.
5. Install first set of dependencies

    `npm install`

6. Install bower globally.

    `npm install -g bower`

7. Install second set of dependancies using bower

    `bower install`

8. Install grunt for building frontend files

    `npm install -g grunt-cli`

9. Build frontend files

    `grunt`

10. Download python (~2.7) if you don't have it.
11. Download [pip](https://pip.readthedocs.org/en/latest/installing.html)
12. Download virtualenv

    `pip install virtualenv`

13. Download virtualenvwrapper

    `pip install virtualenvwrapper`

14. Set [required variables](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

    I have the following in my `$HOME/.bashrc` file:
    ```sh
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/virtualenvProject
    source /usr/local/bin/virtualenvwrapper.sh
    ```

15. Setup python virtual environment in the project directory (assuming you're inside it), replace the project name with one of your choice.

    `mkvirtualenv <project-name> -a . -r ./requirements.txt`.

    note: (You can use `pip install -r ./requirements.txt` to install/update the python project requirements at any time).


Start the app
-------------

    $ workon <project-name>
    $ python manage.py runserver 8000

Navigate to the website
-----------------------

    It's located at `http://localhost:8000/`

Requirements
------------

* python 2.7
* Ruby and the sass gem
* pip
* NodeJs


Running The Tests
-----------------
`nosetests --with-progressive`

Pre-Commit Hook
===============

Place this in project_directory/.git/hooks/pre-commit (make sure it's executable)
```bash
#!/bin/bash

export TERM=xterm-256color

flake8=$(which flake8)

if [ -z "$flake8" ]; then
    $echo "You must install flake8; sudo pip install flake8"
    exit 1
fi

FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -e '\.py$')

# Check for print statements
if [ -n "$FILES" ]; then
    printf "\e[32mChecking files for print violations\n\033[0m"
    grep -n -E -v "^#" $FILES | grep -E "[^\"']\bprint[\"' ]+"
fi

# Check for ipdb and pdb imports/usage
if [ -n "$FILES" ]; then
    printf "\e[32mChecking files for pdb violations\n\033[0m"
    grep --exclude=\*pre-commit -n -E "import.*i?pdb|i?pdb\." $PYTHON_FILES
fi

# Auto-check for pep8
if [ -n "$FILES" ]; then
    printf "\e[32mChecking Python files for flake8 violations\n\033[0m"
    flake8 --ignore=E501 $FILES
    RETVAL=$?
fi

# Run nosetests
nosetests --with-progressive
PASSED=$?

exit $RETVAL && $PASSED
```

Post-Checkout Hook
==================
Place this in project_directory/.git/hooks/post-checkout (make sure it's executable)

```bash
#!/bin/bash

export TERM=xterm-256color

# Start from the repository root
cd ./$(git rev-parse --show-cdup)

printf "\e[32mRemoving .pyc and empty directories...\n\033[0m"
find . -name "*.pyc" -delete
find . -type d -empty -delete
```
