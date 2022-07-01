#replace words from dictionary
dict={1976:"apple",1975:"microsoft",2004:"facebook"}
key=int(input("Enter the key to replace value:"))
value=str(input("Enter new value:"))
for i in dict.keys():
    if(i==key):
        dict[i]=value
print("Dictionary after replacement:",dict)
