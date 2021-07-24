# Linear Regression From Scratch
## Requirements
* Python 3
* Numpy
* Pandas
* Matplotlib

## How to use (simple)
python3 main.py

## Documentation
there are 3 programs 

* linreg.py
1. regresor_fit 
---

Function for linear regression require (x,y) parameters. This function return coefficient and intercept value.

---

2. MSE
---

Mean Square Error function. Evaluating regression. This function return value of MSE.

---
3. predict
---

apply prediction data using formula Y=a+bx. a dan b refers to coefficient and intercept value. This function return prediction that fill in array.

---
4. R2
---

R2 score function. Value range 0-1 (best possible score is 1). This function return value R2 score.

---
* preprocess_dataset.py
1. export
---

This function will process dataset into simple table for Demo. Values of xtrain, ytrain, xtest, ytest will be returned.

---
* main.py

---
Main program of the project. For implementation just type python3 main.py

---

## Additional infomation

* Link Dataset https://www.kaggle.com/dgawlik/nyse

* For implementing your own dataset, first do the preparation and cleaning data. Make sure atributes in numpy array format. Then you can replace X_train,X_test,Y_train,Y_test= export() with your own data.