#argparse module is used for creating command line arguments while running python script

import argparse
import glob
import os
import redactor_functions

def main(args):
    '''
     unpacking the command line arguments from args
     like url and dbname and passing them to
     fetch
     dataextractor
     dboperations
     for their respective operations.
    '''
    ip = args.input
    concept =args.concept
    name = args.names
    date = args.dates
    phone = args.phones
    output = args.output
    stats = args.stats
    if os.path.exists(stats+".txt"):
        os.remove(stats+".txt")
    else:
        pass
    ip = 'project1/'+ip
    print(ip)
    files = glob.glob(ip)
    path = os.path.join('project1/',output)
    try:
        os.makedirs(path,exist_ok=True)
    except OSError as error:
        print(error)
    oppath= 'project1/'+output
    for f in files:
        redactor_functions.file_reader(f,concept,oppath,stats)






if __name__ == '__main__':
    '''
        Creating custom arguments like --incidents and passing a url 
        I have created another custom argument which is --dbname
        it is not required but we can create a db with user required name
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",
                        type=str,
                        required=True,
                        help="Input text Files")
    parser.add_argument("--names",
                        action='store_true',
                        help="Name Flag")
    parser.add_argument("--dates",
                        action='store_true',
                        help="Date Flag")
    parser.add_argument("--phones",
                        action='store_true',
                        help="Phone Flag")
    parser.add_argument("--genders",
                        action='store_true',
                        help="Gender Flag")
    parser.add_argument("--address",
                        action='store_true',
                        help="Address Flag")
    parser.add_argument("--concept",
                        type=str,
                        required=True,
                        help="Concept Word Flag")
    parser.add_argument("--output",
                        type=str,
                        required=True,
                        help="Output File Flag")
    parser.add_argument("--stats",
                        type=str,
                        required=True,
                        help="Status Flag")
    args = parser.parse_args()
    if (args.input!=None and args.names!=None and args.dates!=None and args.phones!=None and args.genders!=None and args.address!=None and args.concept!=None and args.output!=None and args.stats!=None):
        main(args)
    else:
        print(" Less number of arguments are passed")