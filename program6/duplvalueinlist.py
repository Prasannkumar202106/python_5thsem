#Lab-6: Write a function to find Duplicate values in the List#
def find_duplicates(x):
    length = len(x)
    duplicates = []
    for i in range(length):#creating for loop
        n = i + 1 
        for a in range(n, length):
            if x[i] == x[a] and x[i] not in duplicates:#checking the duplicate one
                duplicates.append(x[i]) #for appending duplicate one
    return duplicates
    #insert values to find out the duplicate ones
p = [120,100,3,245,0,45,180,0,0,3,120,100]
print("duplicate values in the given list is")
print(find_duplicates(p))