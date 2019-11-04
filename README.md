# Sentence-search
Rest API to search and count for the number of times a word has occured in a sentence.

## Steps to run the code
Download the zip folder and unzip it in a desired folder.
From the command line navigate to the project folder's directory.
Have the file path for the text file ready.
Run the command
### FILE_PATH=<text_file_path> python3 -m sentence_search
This is an example command for the given file.
### FILE_PATH='/Users/maheshamruthaluri/convey/flask_sentence_search/example.txt' python -m sentence_search

## Running from the command line
### curl --globoff 'http://localhost:5000/count?word=eggplant'

## Running from the browser
### http://localhost:5000/count?word=eggplant