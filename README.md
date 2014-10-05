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

    `sudo npm install -g bower`

7. Install second set of dependancies using bower

    `bower install`

8. Install grunt for building frontend files

    `sudo npm install -g grunt-cli`

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
    $ ./run.sh

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

installation
------------

1. Place the following in project_directory/.git/hooks/pre-commit
2. Make the file executable

Pip Installable Requirements
----------------------------
```
flake8==2.2.1
flake8-print
flake8-debugger
```

pre-commit
----------

```bash
#!/bin/sh

# Allows for colors and such
export TERM=xterm-256color


FILES="git diff --cached --name-only --diff-filter=ACM"
ROOT=$(git rev-parse --show-toplevel)
RETVAL=0

PYTHON_FILES=$($FILES | grep -E ".py$")
# This is because flake8's --exclude doesn't seem to work properly. Exclude via grep.
PYTHON_FILES_WITHOUT_MIGRATIONS=$($FILES | grep -E ".py$" | grep -v "migrations/")
JS_FILES=$($FILES | grep -E ".js$" | grep -v "dist" | grep -v "/build/")

if [ -n "$PYTHON_FILES" ]; then

    flake8=$(which flake8)
    has_flake8_print=$(flake8 --version | grep flake8-print | wc -l)
    has_flake8_debugger=$(flake8 --version | grep flake8-debugger | wc -l)

    if [ -z "$flake8" ] || [ $has_flake8_print -lt 1 ] || [ $has_flake8_debugger -lt 1 ]; then
        printf "\033[31mYou must install flake8 to check for python violations; sudo pip install flake8==2.2.1; sudo pip install flake8-print; sudo pip install flake8-debugger;\n\033[0m"
        RETVAL=1
    else
        printf "\033[32mChecking python files for flake8 violations\n\033[0m"

        for file in ${PYTHON_FILES_WITHOUT_MIGRATIONS}; do
            FLAKE8_ERRORS=$(git show :${file} | flake8 --ignore=E501 - | sed -e 's/^stdin\:/line /g')

            print_allowed=$(echo $file | grep -E "(management/commands|manage.py|/scripts|settings.py)" | wc -l)

            if [ "$print_allowed" -gt 0 ]; then
                FLAKE8_ERRORS=$(echo "$FLAKE8_ERRORS" | grep -v "print statement")
            fi

            if [ "$FLAKE8_ERRORS" != "" ]; then
                printf "\033[33mFlake8 errors detected in $file\n\033[0m"
                printf "\033[31m$FLAKE8_ERRORS\n\033[0m"
                RETVAL=1
            fi
        done
    fi
    RETVAL=$?
fi

if [ -n "$JS_FILES" ]; then

    jshint=$(which jshint)
    node=$(which node)

    if [ -z "$jshint" ] || [ -z "$node" ]; then
        printf "\033[31mYou must install jshint to check for javascript violations; sudo npm install -g jshint\n\033[0m"
        RETVAL=1
    else
        printf "\033[32mChecking javascript files for linting errors\n\033[0m"

        for file in ${JS_FILES}; do
            result=$(git show :${file} | jshint - | sed -e 's/^stdin\: line/line/g')

            if [ "$result" != "" ]; then
                printf "\033[33mJSHint errors detected in $file\n\033[0m"
                printf "\033[31m$result\n\033[0m"
                RETVAL=1
            fi
        done
    fi
fi

if [ $RETVAL -eq 0 ]; then
    printf "\033[32mNo errors found!\n\033[0m"
fi

exit $RETVAL
```

Post-Checkout Hook
==================

installation
------------

1. Place the following in project_directory/.git/hooks/post-checkout
2. Make the file executable

post-checkout
-------------

```bash
#!/bin/bash

export TERM=xterm-256color

# Start from the repository root
cd ./$(git rev-parse --show-cdup)

printf "\e[32mRemoving .pyc and empty directories...\n\033[0m"
find . -name "*.pyc" -delete
find . -type d -empty -delete
```
