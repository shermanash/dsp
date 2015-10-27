# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > * pwd - show current directory
* mkdir dir i create directory dir
* rm file - delete file
* touch file - create file
* head file - output the first 10 lines of file
* grep pattern files - search for pattern in files
* mv file1 file2 - rename or move file1 to file2
* date - show current date and time
* ping host - ping host and output results
* Ctrl+C - halts current command


---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > * `ls` lists the files in the current directory.
*  `ls -a` includes hidden files in the list.
* `ls -l` is a formatted listing of files containing owner, permissions, and size.
* `ls -lh` is a formatted list with the size converted to human readable format
* `ls -lah` is the a formatted list with hidden files and size human readable.
* the meaningful combination is ls the directory listing then the second option are optional parameters.

---


---

What does `xargs` do? Give an example of how to use it.

> > * xargs reads items from input and executes a command one or more times with arguments.
* an example would be `find /.dsp -name `*.md` | xargs ls -lh`
* this command lists all the files ending in md contained in the DSP folder or its subfolders
* `find /.dsp -name `*.md`` finds all files ending in .md, within the dsp folder.
* `xargs ls -lh` executes the find statement on all files and lists the results
---

