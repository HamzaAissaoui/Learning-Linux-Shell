1. 'xargs'	: builds an execution pipeline From standard Input

1.1 'echo "one two three" | xargs mkdir' : creates directories 'one', 'two', 'three' using mkdir.

1.2 'echo "one two three" | xargs -t rm' : '-t' prints the commands that are executed. 
#Output: rm one two three

1.3 'find /tmp -mtime +14 | xargs rm'	 : find the files in temp that are older than 2 weeks then remove them

1.4 'echo "one two three" | xargs -p touch' : '-p' prompts before execution, it means it asks for confirmation.
#Output: touch one two three ?...