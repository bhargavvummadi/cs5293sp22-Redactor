# nltk has all required methods and techniques for natural language processing
import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet
from nltk.stem.porter import *

# used for os operations
import os
import sys
# used for extracting from text files using specified patterns
import re

#Simple and very useful library for doing text and nlp operations
import spacy
from spacy.matcher import Matcher
import en_core_web_sm


#Global flags

stderr_file = 0
stdout_file = 0
concept_count = 0


def file_reader(filename,names,datess,phone_num,gender,address,concept, output, stats):
    '''
       File_reader takes the following parameters
       Parameters
       --------------------------------------
       filename - Each filename from glob object
       concept - The concept to be redacted
       output - output directory to store redacted files
       stats - stats file to store statistics of all redacted files
       ------------------------------------------
       calls all other functions and gets redacted output and
       the output redacted list is used in the consectuive 
       functions.
    '''
    print("names datess phone_num gender address conceptt")
    print(names, datess, phone_num
          , gender
          , address
          , concept)
    file = open(filename, 'r')
    stats_file = stats
    write_stats_file = open(stats_file, "a", encoding="utf-8")
    content = file.readlines()

    wanted_filename = str(filename).split('/')[0]
    print("wanted filename")
    print(filename)
    print(wanted_filename)


    if stats_file == "stderr":
        stderr_file = 1
        sys.stderr.write(wanted_filename + "\n")
        sys.stderr.write('*' * 100 + "\n")
    elif stats_file == "stdout":
        sys.stdout.write(wanted_filename + "\n")
        sys.stdout.write('*' * 100 + "\n")
        stdout_file = 1
    else:
        write_stats_file.write(wanted_filename + "\n")
        write_stats_file.write('*' * 100 + "\n")

    if names == True:
        op = redact_name(content, write_stats_file)
    if phone_num == True:
        op = redact_phone(op, write_stats_file)
    if datess == True:
        op = redact_date(op, write_stats_file)
    if gender == True:
        op = redact_gender(op, write_stats_file)
    if address == True:
        op = redact_address(op, write_stats_file)
    if len(concept) > 0 or concept==True:
        for i in concept:
            op = redact_concept(op, str(i), write_stats_file)
    write_output(output, op, wanted_filename)

    print('Redacted File:',wanted_filename, 'and stored successfully')
    print('*'*200)


def redact_name(file_content, write_stats_file):
    '''
        This method redact_name takes the following parameters
        as input
        Parameters
        ------------------------------------------------------
        file_content - actual content of the file
        write_stats_file - Write status file 
        -----------------------------------------------------
        Using spacy redacted with '\u2588' 
        based up on token.ent_type
        Return
        -----------------------------------------------------
        Redacted output list
    '''
    nlp_obj = spacy.load("en_core_web_sm")
    op = []
    name_count = 0
    for l in file_content:
        doc = nlp_obj(l)
        for token in doc:
            if token.ent_type_ == 'PERSON' or token.ent_type_ == 'GPE':
                if stderr_file == 1:
                    sys.stderr.write(token.ent_type_ + "---" + token.text + "\n")
                elif stdout_file == 1:
                    sys.stdout.write(token.ent_type_ + "---" + token.text + "\n")
                else:
                    write_stats_file.write(token.ent_type_ + "---" + token.text +
                                       "\n")
                name_count = name_count + 1
                for i in range(len(token)):
                    op.append('\u2588')
                op.append(" ")
            else:
                op.append(token.text)
                op.append(" ")
    if stderr_file == 1:
        sys.stderr.write(" NAME COUNT: " + str(name_count) + "\n")
    elif stdout_file == 1:
        sys.stdout.write(" NAME COUNT: " + str(name_count) + "\n")
    else:
        write_stats_file.write(" NAME COUNT: " + str(name_count) + "\n")


    return op


