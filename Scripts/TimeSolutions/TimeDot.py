def IntegrateNum(*nums):     #把一位或两位的字符串变成整数
    a=''
    for i in nums:
        a=a+i
    return int(a)

def TtoNmin(TimeNum):       #把分钟的时间变成小数
    MinNum=IntegrateNum(TimeNum[-5],TimeNum[-4])
    return MinNum/60

def TimeDToNum(TimeNum):     #把整个时间变成浮点数
    if len(TimeNum)==7:
        hrNum=IntegrateNum(TimeNum[-7])
    else:
        hrNum=IntegrateNum(TimeNum[-8],TimeNum[-7])
    MinNum=TtoNmin(TimeNum)
    return hrNum+MinNum

# def TimeToNumList(ListTime):  #处理整个列表的时间
#     error=[]
#     NumTimeList=[]
#     for i in range(len(ListTime)):
#         try:
# #             NumTime=TimeToNum(i)
#             NumTimeList.append(TimeToNum(ListTime[i]))
#         except ValueError:
#             error.append(i)
#             NumTimeList.append('wrong')
#         continue
#     return NumTimeList,error

