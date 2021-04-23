# gelata

Gestore delle attività ATA

## Requirements

-   python

    -   [Windows](https://www.python.org/downloads/)

-   pip (it comes with Python)

-   virtualenv

## How to setup

### 1. Download the repo

Download this github repository locally.

### 2. Install the env

Open a terminal (PowerShell on Windows) in the root folder (gelata-main) and run:

```
pip install vitrualenv
```

Create then the virtual environment:

```
virtualenv .
```

Activate it:

On Windows run

```
.\env\Scripts\activate.bat
```

On Linux:

```
source .venv/bin/activate
```

### 3. Install requirements:

```
pip install -r requirements.txt
```

### 5. Create the `.env` file (ask f0lg0 for credentials)

### 6. Run

Change directory with the `cd` command into the `webserver/` folder:

```
cd src
```

```
cd webserver
```

Then run:

```
python main.py
```

## Running it another day

If you need to work on this project after setting up everything you just need to **activate the virtualenv** and **run the main script**.
