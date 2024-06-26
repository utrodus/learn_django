# Learn Django For Beginner 
## Overview
This repository is the result of the practice of developing and building websites using **Django 4.2.0** from the book [*Django for Beginners* by William Vincent](https://djangoforbeginners.com/). 

The book provides a comprehensive introduction to building web applications with Django, a popular web framework for Python.

## Content

The repository is organized into several folders, each corresponding to a chapter or project from the book. Each folder contains:

- **Source Code**: The complete source code for the project or exercise.
- **README**: Detailed explanations and instructions related to the project.

## Prerequisites

To follow along with the code and examples in this repository, you will need:

- Basic knowledge of Python programming.
- A development environment set up with Python 3.12.3 or higher.
- Familiarity with basic web development concepts (HTML, CSS, JavaScript).

## Getting Started

To get started with the code in this repository:

1. Clone the repository:
   ```bash
   git clone https://github.com/utrodus/learn_django.git
   python3
2. Setup virtual environtment and enter directory:
   ```bash
   # Windows
   $ cd ch_02_hello_world_app
   $ python -m venv .venv
   $ .venv\Scripts\Activate.ps1
   (.venv) 

   # macOS
   $ cd ch_02_hello_world_app
   $ python3 -m venv .venv
   $ source .venv/bin/activate   
   (.venv) $ 

3. install requirements.txt, **Ex: Open ch_02_hello_world_app :**
   ``` bash  
   (.venv) $ pip install -r requirements.txt

4. And then run the django server with this commands:
   ``` bash
   (.venv) $ python manage.py runserver
