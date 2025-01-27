# 作者：郭小华
# 开发时间：2025-01-27 14:48
for i in range(1,4):#外层循环控制行数
    for j in range (1,9):#内层循环控制列数
        print('*',end='')
    print() #空的print语句是为了换行

for i in range(0,6):#五行
    #*的个数与行相同；第一行range(1,2)、第二行range(1,3)、第三行range(1,4)……
    for j in range(1,i+1):
        print('*',end='')
    print() #空的print语句是为了换行
print()  # 空的print语句是为了换行

