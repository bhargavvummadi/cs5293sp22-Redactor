<div id="top"></div>
# cs5293sp22-project1

## Bhargav Durga Prasad Vummadi
## ID - 113541060


[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

<br />

<h2 align="center">Redactor</h2>
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

Norma police department basically collects daily activity reports based on arrests, incidents,case summaries.
These data is stored in pdf format for every day and can be deleted and modified into a monthly summaries. But,
in this project we aim at only collecting the incidents data which is stored in pdf format. When a url is provided
we need to fetch the data and make some data cleaning and adjustments and make a database to store this data. Finally
we can see the pipe '|' seperated data on the console which sorted alphabetically on nature and sorted based on number
of times it has occured.

Here's the over:
<ul>
  <li> Fetching url responose</li>
  <li> Getting data from url blob object</li>
  <li> Creating Database and incidents table </li>
  <li> Inserting Data </li>
  <li> Printing pipe seperated and sorted data </li>
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
* ![image](https://user-images.githubusercontent.com/52027911/157352583-9a8a99a5-f18d-4926-a81f-bb504a948025.png)

* Python 
  ```sh
  sudo apt install -y python3 ipython3 python3-pip
  ```
 * Norman PD incidents pdf.
   I have decided to used some particular file and used them in my project. I have used github css5293sp22 repo (as it is public and github doesn't charge for storing files)
   my own to store this pdfs and access them rather than continuously hitting the norman pd website.
  ```sh
    https://github.com/bhargavvummadi/cs5293sp22/raw/main/2022-01-03_daily_incident_summary.pdf
    https://github.com/bhargavvummadi/cs5293sp22/raw/main/2022-01-26_daily_incident_summary.pdf
  ```
  

### Packages 

_Below are the packages or modules that I have used in my project._

1. pipenv
2. black
3. urllib.response
4. tempfiles
5. pypdf2
6. re
7. sqlite3
8. os 
9. sys
10. pytest

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- HOW TO RUN -->
## How to run

In order to run you need to follow certain steps. Here is the step by step
explanation to run the project.

* First clone the project into your instance
  ```sh
    git clone https://github.com/bhargavvummadi/cs5293sp22-project0
  ```
* Change directory to cloned repository
  ```sh
     cd cs5293sp22-project0
  ```
* Now let's creata a virtual environment for our project using pipenv
  ```sh
    pipenv install
  ```
  Activate the virtual environment with `pipenv shell`
* Now we need to install required packages (if in case required)
  ```sh
    pipenv install PyPDF2
    pipenv install pytest
  ```
* Running the project `main.py`
  ```sh
    pipenv run python project0/main.py --incidents "https://github.com/bhargavvummadi/cs5293sp22/raw/main/2022-01-03_daily_incident_summary.pdf"
  ```
  It will generate output with pipe seperated data as below:
  ```sh
     Abdominal Pains/Problems | 2
     Alarm | 12  
     Alarm Holdup/Panic | 2
     Animal Complaint | 2
     Animal Dead | 2
     Animal Injured | 1
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
All the the files are placed insided project0 subfolder.
- [x] main.py
  This file uses argparse module to create custom command line arguments like --incidents which is mandatory followed by url.
  I have added --dbname argument so that user can give custom name to create database --dbname "oupd.db".
  It imports all other .py files as modules as calls each of their functionality.
- [x] fetch.py
  This file uses urllib.requests module to get a valid response as a blob object
  Returns the object to dataextractor
- [x] dataextractor.py
    It uses pypdf2,re and tempfiles modules.
    The main functionality is to get data page by page using pypdf2 package.
    Then I used list of lists to stored the incidents data in the required format. 
    (logic is simple - once cracked) 😄 
    Managed double liners and replaced empty cell with 'NaN' value.
    Returns a list containing many lists.
- [x] dboperations.py
    - [ ] createdb - creates a database with incidents table and returns db name
    - [ ] populatedb - inserts incident data into table
    - [ ] status - sorts data first based on nature count and then alphabetically, finally
    prints in pipe seperated format. 
 
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- Test cases -->
## Test cases
I have tested all the functionalities in a single test file `test_main.py`.
- [x] test_fetch_operation(url)
   Tests whether url returns a valid reposne code(200) or not.
- [x]  test_data_extraction(...)
  This function takes five attributes of file and checks whether the 
  data is present in the given pdf or not, also asserts data is retrived is 
  not none.
- [x] create_db()
    Tests whether the created table is present in database or not.
- [x] test_for_populate()
    Tests whether data is inserted or not with `SELECT` query. 
- [x] test_for_status()
    Tests whether data is sorted alphabetically or not
    Tests whether data is pipe sepaerated or not
<p align="right">(<a href="#top">back to top</a>)</p>




<!-- Assumptions -->
## Assumptions

In this project to clear the edge cases of both double liners and empty cells, I have made two assumptions as follows:

1. A double liner always contains capital letters in it and it occurs in only 3 column.
2. All the empty cells are present in only 3 and 4 columns

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- Bugs -->
## Bugs

As explained above if my assumptions are wrong there might be the following bugs.

1. Irregular data slicing.
2. Improper 'NaN' value insertions.

One might can experience problems while running the project, If they haven't

* Installed required packages
* Duplicates in the virtual environments 

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

This is the list resources I found helpful and would like to give credit to. I've included them below

* [Python Docs](https://docs.python.org/)
* [W3 Schools](https://www.w3schools.com/python/python_regex.asp)
* [Kite](https://www.kite.com/python/answers/how-to-test-a-url-in-python)
* [Geeks for Geeks](https://www.geeksforgeeks.org/check-if-table-exists-in-sqlite-using-python/)
* [Stackoverflow](https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada?answertab=scoredesc#tab-top)
* [GitHub README.md](https://github.com/othneildrew/Best-README-Template#about-the-project)
* [GitHub pytest Action](https://oudatalab.com/cs5293sp22/documents/ci)

<p align="right">(<a href="#top">back to top</a>)</p>







