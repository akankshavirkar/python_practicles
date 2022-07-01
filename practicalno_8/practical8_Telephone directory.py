#write telephone directory of 10 students using dictionary nad  perform opration
#a) finding value=key-value
#b)Replacing value=key-newvalue
#C)Replacing key value(saveno,delete value,insert value)



telephone_dict ={"Akanksha":8856919915,"pappa":9623651176,"Anil":7020809928,"Chiva":9604602945,"Mummy":8432162176,"Tanvi":9112972690,"aarti":9112769815,"Sheetal":9145868696,"kirti":8821563569,"jui":9685718696}
print("Telephone dictionary is:")
print(telephone_dict)
#a)finding value = key-value
key = str (input("Enter key to find value:"))
print("Telephone number of given key" ""+key +" is:")
for i in telephone_dict.keys():
    if i==key:
        print(telephone_dict[i])



#b)Replacing value=key-new value
key = str(input("Enter key to find value:"))
value =str(input("Enter the new value:"))
for i in telephone_dict.keys():
    if i==key:
        telephone_dict[i]=value
print("Telephone directory after replacement:")
print(telephone_dict)


 #C) replacing key value - delete key and insert key
num = int(input("Enter telephone number :"))
name =  str(input("Enter new key name :"))
old_key =0
for key,value in telephone_dict.items():
    if num==value:
        old_key = key
telephone_dict[name] = telephone_dict.pop(old_key)

print("Dictionary after replacing key:value :")
print(telephone_dict)



