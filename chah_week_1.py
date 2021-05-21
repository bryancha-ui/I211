
print("Please enter a list:")
l=list(map(str,input().split()))
a=len(l)
print("The middle element is ",l[a//2])
   

words = input("Please enter a list of words: ").split()
for word in words:
    if(word !="secret"):
        print(word)
