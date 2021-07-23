import numpy as np

#!Y = a+bx
#? a = (sum(y)*sum(x**2) - sum(x)*sum(x*y)) / ( n*sum(x**2)- (sum(x))**2 )
#? b = ( n*(sum(x*y)) - sum(x)*sum(y)) / ( n*(sum(x**2)) - (sum(x)**2) )
def regresor_fit(x,y):
    global fx
    n = len(x)
    denominator =   ((n * (sum(x**2))) - (sum(x)**2)) 
    a = ( ((np.sum(y) * np.sum(x**2)) - (np.sum(x) * np.sum(x*y))) ) / (denominator)
    b = ( (n*(sum(x*y))) - (sum(x)*sum(y))) / (denominator)
    # a=( (sumy*sumxq) - (sumx*sumxy) )/ ((n*sumxq) - sumxqq)    
    print("koefisien : ",a ," Intercept : ",b)
    fx=[a,b]
    return a,b

#!(1/n) * sum((predict-actual)**2)
def MSE(preds,target):
    p = np.sum((preds-target)**2)
    values = (1/ len(preds)) * p
    # print("nilai MSE = ",values)
    return values

#!apply F(x) 
def predict(pred):
    prediction = fx[0]+fx[1]*pred
    # print("show prediksi", prediction)
    return prediction

#! Cost Function
def R2(x,y):
    return ((len(x)*np.sum(x*y) ) - (sum(x)*sum(y))) / np.sqrt(  (len(x)*np.sum(x**2) - ((np.sum(x))**2)) * (((len(x))*sum(y**2)) - (sum(y)**2))  )