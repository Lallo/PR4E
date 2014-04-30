#3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use raw_input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

hrs = raw_input("Enter Hours:")
h = float(hrs)
rph = raw_input("Enter Rate per Hour:")
r = float(rph)
if ((h < 0) or (r < 0)):
    print "Please use positive numbers"
elif 0 < h <=40:
    print h * r
elif h > 40:
    print 40 * r + (h-40)*r*1.5

