#!/bin/bash
# Test script to test cli and functionality. 

# An example of how proper output should look like can be found in the bottom


##### configuration
TESTDIR=__tmptest__
TESTFILE=__test.txt
RUNNABLE=mvln
#python3 mvln/mvln.py



function setup {
	rm -r $TESTDIR
	mkdir $TESTDIR
	mkdir $TESTDIR/src 
	mkdir $TESTDIR/dst
	mkdir $TESTDIR/src/testfolder 
	mkdir $TESTDIR/src/testfolder2
}

function assert {
	if [ -d $1  ]
	then
	    echo .
	else
		echo Failed to copy the correct with script: python3 cli.py  \< $TESTFILE 
	fi
	
	
	if [ -L $2  ]
	then
	    echo .
	else
		echo Failed to create symlink: python3 cli.py  \< $TESTFILE 
	fi
}



#### run normal tests
python3 mvln/test/test_converter.py
python3 mvln/test/test_mvln.py


#### create input file
echo $(pwd)/$TESTDIR/src/testfolder/' '$(pwd)/$TESTDIR/dst/testfolder/ > $TESTFILE 
echo $(pwd)/$TESTDIR/src/testfolder2/' '$(pwd)/$TESTDIR/dst/testfolder2/ >> $TESTFILE 


#### Test 1
setup

$RUNNABLE  < $TESTFILE

assert $TESTDIR/dst/testfolder $TESTDIR/src/testfolder
assert $TESTDIR/dst/testfolder2 $TESTDIR/src/testfolder2

#### Test 2
setup

$RUNNABLE --file $TESTFILE

assert $TESTDIR/dst/testfolder $TESTDIR/src/testfolder
assert $TESTDIR/dst/testfolder2 $TESTDIR/src/testfolder2

##### Test 3
setup 

$RUNNABLE -v --file $TESTFILE

assert $TESTDIR/dst/testfolder $TESTDIR/src/testfolder
assert $TESTDIR/dst/testfolder2 $TESTDIR/src/testfolder2


##### Clean up:
if [[ "$1" != "-d" ]]
then 
rm -r $TESTDIR
rm $TESTFILE 
fi


#### Output should be something in the line of:

#  $bash test.sh
#..
#----------------------------------------------------------------------
#Ran 2 tests in 0.002s
#
#OK
#...
#----------------------------------------------------------------------
#Ran 3 tests in 0.003s
#
#OK
#Moving /home/pseudo/Dropbox/Projekter/python/mvln/__tmptest__/src/testfolder/ to /home/pseudo/Dropbox/Projekter/python/mvln/__tmptest__/dst/testfolder/
# and creating link.....
#Done!
#Moving /home/pseudo/Dropbox/Projekter/python/mvln/__tmptest__/src/testfolder2/ to /home/pseudo/Dropbox/Projekter/python/mvln/__tmptest__/dst/testfolder2/
# and creating link.....
#Done!
#.
#.
#.
#.
#.
#.
#.
#.
#Loading files to move from: test.txt
#Moving /home/pseudo/Dropbox/Projekter/python/mvln/__tmptest__/src/testfolder/ to /home/pseudo/Dropbox/Projekter/python/mvln/__tmptest__/dst/testfolder/
# and creating link.....
#Done!
#Moving /home/pseudo/Dropbox/Projekter/python/mvln/__tmptest__/src/testfolder2/ to /home/pseudo/Dropbox/Projekter/python/mvln/__tmptest__/dst/testfolder2/
# and creating link.....
#Done!
#.
#.
#.
#.

