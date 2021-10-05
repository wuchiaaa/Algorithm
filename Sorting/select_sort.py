def swap(i, min):
    temp = list[min]
    list[min] = list[i]
    list[i] = temp
    return list
    # print("@:", list)


def select_sort():
    for i in range(len(list) - 1):
        min = i
        for j in range(i+1, len(list)):
            if (list[j] < list[min]):
                min = j
        swap(i, min)

    print("排序後：", list)


### 主程式從這裡開始 ###

count = int(input("輸入個數："))
list = []
for i in range(count):
    number = int(input("輸入排序數字："))
    list.append(number)

print("您輸入的值為：", list)      # 範例: [88, 44, 22, 100, 1, 16]
select_sort()       # 排序結果
