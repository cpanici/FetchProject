# Fetch Programming Exercise
## Pyramid Word Tool
### Christian Panici

### Functionality:

This tool creates a simple web interface for checking if a given word is a "pyramid word".

The user enters a word, and after submitting, a message displays stating whether their input meets the criteria or not.

A word is a **pyramid word** if you can arrange the letters in increasing frequency, starting with 1 and continuing without gaps and without duplicates.


### To Run:

1. Clone repository.

2. Navigate to local copy.

3. Install required dependencies:

>> pip install -r requirements.txt

4. Set FLASK-APP environment variable.

>> set FLASK_APP=app.py

5. Run Flask application.

>> flask run

6. Navigate to http://127.0.0.1:5000/ in preferred web browser.


### Sample Usage:

**User Input:** banana
**Output:** banana is a pyramid word!
**Reason:** 1 'b', 2 'n's, and 3 'a's

**User Input:** bandana
**Output:** bandana is not a pyramid word.
**Reason:** 1 'b' and 1 'd'

### Technologies:

This tool was mainly written in Python with the Flask web framework. Webpages were written in HTML and styled with CSS.
