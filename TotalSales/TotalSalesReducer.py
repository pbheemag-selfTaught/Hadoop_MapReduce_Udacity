def reducer():
    totalCost = 0
    count = 0
    for line in sys.stdin:
        
        # to check if non-float values are being converted to float eg: "hello"
        if type(float(line))== float:
            count +=1
            totalCost += float(line)

    print "{0}\t{1}".format(count,totalCost)