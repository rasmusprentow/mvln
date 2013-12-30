#tests.py

import sys

sys.path.insert(0,"..") 
sys.path.insert(0,"mvln") 

import random, os,shutil
import unittest, sys

from mvln import *


#print(__all__)
#sys.exit()

testfolder = os.getcwd()+ "/__tmptest__/src/testfolder/"
testfolder_dest = os.getcwd()+"/__tmptest__/dst/testfolder/"
class TestSequenceFunctions(unittest.TestCase):
	def setUp(self):
		100

		try:
			shutil.rmtree("__tmptest__")
		except OSError:	
			pass
		
		os.mkdir("__tmptest__")
		os.mkdir("__tmptest__/dst")
		os.mkdir("__tmptest__/src")
		os.mkdir("__tmptest__/test")
		os.mkdir(testfolder)
			
		
		f = open(testfolder+"testfile",'w')
		f.write("testestest")
		f.close()
		

	def test_amv_move(self):
		try: 
			shutil.rmtree("__tmptest__/test2")
		except OSError:	
			pass
		Mvln.copyPreserved("__tmptest__/test","__tmptest__/test2")
		self.assertTrue(os.path.exists("__tmptest__/test2"))

    
	def test_amv_moves_and_makes_symlink(self):
		
		self.assertTrue(os.path.exists(testfolder))
		self.assertFalse(os.path.exists(testfolder_dest))
		#dst = os.getcwd()+"/__tmptest__/dst/"+Mvln.pathLeaf(src)+"/"		
		Mvln.mvAndLink(testfolder, testfolder_dest)

		self.assertTrue(os.path.exists(testfolder_dest))
		self.assertTrue(os.path.islink(testfolder.rstrip('/')), testfolder)

		f = open(testfolder + "testfile")			
		self.assertTrue(f.read() == "testestest")
		f.close()
		f = open(testfolder_dest + "testfile")			
		self.assertTrue(f.read() == "testestest")
		f.close()

		self.assertTrue(os.path.islink(testfolder.rstrip('/')))

		self.assertRaises(FileExistsError,Mvln.mvAndLink,(testfolder), (testfolder_dest)) ## should raise exception

	def test_amv_moves_and_makes_symlink_mvnlnfile(self):
		
		self.assertTrue(os.path.exists(testfolder))
		self.assertFalse(os.path.exists(testfolder_dest))
		#dst = os.getcwd()+"/__tmptest__/dst/"+Mvln.pathLeaf(src)+"/"	/
		Mvln.mvAndLinkFile(MvLnFile(testfolder, testfolder_dest))

		self.assertTrue(os.path.exists(testfolder_dest))
		self.assertTrue(os.path.islink(testfolder.rstrip('/')), testfolder)

		f = open(testfolder + "testfile")			
		self.assertTrue(f.read() == "testestest")
		f.close()
		f = open(testfolder_dest + "testfile")			
		self.assertTrue(f.read() == "testestest")
		f.close()

		self.assertTrue(os.path.islink(testfolder.rstrip('/')))

		self.assertRaises(FileExistsError,Mvln.mvAndLinkFile,(MvLnFile(testfolder, testfolder_dest))) ## should raise exception

if __name__ == '__main__':
    unittest.main()