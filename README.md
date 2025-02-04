# Web-Scrapping-Boilerplate

This is a Web-Scrapping boilerplate project.
This project is running on python version 3.12.3

# Introduction

The goal of this project is to make a web-scrapping framework professionally and everyone can use this project.

_Also want to cover up this things_

* Selenium driver
* Logger

# Project Setup

To use this project to your own machine follow this steps

### Clone repository from github

First of all, clone this repository using this command

```
git clone https://github.com/mehedishovon01/web-scraping-boilerplate.git
```

### The project layouts

```
Web-Scarapping-Boilerplate
├── src
│   ├── config
│   ├── logs
│   ├── output
│   ├── services
│   ├── utils
│   ├── main.py
│   ├── requirements.txt
├── .gitignore
├── README.md
```

### Create a virtualenv

Make a virtual environment to your project directory. Let's do this,

If you have already an existing python virtualenv then run this

```
virtualenv venv
```    

Or if virtualenv is not install in you machine then run this

```
python -m venv venv
```    

Activate the virtual environment and verify it

```
. venv/bin/activate
```    

### Install the dependencies

Most of the projects have dependency name like requirements.txt file which specifies the requirements of that project,
so let’s install the requirements of it from the file.

```
pip install -r requirements.txt
```

Boooooom! Project setup is done.

## Run the script
Run the script using the command below. It will create a `output` directory and download the pdf and also create a `logs` directory and track a log status.
```
python main.py --env dev --debug
```

`Thanks for reading. # Web-Scrapping-Boilerplate`
