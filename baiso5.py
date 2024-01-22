def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):  # vòng lặp for chạy các phần tử trong mảng của a và đếm số phần tử mảng a
        for j in range(len(arrayB)): # vòng lặp for được lồng trong vòng lặp for trước chạy các phần tử trong mảng b và đếm số phần tử trong mảng b
            for k in range(0,100000): # vòng lặp for chạy phần tử k trong phạm vi từ 0 đến 100000
                print(str(arrayA[i]) + "," + str(arrayB[j])) # in ra màn hình 100000 phần tử thứ i và j cách nhau bằng dấu ,
a = [ 1, 2]
b = [ 5, 6]
printUnorderedPairs(a ,b)