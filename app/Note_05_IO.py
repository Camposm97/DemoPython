

def read_file(src):
    arr = []
    with open(src) as file:
        current_line = file.read()
        arr.append(current_line)
    return arr;


my_list = read_file("sample.txt")
print(my_list)
for s in my_list:
    print(s)
