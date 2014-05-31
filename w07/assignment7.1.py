#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
#You can download the sample data at http://www.pythonlearn.com/code/words.txt

# Use words.txt as the file name

def openfile():
    fname = raw_input("Enter file name: ")
    try:    
        fh = open(fname, 'r')
    except:
        print "Error opening file", fname
        quit() 
    return fh

def printit(f):
    for line in f:
        #print line.upper(), #Trailing comma to avoid adding a newline at the end of print
        print line.upper().rstrip() #Trailing comma to avoid adding a newline at the end of print


fh = openfile()
printit(fh)


