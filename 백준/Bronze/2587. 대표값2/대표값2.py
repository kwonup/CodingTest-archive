num_lst = []
total = 0
for i in range(5):
    n = int(input())
    total+=n
    num_lst.append(n)
num_lst.sort()
print(total//5)
print(num_lst[2])
