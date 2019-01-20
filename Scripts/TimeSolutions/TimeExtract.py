def GetTimes(ls):
    Dots=[]
    Periods=[]
    for i in range(len(ls[1])):
        if isDot(ls[1][i])==True:
            Dots.append(i)
        elif isPeriod(ls[1][i])==True:
            Periods.append(i)
        else:
            pass
    return Dots,Periods

def isDot(str):
    for i in str:
        if ':00' in str and '-' not in str:
            return True
        else:
            return False

def isPeriod(str):
    for i in str:
        if ':00' in str and '-' in str:
            return True
        else:
            return False


