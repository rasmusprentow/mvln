#tests.py

from mvln import *

import random, os
import unittest

testfolder = os.getcwd()+ "/tmptest/ssd/testfolder/"
testfolder_dest = os.getcwd()+"/tmptest/old/testfolder/"
class TestSequenceFunctions(unittest.TestCase):
	def setUp(self):
		

		try:
			shutil.rmtree("tmptest")
		except OSError:	
			pass
		
		os.mkdir("tmptest")
		os.mkdir("tmptest/old")
		os.mkdir("tmptest/ssd")
		os.mkdir("tmptest/test")
		os.mkdir(testfolder)
			
		
		f = open(testfolder+"testfile",'w')
		f.write("testestest")
		f.close()
		

	def test_amv_move(self):
		try: 
			shutil.rmtree("tmptest/test2")
		except OSError:	
			pass
		Mvln.copyPreserved("tmptest/test","tmptest/test2")
		self.assertTrue(os.path.exists("tmptest/test2"))

    
	def test_amv_moves_and_makes_symlink(self):
		
		self.assertTrue(os.path.exists(testfolder))
		self.assertFalse(os.path.exists(testfolder_dest))
		#dst = os.getcwd()+"/tmptest/old/"+Mvln.pathLeaf(src)+"/"		
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


if __name__ == '__main__':
    unittest.main()