def daonguocsonguyen(num,sodaonguoc = 0):
    if num == 0:
        return sodaonguoc
    else:
        somoi = num % 10
        sodaonguoc = sodaonguoc * 10 + somoi
        return daonguocsonguyen(num //10, sodaonguoc)
num = int(input('nhap vao so nguyen duong n ='))
print('nguoc dao cua so nguyen duong n la',daonguocsonguyen(num,sodaonguoc = 0))