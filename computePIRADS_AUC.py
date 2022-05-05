from turtle import clear
import numpy as np
import sklearn.metrics as st
import matplotlib.pyplot as plt

x = np.array([2,3,3,4,5,2,3,4,5,5,3,3,4,2,4])
y = np.array([0,1,1,0,1,0,1,1,1,0,0,0,1,0,1])

fpr,tpr,temp = st.roc_curve(y,x/5)
auc = st.auc(fpr,tpr)
print (auc)

fpr_n = []
tpr_n = []


for i in range(3,6):
    x1 = np.copy(x)
    
    x1[x1<i] = 0
    x1[x1>=i] = 1

    tn,fp,fn,tp = st.confusion_matrix(y,x1).ravel()
    fpr_n.append(fp/(fp+tn))
    tpr_n.append(tp/(tp+fn))

fpr_n.append(0)
tpr_n.append(0)

fpr_n = np.array(fpr_n)
tpr_n = np.array(tpr_n)

auc_n = st.auc(fpr_n,tpr_n)
print(auc_n)