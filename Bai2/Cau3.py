def tao_tuple_tu_list(list):
    return tuple(list)
input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
num = list(map(int, input_list.split(',')))
my_tuplre = tao_tuple_tu_list(num)
print("List: ",num)
print("Tuple tu list: ",my_tuplre)