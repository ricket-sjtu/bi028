
# Lab 1: Linux Command Line Practice
### 2018-03-16


### Directory

1. Here is an example directory tree. Suppose your current directory is `Desktop`
```
/root
├── bin
│   ├── ballgown
│   ├── shadowsocks
├── Desktop
├── docker
│   ├── compose
│   ├── docker-spark
├── test.exe
├── PCA.txt
├── perl5
```
- Write down your absolute path of your current working directory.
- Write down your relative path of your current working directory.
- Write down the absolute and relative path for the file `ballgown`. 


### Manpages
1. Sometimes there are several man pages (located in different sections) 
for the same keyword. Which command-line option to `man` can display all 
of them?


### Permissions

1. It is possible to set individual permissions for user, group and others using chmod. 
Review the documentation and answer the following questions:
  - How can you set the permission string to user read/write, group read, others read
using chmod in long format?
  - How can you revoke group write permissions on a file without changing any other
permissions?
  - How can you grant user and group execute permissions without changing any other
permissions?
  - If you use the octal form, how to set the permissions for the above three questions?
  - What do the following numeric file modes represent:
   * (A) 666
   * (B) 770
   * (C) 640
   * (D) 444
2. Which command-line option to chmod allows you to alter the permissions of an entire
directory tree?
3. What does execute (x) permission mean on directories?
4. A user wants to set the permissions of a directory tree rooted in dir so that the user and
group can list, read and write (but not execute) files, but nobody else has any access. Which
of the following commands is most appropriate? Why?
  * (A) `chmod -R 660 dir`
  * (B) `chmod -R 770 dir`
  * (C) `chmod -R u+rw,g+rw,o-rwx dir`
5. When answering the questions, consider how the execute permission is handled by the various 
choices, and what importance the execute permission has on directories.
6. How can you change the owner and group of an entire directory tree (a directory, its
subdirectories and all the files they contain) with a single command?
7. How do you make the file `secret` readable and writable by `root`, readable by the group 
`wheel`, and completely inaccessible to everyone else?

### File manipulation
1. When you run `which mv`, you will find that `mv` is in fact the alias of `mv -i`. Now you 
know what it does? Why?
2. What options to `cp` allows copy of a whole directory `dir1` to the destination `dir2`, 
preserving the modification time, ownership and permissions of all files?
3. In the output from command `ls -laFd dir dsp`:
```
drwxr-xr-x 22  bio staff 4096 Jan 12 2018 dir/
crw-rw----  1 root audit 1403 Jan 22 2018 dsp
```
- What does the `c` at the beginning of the second line indicate?
- What do `bio` and `staff` mean for `dir`?
- Which users may write to the file `dsp`?


### Archive and Compression
1. Draw a table to summarize the usage of `tar`, `gzip` and `bzip2` for the following file types:
- `FILENAME.tar`
- `FILENAME.tar.gz`
- `FILENAME.tgz`
- `FILENAME.tar.bz2`
- `FILENAME.gz`
- `FILENAME.bz2`


### Redirection and Pipe
1. Where will `stdout` and `stderr` be redirected in the following examples:
  - `command 2>&1 >file1`
  - `command >file1 2>&1`
2. Use your shell's alias to create a shell command named `gzless` that decompresses a 
`gzip`-compressed file and pipes it into `less`.
3. What do the following commands do?
- (a) `ls | grep -i doc`
- (b) `command 2>&1 | grep -i fail`
- (c) `command 2>&1 >/dev/null | grep -i fail`
4. Output a recursive listing (using `ls`) of your home directory, including the hidden 
files, to the file `/tmp/HOMEFILES`.
5. Find any files (using `find`) on the system that are all-writable. Error messages should 
be discarded (redirected to `/dev/null`). This command is actually useful for auditing the 
security of a system-world-writable files. 

### System Logging
1. What does `tail -f /var/log/secure` do?
2. If you want to extract the last ten lines in /var/log/secure that are related to the 
service `sshd`, what command shoud you use? (Hint: the `grep` command can be used to search 
for matching lines in a given file.) 
