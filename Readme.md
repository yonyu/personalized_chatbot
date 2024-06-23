# This project is to create a Personalized Chatbot with OpenAI API

## Set up OpenAI account
https://platform.openai.com/docs/quickstart

### Set the OPENAI_API_KEY environment variable
> Add to the current session
> 
> setx OPENAI_API_KEY "your-api-key-here"
> 
> Or add OPENAI_API_KEY to the System Environment variables

## Set up Python
Use Microsoft Store to install the latest Python (3.12.4)

>install pipx
> 
>python.exe -m pip install --upgrade pip
> 
>pipx install virtualenv

### create a virtual env at the project folder
>$ virtualenv venv -p python3.10

### activate the virtual env from the project folder
>$ .\venv\scripts\activate

## Install PyMuPDF
> python.exe -m pip install --upgrade pip
> 
> pip install pymupdf

### create extract_pdf.py and unit tests

## Install packages for scraping web pages

### Install the 'requests' pacakge
> pip install requests
### Install the 'beautifulsoup4' package
> pip install beautifulsoup4

## Install the OpenAI package

> pip install --upgrade openai
> 

## Install the langchain-openai package

> pip install langchain-openai langchain
> 

## Install the Flask package

> pip install Flask
> 

## Run application

> python main.py
> 
> Open a browser, and type in 'http://127.0.0.1' to start a conversation.
> 
> Type a question, you'll an answer from the hotel manager.
> 
> To start a JavaScript debug session from the command window:
> ctrl+shift+'clicking http://127.0.0.1' 

## Next Steps
* Improve UI with better CSS
* Look for different features on LangChain
