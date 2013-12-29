#converter.py

class MvLnFile:

	def __init__(self, src, dst):
		self.src = src
		self.dst = dst



class Converter:
	
	def __init__(self,str):
		self.str = str

	def getLines(self):
		return self.str.splitlines()

	def getFiles(self):
		files = []
		for line in self.getLines():
			srcdest = line.split(" ")
			files.append(MvLnFile(srcdest[0],srcdest[1]))
		return files