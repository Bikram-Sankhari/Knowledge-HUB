![](https://github.com/Bikram-Sankhari/Knowledge-HUB/blob/main/Cover.png?raw=true)

# A Blogging Web Application

![Static Badge](https://img.shields.io/badge/Python-3.12-green) ![Static Badge](https://img.shields.io/badge/Flask-2.2.0-blue) ![Static Badge](https://img.shields.io/badge/SQLAlchemy-1.4.18-orange) ![Static Badge](https://img.shields.io/badge/Jinja2-3.1.3-%23d13828) ![Static Badge](https://img.shields.io/badge/WTForms-3.1.2-%231875c7) ![Static Badge](https://img.shields.io/badge/Bootstrap-8A2BE2)

 ## Usage
With the Deployed version of this Web App:
- Any user can view Blogs anynomously
- Users can create their own Blogs with the built-in fully-fledged text edior after Registration
- Users can comment on any Blog after successful Authentication
- Users can contact the Site Administrator through the Contact Form

## Features

- User Authentication
- Fully-fledged browser based text editor for designing Blogs
- Comment section for each Blog
- Anonymous Blog view support

------------


## Table of Contents

- [Usage](#usage)
- [Features](#features)
- [Running the App - Guide](#running-the-app---guide)
  + [Prerequisites](#prerequisites)
  + [1. Make a Clone of this repo at your preferred location](#1-make-a-clone-of-this-repo-at-your-preferred-location)
  + [2. Create a Virtual Environment](#3-create-a-virtual-environment)
  + [3. Activate the Virtual Evironment](#4-activate-the-virtual-evironment)
  + [4. Install the required packages](#5-install-the-required-packages)
  + [5. Set environment variables](#6-set-environment-variables)
  + [6. Start serving the Flask Application using Gunicorn](#7-start-serving-the-flask-application-using-gunicorn)
* [Want to Contribute?](#want-to-contribute)
    + [1. Create a Fork of this Repository](#1-create-a-fork-of-this-repository)
    + [2. Clone Your Fork](#2-clone-your-fork)
    + [3. Create a New Branch with a name that best describes the contribution you are about to make](#3-create-a-new-branch-with-a-name-that-best-describes-the-contribution-you-are-about-to-make)
    + [4. Now you can work on your new Branch](#4-now-you-can-work-on-your-new-branch)
    + [5. Commit the changes in your new Branch and push the code to your Forked Repository](#5-commit-the-changes-in-your-new-branch-and-push-the-code-to-your-forked-repository)
    + [6. Give a Pull request to this Upstream Repo](#6-give-a-pull-request-to-this-upstream-repo)
* [Found a BUG 🐞 ??](#found-a-bug--)


## Running the App - Guide
This Guide is for running the Web Application on your local server using GUNICORN.

However you can use any other WSGI server (e.g. - Hetzner) to serve the Flask Application. Also if you want to deploy the application on a remote server you should use a Reverse Proxy (e.g. - NGINX) in front of the WSGI Server.

### Prerequisites
- Python version 3.12 or higher
- Git Installed
- Email with third party app password


#### 1. Make a Clone of this repo at your preferred location

	git clone https://github.com/Bikram-Sankhari/Knowledge-HUB.git

#### 2. Open the just cloned "Knowledge-HUB" directory in terminal

#### 3. Create a Virtual Environment

	python -m venv env

#### 4. Activate the Virtual Evironment
##### for Windows:

	env\Scripts\activate

##### for Linux:

	source env/bin/activate

#### 5. Install the required packages

	pip install -r requirements.txt

#### 6. Set environment variables
- Create a copy of the '.env-sample' file in the root directory of the project and rename the copy to ".env"
- Enter your credentials in the respective fields

#### 7. Start serving the Flask Application using Gunicorn

	gunicorn --bind=127.0.0.1:8000 main:app

## Open [127.0.0.1:8000](127.0.0.1:8000) on your browser.
# And CONGRATULATIONS You have Successfully run the Server !!!!! 🥳


<br><br>
## Want to Contribute? 
All contributions are Welcome. If you want to contribute to this project follow the steps.

### 1. Create a Fork of this Repository
See [GitHub Documentation for Forks](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)

### 2. Clone Your Fork


	git clone <URL TO YOUR FORK>

### 3. Create a New Branch with a name that best describes the contribution you are about to make


	git checkout -b <YOUR BRANCH NAME>

### 4. Now you can work on your new Branch
> After making the changes, Test your code well before committing

### 5. Commit the changes in your new Branch and push the code to your Forked Repository

See [This Documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

### 6. Give a Pull request to this Upstream Repo
See [The GitHub Documentation on Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
> Be Descriptive about the Contribution you have made

------------


## Found a BUG 🐞 ??
As this Application is in the very early stage of it&apos;s development lifecycle, it is anticipated that there are some bugs in the code. So if you find out one, then Please -
Let me know directly by Email: bikramsankhari2024@gmail.com

------------