def redact_phone(file_content, write_stats_file):
    '''
        This method redact_phone takes the following parameters
        as input
        Parameters
        ------------------------------------------------------
        file_content - actual content of the file
        write_stats_file - Write status file
        -----------------------------------------------------
        Using spacy redacted with '\u2588'
        based up on matched pattern using spacy
        rule-based matching and some regex patterns
        Returns
        ----------------------------------------------------
        Redacted output list
    '''
    phone_number_count = 0
    nlp_obj = spacy.load("en_core_web_sm")
    pattern1 = [{
        "ORTH": "+",
        "OP": "?"
    }, {
        "SHAPE": {
            "REGEX": "[1-9]{1}"
        },
        "OP": "?"
    }, {
        "ORTH": "(",
        "OP": "?"
    }, {
        "SHAPE": "ddd"
    }, {
        "ORTH": ")",
        "OP": "?"
    }, {
        "SHAPE": "ddd"
    }, {
        "ORTH": "-",
        "OP": "?"
    }, {
        "SHAPE": "dddd"
    }]
    matcher = Matcher(nlp_obj.vocab)
    matcher.add("Phone", [pattern1])
    flag = 0
    op = []
    temp = str()
    kemp = str()
    lastmissingline = str()
    pattern2 = re.compile(r"[+]?\d{1}-\d{3,5}-\d{3,5}-\d{3,5}")
    pattern3 = re.compile(r"\s*?\d{3,5}\s+\d{3,5}\s+\d{3,5}")
    for i in range(len(file_content) - 1, 0, -1):
        if file_content[i] == '\n':
            ll = kemp.strip().split(" ")
            lastmissingline = " ".join(ll[::-1])
            break
        else:
            kemp += file_content[i]
    for t in file_content:
        flag = 0
        if t == '\n':
            temp += '\n'
            temp_temp = temp
            temp_temp = temp_temp.replace(" ", "")
            temp_temp2 = " ".join(re.findall(r"\d+", temp))
            if (re.search(pattern2, temp_temp)):
                if stderr_file ==1:
                    sys.stderr.write("PHONE-NUMBER" + "---" + temp_temp +
                                           "\n")
                elif stdout_file == 1:
                    sys.stdout.write("PHONE-NUMBER" + "---" + temp_temp +
                                           "\n")
                else:
                    write_stats_file.write("PHONE-NUMBER" + "---" + temp_temp +
                                       "\n")
                phone_number_count += 1
                flag = 1
                for i in range(len(temp)):
                    op.append('\u2588')
                op.append("\n")
            elif (re.search(pattern3, temp_temp2)):
                write_stats_file.write("PHONE-NUMBER" + "---" + temp_temp +
                                       "\n")
                flag = 1
                phone_number_count += 1
                for i in range(len(temp)):
                    op.append('\u2588')
                op.append("\n")

            doc = nlp_obj(temp)
            matches = matcher(doc)
            for match_id, start, end in matches:
                flag = 1
                for i in range(1, start):
                    op.append(doc[i].text)
                op.append(" ")
            if flag == 1:
                for match_id, start, end in matches:
                    span = doc[start:end]
                    phone_number_count += 1
                    write_stats_file.write("PHONE-NUMBER" + "---" +
                                           span.text.strip() + "\n")
                    for k in span.text.strip():
                        op.append('\u2588')
                    op.append("\n")
            else:
                op.append(temp)
                op.append(" ")
            temp = str()
        else:
            temp += t

    lastmissingline_temp = lastmissingline
    lastmissingline_temp = lastmissingline_temp.replace(" ", "")
    lastmissingline_temp2 = " ".join(re.findall(r"\d+", lastmissingline))
    if (re.search(pattern2, lastmissingline_temp)):
        phone_number_count += 1
        write_stats_file.write("PHONE-NUMBER" + "---" + lastmissingline_temp +
                               "\n")
        for i in range(len(lastmissingline)):
            op.append('\u2588')
        op.append(" ")
    elif (re.search(pattern3, lastmissingline_temp2)):
        phone_number_count += 1
        write_stats_file.write("PHONE-NUMBER" + "---" + lastmissingline_temp +
                               "\n")
        for i in range(len(lastmissingline)):
            op.append('\u2588')
        op.append(" ")
    else:
        op.append(lastmissingline)

    if stderr_file == 1:
        sys.stderr.write(" PHONE-NUMBER-COUNT: " + str(phone_number_count) +
                               "\n")
    elif stdout_file == 1:
        sys.stdout.write(" PHONE-NUMBER-COUNT: " + str(phone_number_count) +
                               "\n")
    else:
        write_stats_file.write(" PHONE-NUMBER-COUNT: " + str(phone_number_count) +
                           "\n")
    #print("".join(op))
    return op


