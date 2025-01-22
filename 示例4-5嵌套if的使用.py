# 作者：郭小华
# 开发时间：2025-01-22 20:13
answer=input('请问您喝酒了吗？')
if answer=='yes': #yes表示喝酒了
    proof=eval(input('请输入酒精含量:'))   #语句块
    if proof<20:
        print('不构成酒驾行为，祝您一路平安')
    elif proof<80:
        print('构成酒驾行为，请不要开车')
    else:
        print('已构成醉驾行为，请千万不要开车')
else:
    print('您走吧，没你啥事儿！')

