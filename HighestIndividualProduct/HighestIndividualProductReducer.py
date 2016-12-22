def reducer():
    totalCost = 0
    oldkey = None
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data)==2:
            thisProduct,thisCost = data
            if oldkey and oldkey != thisProduct:
                print "{0}\t{1}".format(oldkey , totalCost)
                totalCost = 0
            oldkey = thisProduct
            totalCost += float(thisCost)
    if oldkey !=None:
        print "{0}\t{1}".format(oldkey , totalCost)