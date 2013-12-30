mvln
====

Console application for moving folders and creating links to the destination. 
Roughly equivalent to:
```bash
$ mv a b
$ ln -s b a
```

which should result in:

```bash
$ ln -ls
lrwxrwxrwx  1 pseudo pseudo    1 Dec 30 13:13 a -> b
drwxr-xr-x  2 pseudo pseudo   40 Dec 30 13:12 b
```

Installation
------------

```bash
$ git clone https://github.com/rasmusprentow/mvln.git
$ cd mvln
$ python setup.py install
```

Usage
-----

```bash
$ mvln src dst
```

If multiple files are used the following syntax can be used:

```bash
$ mvln < spec.txt
```
Where `spec.txt` contains:

```bash
/path/to/source1/ /path/to/destination/
/path/to/source1/ /path/to/source2/
```


Why
---
Why did i create this project?  Of course it could be done with a shell script. 
The reason is twofold. First, I wanted to learn python. Second, I needed a script which could move files and create links based on a specification file. Which is quite useful when you have a small SSD and a large HD in the same machine. 