def redact_date(file_content, write_stats_file):
    '''
        This method redact_date takes the following parameters
        as input
        Parameters
        ------------------------------------------------------
        file_content - actual content of the file
        write_stats_file - Write status file
        -----------------------------------------------------
        Using spacy redacted with '\u2588'
        based up on matched pattern using spacy
        rule-based matching and some regex patterns
        Returns
        ----------------------------------------------------
        Redacted output list
    '''
    date_count = 0
    nlp_obj = spacy.load("en_core_web_sm")
    op = []
    for l in file_content:
        doc = nlp_obj(l)
        for token in doc:
            #print(token,token.ent_type_)
            all = re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", token.text)
            all2 = re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{2}", token.text)
            all3 = re.findall(r"[\d]{1,2} [ADFJMNOS]\w* [\d]{4}", token.text)
            all4 = re.findall(r"[\d]{1,2} [adfjmnos]\w* [\d]{4}", token.text)
            if token.ent_type_ == 'DATE' or len(all) > 0 or len(
                    all2) > 0 or len(all3) > 0 or len(all4) > 0:
                date_count += 1
                if stderr_file ==1:
                    sys.stderr.write("DATE" + "---" + token.text + "\n")
                elif stdout_file == 1:
                    sys.stdout.write("DATE" + "---" + token.text + "\n")
                else:
                    write_stats_file.write("DATE" + "---" + token.text + "\n")
                for i in range(len(token.text)):
                    op.append('\u2588')
                op.append(" ")
            else:
                op.append(token.text)
                op.append(" ")
    if stderr_file == 1:
        sys.stderr.write("DATE-COUNT: " + str(date_count) + "\n")
    elif stdout_file == 1:
        sys.stdout.write("DATE-COUNT: " + str(date_count) + "\n")
    else:
        write_stats_file.write("DATE-COUNT: " + str(date_count) + "\n")
    #print("".join(op))
    return op


def redact_gender(file_content, write_stats_file):
    '''
        This method redact_gender takes the following parameters
        as input
        Parameters
        ------------------------------------------------------
        file_content - actual content of the file
        write_stats_file - Write status file
        -----------------------------------------------------
        Using spacy redacted with '\u2588'
        based up on matched list elements
        using a generalized gender_list
        Returns
        ----------------------------------------------------
        Redacted output list
    '''
    gender_count = 0
    nlp_obj = spacy.load("en_core_web_sm")
    '''
    pattern = [{"LOWER": "she"}, {"LEMMA": "he"}, {"LEMMA": "her"},{"LEMMA": "him"},{"LEMMA": "his"}, {"text":"father"},
               {"text":"mother"},{"LEMMA":"man"},{"LEMMA":"men"},{"LEMMA":"male"}]
    matcher = Matcher(nlp_obj.vocab)
    matcher.add("gender", [pattern])
    '''
    gender_list = [
        "she", "he", "him", "her", "his", "father", "mother", "man", "woman",
        "men", "women", "male", "female", "herself", "himself"
    ]
    op = []
    for l in file_content:
        doc = nlp_obj(l)
        '''
        matches = matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            print(span)
        '''
        for token in doc:
            #print(token,token.ent_type_)
            if token.ent_type_ == 'PERSON' or token.ent_type_ == 'GPE' or token.text.lower(
            ) in gender_list:
                if token.text.lower() in gender_list:
                    gender_count += 1
                    if stderr_file ==1:
                        sys.stderr.write("GENDER" + "---" +
                                               token.text.lower() + "\n")
                    elif stdout_file ==1:
                        sys.stdout.write("GENDER" + "---" +
                                               token.text.lower() + "\n")
                    else:
                        write_stats_file.write("GENDER" + "---" +
                                           token.text.lower() + "\n")
                for i in range(len(token)):
                    op.append('\u2588')
                op.append(" ")
            else:
                op.append(token.text)
                #op.append(" ")
    #print("".join(op))
    if stderr_file==1:
        sys.stderr.write("GENDER-COUNT :" + str(gender_count) + "\n")
    elif stdout_file==1:
        sys.stdout.write("GENDER-COUNT :" + str(gender_count) + "\n")
    else:
        write_stats_file.write("GENDER-COUNT :" + str(gender_count) + "\n")
    return op


