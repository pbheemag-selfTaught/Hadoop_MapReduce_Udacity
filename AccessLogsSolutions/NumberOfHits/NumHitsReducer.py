import sys

count = 0 
test = "/assets/js/the-associates.js"

for line in sys.stdin:
	if test in line:
		count += 1

print "{0}\t{1}".format(count , "/assets/js/the-associates.js" )