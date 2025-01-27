# 作者：郭小华
# 开发时间：2025-01-27 15:33
row=eval(input('请输入菱形的行数:'))
while row % 2 == 0: #判断行数的奇偶性，行数是偶数，重新输入
    print('请重新输入一个奇数')
    row = eval(input('请输入菱形的行数:'))
#输出菱形
#上半部分：等腰三角形
top_row=(row+1)//2 #上半部分的行数
for i in range(1,top_row+1):
    for j in range(1,top_row+1-i):
        print(' ', end='')
    for k in range(1, 2*i):
        print('*', end='')
    print()  # 当两个并列的for循环执行完毕之后再换行

#下半部分：直角三角形+倒等腰三角形
bottom_row=row//2 #下半部分的总行数
for i in range(1,bottom_row+1):
    for p in range(1,i+1):#直角三角形
        print(' ', end='')
    for q in range(1,2*bottom_row-2*i+2):#倒等腰三角形
        print('*', end='')
    print()  # 当两个并列的for循环执行完毕之后再换行



