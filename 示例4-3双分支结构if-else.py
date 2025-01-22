# 作者：郭小华
# 开发时间：2025-01-22 19:53
number=eval(input('请输入您的6位中奖号码'))
# if.. else
if number==120909:
    print('恭喜您，中奖了！')
else:
    print('谢谢参与，您未中本期大奖')

print('------以上代码可以使用条件表达式进行简化---------')
result='恭喜您中奖了' if number==120909 else '您未中奖'
print(result)

print('恭喜您中奖了' if number==120909 else '您未中奖')