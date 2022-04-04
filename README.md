<div id="top"></div>
# cs5293sp22-project1

## Bhargav Durga Prasad Vummadi
## ID - 113541060


[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

<br />

<h2 align="center">The Redactor</h2>
<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#packages">Packages</a></li>
      </ul>
    </li>
    <li><a href="#how to run">How to run</a></li>
    <li><a href="#functionalities">Functionalities</a></li>
    <li><a href="#test cases">Test cases</a></li>
    <li><a href="#Assumptions">Assumptions</a></li>
    <li><a href="#Bugs">Bugs</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Whenever sensitive information is shared with the public, the data must go through a redaction process. That is, all sensitive names, places, and other sensitive information must be hidden. Documents such as police reports, court transcripts, and hospital records all contain sensitive information. Redacting this information is often expensive and time consuming. In the project I used data from Enrom email dataset, I took a small chunk of data and made four test files to redact based on various features like names, phone numbers, address, dates and concept. Storing the redacted files in a seperate directory given by the user. Finally a stats file is created which shows statistics of all redacted data.

Here's the overview of project:
<ul>
  <li> Getting input files</li>
  <li> Redacting features (--names --dates --phones --genders --address)</li>
  <li> Redacting based on concept </li>
  <li> Storing redacted data </li>
  <li> Writing the statistics to a file</li>
</ul>

Author Details
   <ul>
  <li> Author Name: Bhargav Vummadi </li>
  <li> EmailId: bhargav.vummadi@ou.edu </li>
  <li> OUID: 113541060</li>
   </ul>

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To start this project we need some prerequisties and installations.
To get the project up and running follow these simple example steps.

### Prerequisites

* First created a project structer as follows:
* ![image](https://user-images.githubusercontent.com/52027911/161438787-a46bcd76-4b65-4b1a-b683-53eaf19d24b2.png)


* Python 
  ```sh
  sudo apt install -y python3 ipython3 python3-pip
  ```
 * Input data for redacting the data.
 * I have taken some files from huge Enrom email dataset files.
 * Named them file_1.txt,file_2.txt,file_3.txt and file_4.txt.
 * Place them inside the project1/ folder.

  

### Packages 

_Below are the packages or modules that I have used in my project._

1. nltk
2. spacy
3. glob
4. re
5. shutil
6. os 
7. sys
8. argparse


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- HOW TO RUN -->
## How to run

In order to run you need to follow certain steps. Here is the step by step
explanation to run the project.

* First clone the project into your instance
  ```sh
    git clone https://github.com/bhargavvummadi/cs5293sp22-project1
  ```
* Change directory to cloned repository
  ```sh
     cd cs5293sp22-project1
  ```
* Now let's creata a virtual environment for our project using pipenv
  ```sh
    pipenv install
  ```
  Activate the virtual environment with `pipenv shell`
* Now we need to install required packages (if in case required)
  ```sh
    pipenv install nltk
    pipenv install spacy
    pipenv run python -m spacy download en_core_web_sm
    pipenv install pytest
  ```
* Running the project `main.py`
  ```sh
     pipenv run python project1/redactor.py --input '*.txt'  --names --dates --phones --address --gender --concept 'kids' --output 'files/' --stats stderr
  ```
  or 
  ```sh
     pipenv run python project1/redactor.py --input '*.txt'  --names --dates --phones --address --gender --concept 'kids' --output 'files/' --stats stats
  ```
  
  It will generate all redacted files and store them inside files/ folder with .redacted extension.
  
  There will be console output as below:
  ```sh
     Redacted File: file_3.txt and stored successfully
     *******************************************************************************************************************************************************************************************************
  Redacted File: file_2.txt and stored successfully
  **********************************************************************************************************************************************************************  **********************************
  Redacted File: file_1.txt and stored successfully
  ********************************************************************************************************************************************************************************************************
  Redacted File: file_4.txt and stored successfully
  ********************************************************************************************************************************************************************************************************
  ```
 * Running the pytests for the project with `pytest`
  ```sh
    pipenv run python -m pytest -v
  ```
 This command will run all the pytests and gives SUCCESS if all cases are passed.
 
  

_Hint Use 'rm -rf virtualenv_name' before creating a virtualenv with same name_

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Functionalities -->
## Functionalities
All the the files are placed insided project1 subfolder.
- [x] redactor.py
  This file uses argparse module to create custom command line arguments as --input, --concept, --output and --stats which are mandatory.
  I have used argparse attribute 'action' for making values not required for --names --dates --phones --genders --address cmd line attributes.
  It imports all other .py files as modules as calls each of their functionality.
  It passes all the values of command line arguments to main method
  - [ ] main(args)- method
         In this method it first checks for the previous stats file if it is present it removes it and creates a new one, else just creates a new one
         Similarly it checks for the output directory if it is previously created removes it using shutil and creates a new one.
         Takes all the inputs from glob objects
         Passes each file to a function in redactor_functions.py
- [x] redactor_functions.py
      I have used a list redactor approach, where I redacted contents of files based on each flag and pass the redacted data to
      the other flags which will use the redacted list and finally write redacted data to output files and store in a directory.
    - [ ] file_reader - It takes all the required arguments and file passed from main.py and reads the contents of file and 
          checks for what type of stats file and flags it. The contents of file and respective stats file and/or concept is 
          passed to subsequent methods.
    - [ ] redact_names - redacts names using spacy entities and en_web_core_sm module and returns redacted list op.Writes to stats file. 
    - [ ] redact_phone - redacts phone numbers using spacy rule based matching and regex and returns redacted list op. Writes to stats file.
    - [ ] redact_dates - redacts dates using spacy entities and en_web_core_sm and regex and returns redacted list op. Writes to stats file.
    - [ ] redact_gender - redacts gender using generalized gender list returns redacted list op. Writes to stats file. (tried lemmitization but results are not as expected so went with te gender-list).
    - [ ] redact_address - redacts addresses using generalized us state list regex and returns redacted list op. Writes to stats file.
    - [ ] redact_concept - redacts based on the concept. Here I used Stemmization on each word of the input file. I have using ```wordnet``` to
          get synonyms of concept that is passed. If any of the stemmized word is matched with any of the synonym of concept, I just redacted the
          entire sentence. I tought it is easiest way to do. Returns the redacted list op. Writes the stats file.
    - [ ] write_output - Takes the final redacted op list and writes it into filename.redacted.
  
 
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Test cases -->
## Test cases
I have tested all the functionalities in a single test file `test_redactor.py`.
I have used filetest.txt for testig purpose. Change code in test file for testing other file
change this line ```tf = "tests/filetest.txt" ``` to ```tf = "tests/INPUT_TEST_FILE" ```.
Generates fileteststats.txt stats output file.
- [x] test_redact_names(file_content,file_stat)
   Test and compares with the count of redacted names from stats file.
- [x] test_redact_phone(file_content,file_stat)
   Test and compares with the count of redacted phone numbers from stats file.
- [x] test_redact_date(file_content,file_stat)
   Test and compares with the count of redacted dates  from stats file.
- [x] test_redact_gender(file_content,file_stat)
   Test and compares with the count of redacted genders from stats file.
- [x] test_redact_address(file_content,file_stat)
   Test and compares with the count of redacted address from stats file.
- [x] test_redact_concept(file_content,concept,file_stat)
   Test and compares with the count of redacted concept lines from stats file.
- [x]  test_write_output(concept,output,new_stats)
  Tests whether the file is redacted and stored in the redact_test_files/ directory.
* I have re-used the stats file for testing by closing and opening after each method.
<p align="right">(<a href="#top">back to top</a>)</p>




<!-- Assumptions -->
## Assumptions

In this project to get all the flags redacted from the input fies, I have made some assumptions as follows:

1. Names are correctly redacted using spacy
2. Data is mostly from US based states.
3. The Address format is as follows 'Area name, state-short-name  zipcode'
4. Genders might come from the (gender_list)list I provided, if not we can add other items to the list to make it redact.
5. Concept synonym might match with one of following words in the file.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- Bugs -->
## Bugs

As explained above if my assumptions are wrong there might be the following bugs.

1. Irregular data format in input files.
2. Improper Address formats.
3. Names might be not redacted because of spacy entities
4. Some test files might not contain address or genders or phone numbers or concept.


One might can experience problems while running the project, If they haven't

* Installed required packages
* Duplicates in the virtual environments 

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

This is the list resources I found helpful and would like to give credit to. I've included them below

* [Python Docs](https://docs.python.org/)
* [W3 Schools](https://www.w3schools.com/python/python_file_remove.asp)
* [Kite](https://www.kite.com/python/answers/how-to-test-a-url-in-python)
* [Geeks for Geeks](https://www.geeksforgeeks.org/check-if-table-exists-in-sqlite-using-python/)
* [Towards datascience](https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da)
* [Medium](https://medium.com/@tusharsri/nlp-a-quick-guide-to-stemming-60f1ca5db49e)
* [W3Resource](https://www.w3resource.com/python-exercises/nltk/nltk-corpus-exercise-7.php)
* [Stackoverflow](https://stackoverflow.com/questions/12419998/find-numbers-in-a-sentence-by-regex)
* [GitHub README.md](https://github.com/othneildrew/Best-README-Template#about-the-project)
* [GitHub pytest Action](https://oudatalab.com/cs5293sp22/documents/ci) [It's not working because of installation of en_core_web_sm]

<p align="right">(<a href="#top">back to top</a>)</p>







