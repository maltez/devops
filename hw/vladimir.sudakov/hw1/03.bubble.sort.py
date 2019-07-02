list = [100,-5,200,1,78,77,88]
def bubble(self):
    n = len(list)
    for i in range(n-1):
        for j in range(n-i-1):
            if list[j] < list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]        
    return list
print(bubble(list))
