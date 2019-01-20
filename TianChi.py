import MyModel
import ListToTensor
import Division
import TimeTransfer
import PreProcess
import StanAndNor

doc='Data/NewData.csv'
Raw_List=PreProcess.ToFullMatrix(doc)
#将所有的特征和样本生成一个处理了缺失值的大矩阵，并将大矩阵转换成列表

TimeToNumList=TimeTransfer.Transfer(Raw_List)
#将完整的矩阵的时间值进行批量处理

WholeArray=StanAndNor.SAndN(TimeToNumList)
#将全部的特征变为浮点数，并统一归一化

WholeList = WholeArray.tolist()
feature_train_r,label_train_r,feature_val_r,label_val_r=Division.divide(WholeList,1000)
#将转化好后的大列表分为4份

feature_train,label_train,feature_val,label_val=ListToTensor.transferType(feature_train_r,label_train_r,feature_val_r,label_val_r)
#整理好四个列表形式后，将列表化为张量并且将所有数据转化为浮点数，可以输入网络了

myModel=MyModel.RunModel(feature_train,label_train,feature_val,label_val)
#输入网络中运行