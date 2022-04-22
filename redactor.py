#argparse module is used for creating command line arguments while running python script

import argparse
import glob
import os
import sys

import redactor_functions
import shutil

errr_arr = []

def main(args):
    '''
     unpacking the command line arguments from args
     like input files,concept,output directory and passing
     them to method of 
     file_reader
     which further calls other
     respective operations.
    '''
    names = args.names
    datess = args.dates
    phone_num = args.phones
    gender = args.genders
    address = args.address
    conceptt = args.concept
    '''
    #print("names datess phone_num gender address conceptt")
    #print(names,datess,phone_num
        ,gender
        ,address
        ,conceptt)
    '''
    ip = "docs/" + args.input
    errfl = 0
    #print('all the files')
    #print(ip)
    if os.path.exists(ip):
        pass
    else:
        errfl = 1
        #print("File Not Exsists give file present in docs/ folder through stderr")
        errr_arr.append("File Not Exsists give file present in docs/ folder through stderr")
    concept = args.concept
    output = args.output
    stats = args.stats
    if os.path.exists(stats):
        os.remove(stats)
    else:
        pass
    if stats == "stderr" and errfl == 1:
        sys.stderr.write(errr_arr[0])
    files = glob.glob(ip)
    path = os.path.join(output)
    if os.path.exists(path) and os.path.isdir(path):
        shutil.rmtree(path)

    try:
        os.makedirs(path, exist_ok=True)
    except OSError as error:
        print(error)
    oppath = output
    for f in files:
        #print("file that checked ")
        if "stats" in f or "stderr" in f or "stdout" in f:
            print("need not be redacted", f)
        else:

            redactor_functions.file_reader(f, names, datess, phone_num, gender,
                                           address, concept, oppath, stats)


if __name__ == '__main__':
    '''
        Creating custom arguments like --inputs,--concept,--output and --stats 
        which are mandatory and should have values other arguments are required
        just for flagging purpose and passed to main method.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",
                        type=str,
                        required=True,
                        help="Input text Files")
    parser.add_argument("--names", action='store_true', help="Name Flag")
    parser.add_argument("--dates", action='store_true', help="Date Flag")
    parser.add_argument("--phones", action='store_true', help="Phone Flag")
    parser.add_argument("--genders", action='store_true', help="Gender Flag")
    parser.add_argument("--address", action='store_true', help="Address Flag")
    parser.add_argument("--concept",
                        action='append',
                        type=str,
                        required=True,
                        help="Concept Word Flag")
    parser.add_argument("--output",
                        type=str,
                        required=True,
                        help="Output File Flag")
    parser.add_argument("--stats", type=str, required=True, help="Status Flag")
    args = parser.parse_args()
    if (args.input != None and args.names != None and args.dates != None
            and args.phones != None and args.genders != None
            and args.address != None and args.concept != None
            and args.output != None and args.stats != None):
        main(args)
    else:
        print(" Less number of arguments are passed")
