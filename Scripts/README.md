# Bash Scripts

A Reference sheet for bash commands

## Basic Commands

* *cat* - view contents of file
    * `>` overwrite file
    * `>>` append to file

* *cd* - change directory
    * `../` go up one directory
    * `../../` go up two directories

* *chmod* - change permissions 
    * `-x` read and write permissions

* *cp* - copy contents of directory or file into *x* file/directory

* *echo* - list contents of directory

* *head* - print first **10** lines of a file.

* *ls* - list contents of directory
    * `-a` all or hidden files (starts with *.*)
    * `-l` more information (permissions, iNodes, owner/group, (size,modifation, name) )

* *man* - manual pages

* *mv* - move file or directory

* *pwd* - present working directory

* *touch* - create new file

## Redirecting I.O. Streams

Redirection - redirecting output from one process to another

### > redirects output 

#### Overwrite 
example: **python** ```print('hello')``` > file.txt  ===> writes *hello* to the file. <br/>
example: ```echo "hello"``` > file.txt  ===> writes *hello* to the file.

#### Append
example: **python** ```print('hello')``` >> file.txt  ===> writes *hello* to the file. <br/>
example: ```echo "hello"``` >> file.txt  ===> writes *hello* to the file.

## Pipes

Pipes - connection the output of one program to another.

Simple <br/>
`ls -l | less` - paginate the output of the list command using the less command

Advanced <br/>
`cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nc | head`

Read contents of file, where there is a space add a new line, sort alphabetically, display non-unique elements only once, sort numerically and count occurences, finally print the head or first 10 lines.

