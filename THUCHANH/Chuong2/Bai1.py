def mang_doixung(arr):
    n = len(arr)
    for i in range(n // 2):  
        if arr[i] != arr[n - i - 1]:
            return False
    return True
arr1 = [1, 2, 3, 2, 1]
arr2 = [1, 2, 3, 4, 5]
print(mang_doixung(arr1))  
print(mang_doixung(arr2)) 
