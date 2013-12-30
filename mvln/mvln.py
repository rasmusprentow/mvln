



import shutil,os, stat,shlex, ntpath,argparse,fileinput, sys



class MvLnFile:

	def __init__(self, src, dst):
		self.src = src
		self.dst = dst



class Converter:
	
	def __init__(self,str):
		self.str = str

	def getLines(self):
		return self.str.splitlines()

	def splitLine(line):
		srcdest = line.split(" ")
		return MvLnFile(srcdest[0],srcdest[1])

	def getFiles(self):
		files = []
		for line in self.getLines():
			files.append(Converter.splitLine(line))
		return files


class IsEqual:
	pass

class Mvln:

	def fromFilesSpec(fileSpec):
		pass


	def pathLeaf(path):
	    head, tail = ntpath.split(path)
	    return tail or ntpath.basename(head)

	#Copies from src to dst and create a link from dst to src. 
	def copyPreserved(src, dst):
	  file_stat = os.stat(src)
	  owner = file_stat[stat.ST_UID]
	  group = file_stat[stat.ST_GID]
	  mode = file_stat[stat.ST_MODE]

	  shutil.copytree(src, dst)
	  os.chown(dst, owner, group)
	  os.chmod(dst,mode)


	def mvAndLink(src,dst):
		if src is dst:
			raise IsEqual
		
		Mvln.copyPreserved(src,dst)
		if os.path.isdir(dst):

			shutil.rmtree(src)
			
			
			os.symlink(dst,src.rstrip('/'))
			#print("Removing tree {}".format(src))
		else:
			print("Destination: {} was not copied".format(dst))	
		

	def mvAndLinkFile(mvlnfile):
		Mvln.mvAndLink(mvlnfile.src,mvlnfile.dst)

		



def parseLine(line, verbose=False):
	mvlnfile = Converter.splitLine(line)
	if verbose:
		print("Moving {} to {} and creating link.....".format(mvlnfile.src, mvlnfile.dst))
	Mvln.mvAndLinkFile(mvlnfile)
	if verbose:
		print("Done!")


def main():
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

if  __name__ =='__main__':mains()