import os
import sys
#using os and sys to set the system path
import pytest
import shutil
import redactor_functions



import redactor_functions

tf = "tests/filetest.txt"

tf_f = open(tf, 'r')
content = tf_f.readlines()


@pytest.fixture()
def file_content():
    return content




@pytest.fixture()
def concept():
    return "kids"


def test_redact_names(file_content):
    '''
      test_redact_names takes following parameters
      -----------------------------------------------
      file_content - contents of the input file
      file_stat - stats text file to test
      ----------------------------------
      asserts count of redacted names
    '''
    op = redactor_functions.redact_name(file_content)
    red_flag =0
    for i in op:
        if i == '\u2588':
            red_flag = 1
            break

    assert red_flag > 0





def test_redact_phone(file_content):
    '''
          test_redact_phone takes following parameters
          -----------------------------------------------
          file_content - contents of the input file
          file_stat - stats text file to test
          ----------------------------------
          asserts count of redacted phone numbers
    '''
    op = redactor_functions.redact_phone(file_content)
    for i in op:
        if i == '\u2588':
            red_flag = 1
            break

    assert red_flag > 0




def test_redact_date(file_content):
    '''
          test_redact_date takes following parameters
          -----------------------------------------------
          file_content - contents of the input file
          file_stat - stats text file to test
          ----------------------------------
          asserts count of redacted dates
    '''
    op = redactor_functions.redact_date(file_content)
    for i in op:
        if i == '\u2588':
            red_flag = 1
            break

    assert red_flag > 0




def test_redact_gender(file_content):
    '''
          test_redact_gender takes following parameters
          -----------------------------------------------
          file_content - contents of the input file
          file_stat - stats text file to test
          ----------------------------------
          asserts count of redacted genders
    '''
    op = redactor_functions.redact_gender(file_content)
    for i in op:
        if i == '\u2588':
            red_flag = 1
            break

    assert red_flag > 0




def test_redact_address(file_content):
    '''
          test_redact_address takes following parameters
          -----------------------------------------------
          file_content - contents of the input file
          file_stat - stats text file to test
          ----------------------------------
          asserts count of redacted addresses
    '''
    op = redactor_functions.redact_address(file_content)
    for i in op:
        if i == '\u2588':
            red_flag = 1
            break

    assert red_flag > 0


@pytest.fixture()
def concept6():
    return "kids"



def test_redact_concept(file_content, concept6):
    '''
          test_redact_names takes following parameters
          -----------------------------------------------
          file_content - contents of the input file
          concept - concepted to be redacted
          file_stat - stats text file to test
          ----------------------------------
          asserts count of redacted concept sentences
    '''


    op = redactor_functions.redact_concept(file_content, concept6)
    for i in op:
        if i == '\u2588':
            red_flag = 1
            break

    assert red_flag > 0

@pytest.fixture()
def new_stats():
    return "stats_output.txt"

@pytest.fixture()
def output():
    return "redact_test_files/"

def test_write_output(concept,output,new_stats):
    '''
          test_write_output takes following parameters
          -----------------------------------------------
          concept
          output - Directory
          new_stats - stats file
          ----------------------------------
          asserts the exsistance of the output redacted file
    '''
    if os.path.exists(new_stats):
        os.remove(new_stats)
    else:
        pass
    path = os.path.join('tests/', output)
    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as error:
        print(error)
    oppath = 'tests/' + output
    redactor_functions.file_reader(tf, True, True, True, True, True, concept, oppath, new_stats)

    test_file_flag = 0

    if os.path.exists(path+"filetest.txt.redacted"):
        test_file_flag = 1

    assert test_file_flag > 0

def test_stats_output(new_stats):
    found = 0
    if os.path.exists(new_stats):
        found = 1
    assert  found > 0