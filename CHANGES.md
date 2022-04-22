___
* Changed the file structer --- removed project1 folder and made redactor.py 
and redactor_functions.py kept under root directory. Here is the snapshot.
* Moved all the testfiles into docs folder if you want to test project with custom testfiles please do consider keeping inputfiles insides the **docs** directory and running the project
* Made changes in the redactor.py and redactor_functions.py , In redactor.py made changes to enable single flag testing, for instance passing name only flag and other flags which are mandatory.
* In redactor_functions.py I have added nltk for redacting names in addition to spacy, I have added more genders to gender_list to redact more genders.
* In tests folder I have changed the test_redactor.py to test all the functionalities.
* For stats file I have created a new function in redactor_functions.py and utilized sys module for writing to stderr or stdout and any other filename which is passed through console.
* My stats file consists of data for all the redacted names,genders,phone numbers,addresses, dates and concepts and their respective total count.
* while running the project it might ask for nltk and en_core_wb_sm, use the following commands
```
    pipenv install nltk
    pipenv install spacy
    pipenv run python -m spacy download en_core_web_sm
    pipenv install pytest
```
---
