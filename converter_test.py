#converter_test.py

from converter import *


import unittest, os, shutil

testfolder = os.getcwd()+ "/tmptest/ssd/testfolder/"
testfolder_dest = os.getcwd()+"/tmptest/old/testfolder/"
testfolder2 = os.getcwd()+ "/tmptest/ssd/testfolder2/"
testfolder2_dest = os.getcwd()+"/tmptest/old/testfolder2/"
class TestSequenceFunctions(unittest.TestCase):
	def setUp(self):
		try:
			shutil.rmtree("tmptest")
		except OSError:	
			pass
		
		os.mkdir("tmptest")
		os.mkdir("tmptest/old")
		os.mkdir("tmptest/ssd")
		os.mkdir(testfolder)
		os.mkdir(testfolder2)	
		
		f = open(testfolder+"testfile",'w')
		f.write("testestest")
		f.close()
		
		f = open(testfolder2+"testfile",'w')
		f.write("testestest")
		f.close()

		self.converter = Converter( testfolder + " " 	+ testfolder_dest 	+ "\n" +
									testfolder2 + " " 	+ testfolder2_dest	+ "\n")


	def test_getlines(self):

		
		result = self.converter.getLines()
		self.assertEqual(result[1], testfolder2 + " " 	+ testfolder2_dest)
		

	def test_convert(self):

		
		result = self.converter.getFiles()
		self.assertIsInstance(result[1], MvLnFile)
		self.assertEqual(result[1].dst, testfolder2_dest)
		self.assertEqual(result[1].src, testfolder2)
		self.assertEqual(result[0].dst, testfolder_dest)
		self.assertEqual(result[0].src, testfolder)

if __name__ == '__main__':
    unittest.main()