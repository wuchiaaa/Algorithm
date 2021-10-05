def swap(j):
    temp = list[j]
    list[j] = list[j + 1]
    list[j + 1] = temp
    return list
    # print("@:", list)


def bubble_sort():
    for i in range(len(list) - 1):
        flag = 0
        for j in range(len(list) - 1 - i):
            if (list[j] > list[j + 1]):
                swap(j)
                flag = 1
        if flag == 0:
            break  # 此回合沒有發生交換

    print("排序後：", list)


### 主程式從這裡開始 ###

count = int(input("輸入個數："))
list = []
for i in range(count):
    number = int(input("輸入排序數字："))
    list.append(number)

print("您輸入的值為：", list)      # 範例: [88, 44, 22, 100, 1, 16]
bubble_sort()       # 排序結果
