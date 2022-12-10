# TODO: Add import statements
from sklearn.linear_model import Lasso
from pandas import read_csv
import numpy as np
# Assign the data to predictor and outcome variables
# TODO: Load the data
train_data = read_csv('regularData.csv', header=None)
X = train_data.iloc[:,:-1]
y = train_data.iloc[:,-1]


# TODO: Create the linear regression model with lasso regularization.
lasso_reg = Lasso(alpha=0.01)

# TODO: Fit the model.
lasso_reg.fit(X,y)

# TODO: Retrieve and print out the coefficients from the regression model.
reg_coef = lasso_reg.coef_
print(reg_coef)