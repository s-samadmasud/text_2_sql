# text_2_sql: Streamlit App for Text-to-SQL Queries

This repository provides a Streamlit application that allows users to input natural language questions and retrieve data from an SQLite database using generated SQL queries.

## Requirements:

Python >= 3.10 (create a virtual environment using the command provided)
requirements.txt file specifies the necessary dependencies.

## Dependencies (listed in requirements.txt):

streamlit
google-generativeai (commented out in current version)
python-dotenv
langchain (optional, for future GenAI integration)
PyPDF2 (optional, for future text extraction from PDFs)
chromadb (optional, for potential future data visualization)
faiss-cpu (optional, for potential future data exploration)
pdf2image (optional, for future text extraction from PDFs)
sqlite3

## Project Structure:

text_2_sql/
├── README.md (this file)
├── requirements.txt
├── .env (optional, for storing environment variables)
├── main.py (Streamlit application script)
└── sqlite.py (SQLite database interaction script)

## How to Run:

### Step 1: Create a virtual environment named myvenv using the provided command:

```
$ conda create -n myvenv python==3.10 -y

```

### Step 2: Activate the virtual environment:
For bash/zsh
```
$ source activate myvenv  

```
For conda prompt
```
$ conda activate myvenv 

```
### Step 3: Install the dependencies:
```
$ pip install -r requirements.txt

```
### Step 4: Run the Streamlit app:
```
$ streamlit run main.py

```
## Additional Notes:

The current version of the code comments out the google-generativeai integration. If you want to use it, you'll need to set up an appropriate Google Cloud project and API key.
The listed optional dependencies are provided for your reference and can be included for future functionalities.

