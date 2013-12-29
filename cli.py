#cli.py
#import fileinput, 

#for line in fileinput.input():
#	print(line);


#print("fdsdfdsf");
#f = open("files.conf", "r")

#for file in (shlex.split(f.read(), True)):
#	mvAndLink(os.getcwd()+"/test/old/"+pathLeaf(file))

from mvln import *

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--src", help="Source of the location your are moving, A link to dst from \"src will be created.")
parser.add_argument("--dst", help="Destination location.")
parser.add_argument("--file", help="File containing which files to move.")
args = parser.parse_args()

if args.file: 
	print ("Loading files to move from: " + args.file)
	Mvln.fromFile(args.file)
	sys.exit();

if args.src  and args.dst:
	if args.verbose:
		print("Creating symlink from "+ src.rstrip('/') + " poiting to " + dst)
	Mvln.mvAndLink(args.src, args.dst)