# Python code to get difference of two lists
# Using set()
def Diff(A, B):
    print("Difference of two lists ::>")
    return (list(set(A) - set(B)))

# Driver Code
A=list()
n1=int(input("Enter the size of the first List ::"))

print("Enter the Element of first List ::")
for i in range(int(n1)):
    k=int(input(""))
    A.append(k)
B=list()
n2=int(input("Enter the size of the second List ::"))
print("Enter the Element of second List ::")
for i in range(int(n2)):
    k=int(input(""))

    B.append(k)
print(Diff(A, B))
