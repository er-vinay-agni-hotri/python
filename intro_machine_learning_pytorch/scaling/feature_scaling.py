# TODO: Add import statements
from sklearn.linear_model import Lasso
from pandas import read_csv
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
import numpy as np
# Assign the data to predictor and outcome variables
# TODO: Load the data
train_data = read_csv('feature_scale_data.csv', header=None)
X = train_data.iloc[:,:-1]
y = train_data.iloc[:,-1]


# TODO: Create the standardization scaling object.
scaler= StandardScaler()

# TODO: Fit the standardization parameters and scale the data.
X_scaled = scaler.fit_transform(X)

# TODO: Create the linear regression model with lasso regularization.
lasso_reg = Lasso(alpha=0.01)

# TODO: Fit the model.
lasso_reg.fit(X,y)

# TODO: Retrieve and print out the coefficients from the regression model.
reg_coef = lasso_reg.coef_
print(reg_coef)