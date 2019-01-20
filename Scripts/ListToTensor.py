import numpy as np

def ToArray(ls_fea_t,ls_lab_t,ls_fea_v,ls_lab_v):
    str_lab_t = np.array(ls_lab_t)
    str_lab_v = np.array(ls_lab_v)
    str_fea_t = np.array(ls_fea_t)
    str_fea_v = np.array(ls_fea_v)
    return str_fea_t, str_lab_t, str_fea_v, str_lab_v

def Tofloat(str_fea_t, str_lab_t, str_fea_v, str_lab_v):
    fea_t=str_fea_t.astype(float)
    lab_t=str_lab_t.astype(float)
    fea_v=str_fea_v.astype(float)
    lab_v=str_lab_v.astype(float)
    return fea_t,lab_t,fea_v,lab_v

def transferType(l_fea_t,l_lab_t,l_fea_v,l_lab_v):
    s_fea_t, s_lab_t, s_fea_v, s_lab_v=ToArray(l_fea_t,l_lab_t,l_fea_v,l_lab_v)
    fea_t, lab_t, fea_v, lab_v=Tofloat(s_fea_t, s_lab_t, s_fea_v, s_lab_v)
    return fea_t, lab_t, fea_v, lab_v


