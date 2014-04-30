#3.2 

try:
    inp = raw_input("Enter Hours:")
    hours = float(inp)
    inp = raw_input("Enter Rate per Hour:")
    rate = float(inp)
except:
    print "Error, please enter numeric input"
    quit()

#print rate, hours
if hours <= 40 :
    pay = rate * hours
else:
    pay = rate * 40 + ( rate * 1.5 * ( hours - 40) )
