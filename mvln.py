#mvln.py




import shutil,os, stat,shlex, ntpath

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
		

		Mvln.copyPreserved(src,dst)
		if os.path.isdir(dst):

			shutil.rmtree(src)
			
			
			os.symlink(dst,src.rstrip('/'))
		else:
			print("Destination: "+ dst + " was not copied")	
		
		

