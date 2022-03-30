import os
import sys
#using os and sys to set the system path
import pytest

sys.path.append(os.getcwd() + '/project1')

from project1 import redactor_functions

tf = "tests/filetest.txt"
ts = "fileteststats.txt"

tf_f = open(tf, 'r')
if os.path.exists(ts):
    os.remove(ts)
else:
    pass
ts_f = open(ts, "a", encoding="utf-8")
ts_f.write(ts + "\n")
ts_f.write('*' * 100 + "\n")
content = tf_f.readlines()


@pytest.fixture()
def file_content():
    return content


@pytest.fixture()
def file_stat():
    return ts_f


@pytest.fixture()
def concept():
    return "kids"


def test_redact_names(file_content, file_stat):
    op = redactor_functions.redact_name(file_content, file_stat)
    file_stat.close()
    ts_f = open(ts, 'r')
    req_count = 0
    for l in ts_f:
        if l.strip().startswith("NAME COUNT"):
            req_count = int(l.split(":")[1])
            break
    ts_f.close()
    assert req_count > 0


ts_f2 = open(ts, "a", encoding="utf-8")


@pytest.fixture()
def file_stat2():
    return ts_f2


def test_redact_phone(file_content, file_stat2):
    op = redactor_functions.redact_phone(file_content, file_stat2)
    file_stat2.close()
    ts_f = open(ts, 'r')
    req_count = 0
    for l in ts_f:
        if l.strip().startswith("PHONE-NUMBER-COUNT"):
            req_count = int(l.split(":")[1])
            break
    ts_f.close()
    assert req_count > 0


ts_f3 = open(ts, "a", encoding="utf-8")


@pytest.fixture()
def file_stat3():
    return ts_f3


def test_redact_date(file_content, file_stat3):
    op = redactor_functions.redact_date(file_content, file_stat3)
    file_stat3.close()
    ts_f = open(ts, 'r')
    req_count = 0
    for l in ts_f:
        if l.strip().startswith("DATE-COUNT"):
            req_count = int(l.split(":")[1])
            break
    ts_f.close()
    assert req_count > 0


ts_f4 = open(ts, "a", encoding="utf-8")


@pytest.fixture()
def file_stat4():
    return ts_f4


def test_redact_gender(file_content, file_stat4):
    op = redactor_functions.redact_gender(file_content, file_stat4)
    file_stat4.close()
    ts_f = open(ts, 'r')
    req_count = 0
    for l in ts_f:
        if l.strip().startswith("GENDER-COUNT"):
            req_count = int(l.split(":")[1])
            break
    ts_f.close()
    assert req_count > 0


ts_f5 = open(ts, "a", encoding="utf-8")


@pytest.fixture()
def file_stat5():
    return ts_f5


def test_redact_address(file_content, file_stat5):
    op = redactor_functions.redact_address(file_content, file_stat5)
    file_stat5.close()
    ts_f = open(ts, 'r')
    req_count = 0
    for l in ts_f:
        if l.strip().startswith("ADDRESS-COUNT"):
            req_count = int(l.split(":")[1])
            break
    ts_f.close()
    assert req_count > 0


ts_f6 = open(ts, "a", encoding="utf-8")


@pytest.fixture()
def file_stat6():
    return ts_f6


def test_redact_concept(file_content, concept, file_stat6):
    op = redactor_functions.redact_concept(file_content, concept, file_stat6)
    file_stat6.close()
    ts_f = open(ts, 'r')
    req_count = 0
    for l in ts_f:
        if l.strip().startswith("CONCEPT-COUNT"):
            req_count = int(l.split(":")[1])
            break
    ts_f.close()
    assert req_count > 0