def redact_address(file_content, write_stats_file):
    '''
        This method redact_address takes the following parameters
        as input
        Parameters
        ------------------------------------------------------
        file_content - actual content of the file
        write_stats_file - Write status file
        -----------------------------------------------------
        Using spacy redacted with '\u2588'
        based up on list based matching and
        some regex patterns
        Returns
        ----------------------------------------------------
        Redacted output list
    '''
    address_count = 0
    nlp_obj = spacy.load("en_core_web_sm")
    op = []
    us_states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    temp = ""
    kemp = str()
    lastmissingline = str()
    pattern1 = re.compile(r"\d{3}\s[a-zA-Z]+\s[a-zA-Z]+")
    pattern2 = re.compile(r"[a-zA-Z]+(,)?\s+[a-zA-Z]+\s+\d{5}")
    for i in range(len(file_content) - 1, 0, -1):
        if file_content[i] == '\n':
            ll = kemp.strip().split(" ")
            lastmissingline = " ".join(ll[::-1])
            break
        else:
            kemp += file_content[i]

    for i in range(len(file_content)):
        if file_content[i] == '\n':
            temp += "\n"
            ll = temp.strip().split(" ")
            if (re.search(pattern1, temp)):
                address_count += 1
                if stderr_file ==1:
                    sys.stderr.write("ADDRESS" + "---" + temp + "\n")
                elif stdout_file == 1:
                    sys.stdout.write("ADDRESS" + "---" + temp + "\n")
                else:
                    write_stats_file.write("ADDRESS" + "---" + temp + "\n")
                for i in range(len(temp)):
                    op.append('\u2588')
                op.append("\n")
            #print(op)
            elif (re.search(pattern2, temp)):
                tl = temp.split(" ")
                if set(tl).intersection(set(us_states.keys())):
                    address_count += 1
                    write_stats_file.write("ADDRESS" + "---" + temp + "\n")
                    for i in range(len(temp)):
                        op.append('\u2588')
                    op.append("\n")
            else:
                op.append(temp)
                #op.append(" ")
            temp = str()
        else:
            temp += file_content[i]

    op.append(lastmissingline)
    if stderr_file==1:
        sys.stderr.write("ADDRESS-COUNT :" + str(address_count) + "\n")
    elif stdout_file ==1:
        sys.stdout.write("ADDRESS-COUNT :" + str(address_count) + "\n")
    else:
        write_stats_file.write("ADDRESS-COUNT :" + str(address_count) + "\n")
    #print("".join(op))
    return op


def redact_concept(file_content, concept, write_stats_file):
    '''
        This method redact_concept takes the following parameters
        as input
        Parameters
        ------------------------------------------------------
        file_content - actual content of the file
        write_stats_file - Write status file
        concept - a word used to redact any matched concept
        -----------------------------------------------------
        Using spacy redacted with '\u2588'
        based up on stemmization and 
        synonym extractions and matching
        Returns
        ----------------------------------------------------
        Redacted output list
    '''

    op = []
    bl_flag  = False
    synonyms = []
    for syn in wordnet.synsets(concept):
        for l in syn.lemmas():
            synonyms.append(l.name())

    synonyms = set(synonyms)
    flag = 0

    req = "".join(file_content)
    porterStemmer = PorterStemmer()
    for l in req.split('\n'):
        flag = 0
        for r in l.split('.'):
            wl = nltk.word_tokenize(r)
            for w in wl:
                if str(w) in synonyms:
                    bl_flag = True
            sw = [porterStemmer.stem(w) for w in wl]
            for token in sw:
                if str(token) in synonyms or bl_flag == True:
                    bl_flag = False
                    #print("Foud a match")
                    flag = 1
                    global concept_count
                    concept_count += 1
                    if stderr_file ==1:
                        sys.stderr.write("CONCEPT" + "---" + r + "\n")
                    elif stdout_file ==1:
                        sys.stdout.write("CONCEPT" + "---" + r + "\n")
                    else:
                        write_stats_file.write("CONCEPT" + "---" + r + "\n")
                    #print(token)
            if flag == 1:
                for i in range(len(r)):
                    op.append('\u2588')
                op.append("\n")
        if flag != 1:
            op.append(l)
            op.append("\n")
    if stderr_file ==1:
        sys.stderr.write("CONCEPT-COUNT :" + str(concept_count) + "\n")
        sys.stderr.write('*' * 200 + '\n')
    elif stdout_file ==1:
        sys.stdout.write("CONCEPT-COUNT :" + str(concept_count) + "\n")
        sys.stdout.write('*' * 200 + '\n')
    else:
        write_stats_file.write("CONCEPT-COUNT :" + str(concept_count) + "\n")
        write_stats_file.write('*' * 200 + '\n')
    #print("".join(op))
    return op


def write_output(dirr, res, filename):
    '''
        This method write_output takes the following parameters
        as input
        Parameters
        ------------------------------------------------------
        dirr - Directory to store redacted files
        res - redacted output list
        filename - to store filename.redacted
        -----------------------------------------------------
        writing the files to passed directory under
        filename.redacted
        ----------------------------------------------------
    '''
    #print("".join(res))
    filename = str(filename).split('.')[0]
    req_file = filename + '.redacted'
    op_file = open(dirr + req_file, "w", encoding="utf-8")
    op_file.write("".join(res))
    op_file.close()
