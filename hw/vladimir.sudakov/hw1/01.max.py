arr = [18,2,-4,405,12,54,13,0]
def maxi(self):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max    
print(maxi(arr))
