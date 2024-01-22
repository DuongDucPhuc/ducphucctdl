def printUnorderedPairs(array):
    for i in range(0,len(array)):   # vòng lặp này lặp các phần tử của mảng
        for j in range(i+1,len(array)): # vòng lặp này lặp các phần tử từ i+1 đến hết mảng
            print(str(array[i]) + "," + str(array[j])) # in ra màn hình i và j phân cách nhau bằng dấu ,
a=[1,2,3]
printUnorderedPairs(a)