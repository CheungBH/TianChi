def IntegrateNum(*nums):     #把一位或两位的字符串变成整数
    a=''
    for i in nums:
        a=a+i
    return int(a)

def TtoNminP(TimeNum):       #把时间段中分钟的时间变成小数
    MinNum=IntegrateNum(TimeNum[-2],TimeNum[-1])
    return MinNum/60

def TimeToNumP(TimeNum):     #把时间段中整个时间变成浮点数
    if len(TimeNum)==4:
        hrNum=IntegrateNum(TimeNum[-4])
    else:
        hrNum=IntegrateNum(TimeNum[-5],TimeNum[-4])
    MinNum=TtoNminP(TimeNum)
    return hrNum+MinNum

def TimePToNum(TimeStr):
    DTime=TimeStr.split('-')
    TimeP=TimeToNumP(DTime[1])-TimeToNumP(DTime[0])
    if TimeP>0:
        return TimeP
    else:
        return TimeP+24

# def TimePToNumList(ListTimeP):            #处理整个列表的时间
#     error=[]
#     TimePList=[]
#     for i in range(len(ListTimeP)):
#         try:
#             TimePList.append(TimePToNum(ListTimeP[i]))
#         except ValueError:
#             error.append(i)
#             TimePList.append('wrong')
#         continue
#     return TimePList,error
