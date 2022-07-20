# Getting Started

## Installing Python 3.9 or higher
Please install python version 3.9 or higher from the [Python website](https://www.python.org/downloads/).

## Initializing the environment
Open a terminal and navigate to this directory.

Check your python version of your environment by running the following command:

```
python --version
```

Ensure that the python version is 3.9 or higher.

Run the following command:

```
python -m venv .env
```

Activated your enviroment in the following way:

- On Windows:
```
.\env\Scripts\Activate.ps1
```

- On Linux:
```
source .env/bin/activate
```

## Installing the dependencies
Intall python packages:

```
python -m pip install -r requirements.txt
```
Install this package in edit mode:

```
python -m pip install -e .
```

## Running the solver
Run the following command to run the solver:

```
python ./labyrinth_solver/main.py
```
