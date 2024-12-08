# Pakage in Python 
# => In Python, a package is a collection of modules that are related to each other and can be used together.
# => A package is a directory that contains one or more modules.
# => A package is a directory that contains one or more subdirectories.

# __init__.py file in Python
# => A __init__.py file is a special file that is used to indicate that a directory is a Python package.
# => A __init__.py file is a file that is used to initialize a package

# => A __init__.py file is a file that is used to initialize a package
''' 
game_project/
├── game_project/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── character.py
│   │   ├── enemy.py
│   │   └── ...
│   ├── views/
│   │   ├── __init__.py
│   │   ├── game_view.py
│   │   └── ...
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── game_controller.py
│   │   └── ...
│   └── ...
└── setup.py

'''

#importing Importing module from a package
#In Python, we can import modules from packages using the dot (.) operator.
# => We can import a module from a package by using the following syntax:
# => from package_name.module_name import module
#example 1 =>
import game_project.views.game_view 
# here now we can use game_project.views.game_view functions

#example 2 =>
from game_project.views import game_view
# here now we can use game_project.views.game_view functions

