#mvln.py




import shutil,os, stat,shlex, ntpath


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

		

