#9.4 Write a program to read through the mbox-short.txt and figure out who has the most commits. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the senders mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt

def openFile():
    fname = raw_input("Enter file name: ")
    if len(fname) < 1 : fname = "mbox-short.txt"
    try:
        fh = open(fname, 'r')
    except:
        print "Error opening file", fname
        quit()
    return fh

def startsWith():
    sw = raw_input("Enter line prefix to consider: ")
    if len(sw) < 1 : sw = "From"
    return sw

def doCount(lines,s):
    counts = dict()
    for line in lines:
        if line.startswith(s) and not line.startswith(s+':'):
            line = ((line.rstrip()).lstrip()).split()
	    counts[line[1]] = counts.get(line[1],0) + 1
    return counts

def max(dictionary):
    max = None 
    highest = None
    #print dictionary
    for key in dictionary:
        if max < dictionary[key]:
	    max = dictionary[key]
	    #print "new max is", max
	    highest = key
    return highest

fh = openFile()
sw = startsWith()

dictionary = doCount(fh,sw)
key = max(dictionary)
print key, dictionary[key] 
