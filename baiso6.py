def reverse(array):
    for i in range(0, int(len(array)/2)): # vòng lặp for chạy biến i trong phạm vi từ 0 đến tổng các phần tử của mảng chia 2
        other = len(array)-i-1         # gán tổng các phần tử của mảng -i -1 cho other
        temp = array[i]               #gán phần tử thứ i của mảng cho temp
        array[i] = array[other]      # gán phần tử thứ other của mảng cho phần tử thứ i của mảng
        array[other] = temp            # giá trị của temp được gán cho phần tử thứ other của mảng
    print(array)                     # in mảng 
a=[1,2,3,4]
reverse(a)