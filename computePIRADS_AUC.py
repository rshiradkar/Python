from turtle import clear, color
import numpy as np
import sklearn.metrics as st
import matplotlib.pyplot as plt

x = np.array([2,3,3,4,5,2,3,4,5,5,3,3,4,2,4])
y = np.array([0,0,1,0,1,0,1,1,1,0,0,0,1,0,1])

fpr,tpr,temp = st.roc_curve(y,x/5)
auc = st.auc(fpr,tpr)
print (fpr)

fpr_n = [1]
tpr_n = [1]


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
print(fpr_n)

plt.figure()
plt.plot(fpr,tpr,color = "red", lw = 2, label = "ROC of PIRADS/5 = %0.2f" % auc,)
plt.plot(fpr_n,tpr_n,color = "darkorange", lw = 2,linestyle = "dashed", label = "ROC of PIRADS>=3 = %0.2f" % auc_n,)

plt.plot([0, 1], [0, 1], color="navy", lw=2, linestyle="--")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Receiver operating characteristic of PIRADS")
plt.legend(loc="lower right")
plt.show()