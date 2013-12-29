#cli.py
#import fileinput, 

#for line in fileinput.input():
#	print(line);


#print("fdsdfdsf");
#f = open("files.conf", "r")

#for file in (shlex.split(f.read(), True)):
#	mvAndLink(os.getcwd()+"/test/dst/"+pathLeaf(file))

from mvln import *


import argparse,fileinput, sys

def parseLine(line, verbose=False):
	mvlnfile = Converter.splitLine(line)
	if verbose:
		print("Moving {} to {} and creating link.....".format(mvlnfile.src, mvlnfile.dst))
	Mvln.mvAndLinkFile(mvlnfile)
	if verbose:
		print("Done!")

######## Check if stdin is used

if  not sys.stdin.isatty():
	for line in fileinput.input():
		parseLine(line, True)
	fileinput.close()
	sys.exit()

######## Use normal argument parsing

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("--src", help="Source of the location your are moving, A link to dst from \"src will be created.")
group.add_argument("--file", help="File containing which files to move.")
parser.add_argument("--dst", help="Destination location.")

parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()

if args.file: 
	if args.verbose:
		print ("Loading files to move from: " + args.file)
	for line in open(args.file):
		parseLine(line, args.verbose)	
	sys.exit();

if args.src  and args.dst:
	if args.verbose:
		print("Creating symlink from "+ args.src.rstrip('/') + " poiting to " + args.dst)
	Mvln.mvAndLink(args.src, args.dst)