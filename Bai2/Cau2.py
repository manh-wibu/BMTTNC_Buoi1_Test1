def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
num = list(map(int, input_list.split(',')))
list_dao_nguoc = dao_nguoc_chuoi(num)
print("List sau khi dao nguoc la: ",list_dao_nguoc)