# 作者：郭小华
# 开发时间：2025-01-22 16:03
number=eval(input('请输入您的6位中奖号码:'))
#使用if语句
if number==888888:    #等值判断
    print('恭喜您，中奖了！')
if number!=888888:  #不等值判断
    print('您未中本期大奖')

print('--------以上if判断的表达式，是通过比较运算符计算出来的，结果是布尔值类型---------')
n=98 #赋值操作
if n%2:     #每个对象都有一个布尔值，一切皆对象，0的布尔值是False，非0的布尔值是True
    print(n,'是奇数') #98%2的余数是0，该行代码不执行

if not n%2:  #98%2的余数是0，0的布尔值是False，not False是True，下行代码执行
    print(n,'是偶数')

print('----判断一个字符串是空字符串----')
x=input('请输入一个字符串:')
if x:   #在python中一切皆对象，每个对象都有一个布尔值，而非空字符串的布尔值为True，空字符串的布尔值为False
    print(x,'是一个非空字符串')
if not x: #空字符串的布尔值为False，not False=True,执行下列代码
    print(x,'是一个空字符串')

print('----表达式也可以是一个单纯的布尔型变量----')
flag=eval(input('请输入一个布尔类型的值:True/False'))
if flag:
    print('flag的值为True')
if not flag:
    print('flag的值为False')

print('------使用if语句时，如果语句块中只有一句代码，可以将语句块直接写在冒号的后面-------')
a=10
b=5
if a>b:max=a #语句块只有一句，赋最大值
print('a和b的最大值为:',max)