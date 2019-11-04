# Sentence-search
Rest API to search and count for the number of times a word has occured in a sentence.

## Steps to run the code
Download the zip file and unzip it in a desired folder.
From the command line navigate to the project folder's directory.
Have the file path for the text file ready.

### Install requirements and dependencies
Assuming python3 is installed run the following command to install virtual env
1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt

Run the command
### FILE_PATH=<text_file_path> python3 -m sentence_search
This is an example command for the given file.
### FILE_PATH='/Users/username/convey/flask_sentence_search/example.txt' python3 -m sentence_search

## Running from the command line
### curl --globoff 'http://localhost:5000/count?word=eggplant'

## Running from the browser
### http://localhost:5000/count?word=eggplant