
import os
import sys
import re

def transform(path, current) :

    if 'spa' in path :
	return

    tmp_path= os.path.basename( path ) 
    tmp_list = tmp_path.split('_') 
    tmp_str = tmp_list[0]
    # tmp_list_1 = tmp_str.split('\\')
    # output_name = tmp_list_1[-1]
    output_name = tmp_str + '.txt'
    output_name = os.path.join( current , output_name )
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
    current_folder = os.getcwd()
    print current_folder

    if (len(sys.argv) == 2) : 
	if os.path.isdir( sys.argv[1] ) :
	    for root,dirs, files in os.walk( sys.argv[1] ) :
		for f in files :
		    # print root
		    # print dirs
		    # print f
		    target = os.path.join( root , f )
		    transform( target , current_folder ) 
	else :
	    transform( sys.argv[1], current_folder ) 
    else :
	print "please enter the path"
if __name__ == '__main__':
    main()
