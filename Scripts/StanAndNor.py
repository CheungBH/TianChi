import numpy as np
from sklearn import preprocessing

def SAndN(ls):
    RawArray = np.array(ls)
    FArray=RawArray[0:, 0:-1]
    LArray=RawArray[:,[-1]]
    FloatArray = FArray.astype(float)
    a = preprocessing.MinMaxScaler()
    FPArray = a.fit_transform(FloatArray)
    FinalArray=np.c_[FPArray,LArray]
    return FinalArray