def int_sorted():
    list_index.append(int(match))
    list_int.append(name)


    for i in range(len(list_index) - 1):
        flag = 0

        for j in range(len(list_index) - 1 - i):
            if (list_index[j] > list_index[j + 1]):
                tempindex = list_index[j]
                list_index[j] = list_index[j + 1]
                list_index[j + 1] = tempindex
                temp = list_int[j]
                list_int[j] = list_int[j + 1]
                list_int[j + 1] = temp
                flag = 1
        if flag == 0:
            break  # 此回合沒有發生交換


### 主程式從這裡開始 ###

list = ['yolo-asff_100000.tib', 'yolo-asff_90000.tib', 'yolo-asff_final.tib', 'yolo-asff_99000.tib',
        'yolo-asff_best.tib', 'yolo-asff_93000.tib']

list_int = []
list_str = []
list_index = []
area = '0123456789abcdefghijklmnopqrstuvwxyz'
for x in range(len(list)):
    name = list[x]
    match = name[10:-4:1]
    index = area.index(match[0])

    if index >= 10:
        list_str.append(name)
        list_str = sorted(list_str, reverse=True)
    else:
        int_sorted()

list_sorted = list_int + list_str
print(list_sorted)
