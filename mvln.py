#mvln.py




import shutil,os, stat,shlex, ntpath


def pathLeaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def copyPreserved(src, dest):
  file_stat = os.stat(src)
  owner = file_stat[stat.ST_UID]
  group = file_stat[stat.ST_GID]
  mode = file_stat[stat.ST_MODE]

  shutil.copytree(src, dest)
  os.chown(dest, owner, group)
  os.chmod(dest,mode)

def mvAndLink(src):
	dest = os.getcwd()+"/tmptest/old/"+pathLeaf(src)+"/"

	copyPreserved(src,dest)
	if os.path.isdir(dest):

		shutil.rmtree(src)
		print("Creating symlink from "+ src.rstrip('/') + " poiting to " + dest)
		
		os.symlink(dest,src.rstrip('/'))
	else:
		print("Destination: "+ dest + " was not copied")	
	
	

