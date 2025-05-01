# To PDF Converter

A simple web API built with FastAPI that converts .docx files to .pdf using docx2pdf Python library.

## Features

- Upload a .docx file and receive a .pdf in response
- Built with FastAPI
- Handles file storage securely
- Automatically creates upload directories

## Stacks 

- Python 
- FastAPI – for building the web server
- docx2pdf – for converting .docx files to .pdf

## Setup instructions

- Clone repository
git clone https://github.com/your-username/docx-to-pdf-api.git
cd docx-to-pdf-api

- Install dependencies
pip install -r requirements.txt

- Run the server
uvicorn main:app --reload

## How to use

- Make a POST requesto to
http://localhost:8000/convert



