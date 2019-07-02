list = [100,-5,200,1,78,77,88]
new = []
def sort(self):
    while list:
        n = list.index(max(list))
        rem = list.pop(n)
        new.append(rem)
    return new
print(sort(list))
#print(list)