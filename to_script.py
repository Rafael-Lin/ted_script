
import os
import sys
import re
def function(path) :

    output_name, tmp = path.split('_') 
    output_name += '.txt'
    lines = open(path, 'r').readlines()
    file = open(output_name, "w")
    for line in lines:
	if re.match( "^[0-9]+.*$" , line ):
	    continue 
	elif line.startswith('\n' )  :
	    continue 
	else :
	    file.write( line ) 

    print 'success! transform to ' + output_name
    file.close()
def main() :

    if (len(sys.argv) == 2) : 
	function( sys.argv[1] ) 
    else :
	print "please enter the path"
if __name__ == '__main__':
    main()
