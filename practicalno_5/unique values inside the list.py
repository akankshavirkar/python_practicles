# take an input list as lst
lst = [1, 2, 3, 5, 1, 2, 6, 7]
print("Input list : ",lst)

#Empty list
lst1 = []

count = 0

# traverse the array
for i in lst:
    if i not in lst1:
        count = count + 1
        lst1.append(i)

    # printing the output
print("Output list : ",lst1)
print("No. of unique items are:", count)

