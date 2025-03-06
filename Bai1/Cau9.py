def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int (n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Nhap vao so cam kiem tra: "))
if kiem_tra_so_nguyen_to(num):
    print(num,"la so nguyen to")
else:
    print(num,"khong phai la so nguyen to")