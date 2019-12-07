1. 'grep'	:	used to find matching patterns In directories Or inside files directly
				You pipe the output With the command “|”

1.1 'ls ~/Downloads | grep .jpg': Looking For jpg files In downloads ONLY
#Output will be all the files with jpg extension, the extension will be highlighted

1.1. 'ls ~/Downloads | grep -r .deb': looks recursively through all the folders and files In downloads	

1.2 'cat test.txt | grep hi': Looking For 'hi' occurences In the test file and prints the words containing them

1.3 'cat test.txt | grep -i hi': ignores the case, so it also returns Hi or HI..

1.4 'grep -i word /path/to/file.txt': same As the command above

1.5 'grep -rv word /etc/nginx': returns everything not containing the word

1.6 'cat textfile.txt | grep -w it': looks For 'it' And only returns it, not the entire words.





