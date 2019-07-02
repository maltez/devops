a = [1,2,3,5,6,7,8,9]
b = [9,3,7,8,1,4,2,6]
def count(self):
    arr = [1,2,3,4,5,6,7,8,9]
    temp = sum(arr)
    summa = sum(self)
    return temp-summa
print("lost digit in list a is ", count(a))
print("lost digit in list b is ", count(b))