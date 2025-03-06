def tinh_tong_so_chan(list):
    tong = 0
    for num in list:
        if num % 2 == 0:
            tong += num
    return tong
input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
num = list(map(int, input_list.split(',')))
tong_chan = tinh_tong_so_chan(num)
print("Tong cac so chan trong list la: ",tong_chan)