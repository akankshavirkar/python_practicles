#solve tuple by total digits
def count_digits(t):

    return sum([len(str(x)) for x in t])
l = [(1,2,3,4),(4,6,4,7),(3,9,5,4),(1,7,9,4)]
print("original list",1)
l.sort(key=count_digits)
print ("sorted list:",l)