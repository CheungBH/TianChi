def divide(ls,num):
    label = []
    for i in range(len(ls)):
        label.append(ls[i][-1])
        del (ls[i][-1])
    lab_t = label[:num]
    lab_v = label[num:]
    fea_t = ls[:num]
    fea_v = ls[num:]
    return fea_t,lab_t,fea_v,lab_v