This was a coding puzzle that I spent an afternoon solving as part of a job application process.

#Here is the assignment I was given
===================================================================================================

Your task is to write a program that solves mazes.  The input to your program is a text file describing the maze.  Your program should read this from standard input.  An example maze is:
<pre>
###_###
#_____#
#_##_##
#_##__#
#_#####
</pre>
The # represent walls of the maze, and the underscores represent the open areas.  Rows of the maze are separated by newlines ('\n').  Your program should print a solution to standard output like this:
<pre>
###a###
#dcb__#
#e##_##
#f##__#
#g#####
</pre>
Here the lower case letters a represent the path through the maze.  If the maze is large enough that it requires more than 26 steps to go through it, simply start at 'a' again after 'z'.  

FAQ:
Q: Can there be more than one entrance on the top row?
A: Nope, there is just one entrance and it is always on the top row of the maze.

Q: Can there be more than one exit?
A: Nope, just one exit and its in the last row.

Q: Will there be entrances/exits on the sides?
A: Nope, just top or bottom rows.

Too easy?  If you were able to get that done in a hurry and are bored, try to present only the shortest solution to the maze if there is more than one solution. 


#How to run
===================================================================================================

Pick a maze file that looks interesting or design your own. Then run the program with that file as the only argument:
	
	`python maze-solver.py tests/maze-with-cycles > output && cat output`

