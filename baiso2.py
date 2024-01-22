def printPairs(array):
    for i in array:    # vòng lặp for chạy các phần tử trong mảng
        for j in array:  # vòng lặp for này được lồng vào trong vòng lặp for trước
                        #vd: for i in array:   vòng lặp for này sẽ chạy được phần tử đầu tiên của mảng như là phần tử đầu tiên của cặp 
                        #       for j in array:  vòng lặp for này sẽ chạy được phần tử thứ thứ 2 của cặp  
            print(str(i)+","+str(j)) # in ra i và j ngăn cách nhau bới dấu ,
a =[1,2,3]
printPairs(a)