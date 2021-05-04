# terminal command

[Learning Shell](https://linuxcommand.org/lc3_lts0020.php)



##	 cd

   - Change Dictioary

     ```shell
     $ cd [relative path or absolute path]
     ```

     + absolute pathname

       ```shell
       $ cd /usr/share/doc 
       ```

     + relative pathname

       ```shell
       $ cd .  # this directory
       $ cd .. # working directory's parent directory
       $ cd ./usr/bin #  ./  usually omitted
       ```


  ## pwd

Pathway Directory

```shell
$ pwd
/usr/bin
```

  ## ls

```shell
$ ls        #list the files in working directory
$ ls /bin   #list files in /bin directory
            #  absolute path name
```

```shell
$ ls -a     #list all the files  (hidden filees included)
$ ls -l     #list files with complex details
$ ls -la
```

```shell
$ ll         # equals to ls -l
```

  ## mkdir

Make Directory

```shell
$ mkdir [Directory name] 
```

 ## rm

Remove File

```shell
$ rm [-fir] [document name]
	# -f force delete
	# -i make sure once (Preset)
	# -r redo until nothing to remove
```

 ## mv

```shell
$ mv [-u] [source] [destination]
		# -u update 
		# means the program only works when source file is newer.
$ mv test.txt ../ 
$ mv a.file b .file /bin #source can be multiple
```

 ## clear

```shell
$ clear # clear the screen
```

