#sort python dictionaries by key and value.
dict ={1976:"apple",1975:"microsoft",2004:"facebook"}
print("Given dictionary:",dict)
sorted_key=sorted(dict.keys())
print("Sorting dictionary by using key:")
for i in sorted_key:
    print(i,":",dict[i],end=" ")

sorted_value=sorted(dict.values())
sorted_dict={}
for i in sorted_value:
    for k in dict.keys():
        if dict[k]==i:
            sorted_dict[k]=dict[k]
            break
print("\nSorting dictionary by using value:")
print(sorted_dict)
