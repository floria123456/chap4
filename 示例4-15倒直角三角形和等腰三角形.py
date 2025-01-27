# 作者：郭小华
# 开发时间：2025-01-27 15:12
#倒三角形
for i in range(1,6):#五行1、2、3、4、5
    #*；第一行range(1,6)、第二行range(1,5)、第三行range(1,4)……
    for j in range(1,7-i):
        print('*',end='')
    print() #空的print语句是为了换行

#等腰三角形
for i in range(1,10):#五行
    #*的个数与行相同；第一行range(1,2)、第二行range(1,4)、第三行range(1,6)……
    for s in range(1,10-i):
        print(' ', end='')
    for j in range(1,2*i):
        print('*',end='')
    print() #当两个并列的for循环执行完毕之后再换行
#嵌套了两个并列的循环
