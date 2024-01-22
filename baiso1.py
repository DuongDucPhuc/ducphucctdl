def foo(array):
    sum = 0 # khởi tạo biến sum = 0
    product = 1 # khởi tạo biến product = 1
    for i in array:  # vòng lặp for sẽ chạy từ giá trị đầu tiên đến giá trị cuối cùng trong mảng tính tổng các phần tử trong mảng
        sum += i      # 2+ 3+ 4+ 5+6 =20
    for i in array:  # vòng lặp for sẽ chạy từ giá trị đầu tiên đến giá trị cuối cùng trong mảng tính tích các phần tử trong mảng
        product *= i  # 2*3*4*5*6=720
    print("Sum = "+str(sum)+", Product = "+str(product))  # in ra màn hình tổng và tích

a =[2, 3, 4, 5, 6]
foo(a)
