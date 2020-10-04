def insert_sort(r, i):
    j = i
    while (r < list[j]):
        list[j + 1] = list[j]
        j -= 1
    list[j + 1] = r
    return list
    # print("@", list)


### 主程式從這裡開始 ###

count = int(input("輸入個數："))
list = []
list.append(-100000000)
for i in range(count):
    number = int(input("輸入排序數字："))   # list = [-100000000, 88, 44, 22, 100, 1, 16]
    list.append(number)

print("您輸入的值為：[ ", end='')
for i in range(1, len(list)):
    print(',', list[i], end='')
print(']')

for i in range(2, len(list)):
    insert_sort(list[i], i - 1)

print("排序後結果：[ ", end='')
for i in range(1, len(list)):
    print(',', list[i], end='')
print(']')
