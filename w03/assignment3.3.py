#3.3 Write a program to prompt the user for a score using raw_input. Print out a letter grade based on the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

try:
    inp = raw_input("Please enter a score: ")
    score=float(inp)
except:
    print "Please enter a score number between 0.0 and 1.0"
    quit()

if 0.0 <= score  < 0.6 :
    print "F"
elif 1.0 >= score >= 0.9 :
    print "A"
elif 0.9 > score >= 0.8 :
    print "B"
elif 0.8 > score >= 0.7 :
    print "C"
elif 0.7 > score >= 0.6 :
    print "D"
else :
    print "Your score number is not in the 0 - 1 range."
