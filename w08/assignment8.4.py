#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() function. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

def openfile():
    fname = raw_input("Enter file name: ")
    try:
        fh = open(fname, 'r')
    except:
        print "Error opening file", fname
        quit()
    return fh

def listWords(fh):
    lst = []
    for line in fh:
        line = ((line.rstrip()).lstrip()).split()
        for word in line:
            if word not in lst:
                lst.append(word)
    lst.sort()
    return lst


fh = openfile()
result = listWords(fh)
print result
