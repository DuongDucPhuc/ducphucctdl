def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):   #vòng lặp for chạy hết các phần tử trong mảng a
        for j in range(len(arrayB)): # vòng lặp for được lồng vào vòng lặp for trước chạy hết các phần tử mảng b
            if arrayA[i] < arrayB[j]: # nếu phần tử thứ i mảng a bé hơn phần tử thứ j mảng b
                print(str(arrayA[i]) + "," + str(arrayB[j])) # in ra màn hình i và j ngăn cách bằng dấu ,
a = [1,2,3,4]
b = [5,6,7,8]
printUnorderedPairs(a,b)