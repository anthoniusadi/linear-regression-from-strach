import numpy as np
import linreg
import matplotlib.pyplot as plt
#!train data
X_train=np.array([24,22,21,20,22,19,20,23,24,25,21,20,20,19,25,27,28,25,26,24,27,23])
Y_train=np.array([10,5,6,3,6,4,5,9,11,13,7,4,6,3,12,13,16,12,14,12,16,9])
#!test data
X_test = np.array([24,23,22,21,26,25,26,27])
Y_test = np.array([13,11,7,5,12,11,13,14])
#!apply regression function
a,b = linreg.regresor_fit(X_train,Y_train)
#!predict data test
ypred = linreg.predict(X_test)
#! Evaluation MSE & R2Score
print("Nilai MSE : ",linreg.MSE(ypred,Y_test))
print("R2 score : ",linreg.R2(Y_test,ypred))
#!Ploting
plt.scatter(X_test,Y_test)
plt.plot(X_test, ypred, color='blue', linewidth=1)
plt.show()