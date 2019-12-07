1. 'chown' : change the owner or the group of a file or directory.

1.1 'chown ines tmpfile': change the owner of tmpfile to ines.

1.2 'chown :friends tmpfile': change the group of tmpfile to friends. 

1.3 'chown ines:friends tmpfile': change both owner and group of tmpfile

1.4 'chown --from=root ines tmpfile': change the owner of tmpfile to ines only if the current owner is root

1.5 'chown --reference=file1 file2': copy the owner and group of file1 into file2

1.6 'chown -R ines:friends downloads/': change owner and groups of all files inside downloads recursively.