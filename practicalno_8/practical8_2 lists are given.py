#2 lists are given (one has key and other has values and merge them and make dictionary)
#take two list as input and coverted them into dictionary and print dictionary
#two list
list1=["akanksha","amisha","jui"]
list2=[20,21,23]

#key-value lists
print("keys:"+str(list1))
print("values:"+str(list2))


#dictionary = dict(zip(lists1,lists2)) using zip function

dictionary1 ={}
for key in list1:
    for value in list2:
        dictionary1[key] = value
        list2.remove(value)
        break
print("Dictionary is:"+str(dictionary1))
