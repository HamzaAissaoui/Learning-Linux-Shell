1.  'chmod'	: sets the permissions 'read','write','execute' of files or directories \
			  For 'user','group','others'

1.1 'chmod u=rwx,g=rx,o=r myfile' :	User can do everything to myfile, members of the Group can read and execute
									Others can only read myfile.

2.We can also use octal permissions notation:

4 stands for "read",
2 stands for "write",
1 stands for "execute",
0 stands for "no permission.
Each digit is a combination of the numbers 4, 2, 1, and 0:

7: all permissions.
5: read and execute.
4: read only.

2.2 'chmod 754 myfile' : 7: For User, 5: For Group, 4: For Others


