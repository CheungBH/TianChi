import TimeDot
import TimePeriod
import TimeExtract

def TransferTimeD(ls,Dots):
    error=[]
    for i in Dots:
        for j in range(len(ls)):
            try:
                ls[j][i]=TimeDot.TimeDToNum(ls[j][i])
            except (ValueError,IndexError):
                error.append(j)
                ls[j][i]='wrong'
            continue
    return ls,list(set(error))

def TransferTimeP(ls,Periods):
    error=[]
    for i in Periods:
        for j in range(len(ls)):
            try:
                ls[j][i]=TimePeriod.TimePToNum(ls[j][i])
            except (ValueError,IndexError):
                error.append(j)
                ls[j][i]='wrong'
            continue
    return ls,list(set(error))

def WrongDelete(ls,err):
    for i in err:
        del(ls[i])
    return ls

def Transfer(ls):
    TDots, TPeriods=TimeExtract.GetTimes(ls)
    ls_D,errD=TransferTimeD(ls,TDots)
    ls_P,errP=TransferTimeP(ls_D,TPeriods)
    error=list(set(errD+errP))
    error.sort()
    error.reverse()
    F_List=WrongDelete(ls_P,error)
    return F_List

