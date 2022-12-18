# TODO: Add import statements
from pandas import read_csv
from sklearn.linear_model import LinearRegression
import numpy as np
# plot the results
import matplotlib.pyplot as plt
# Assign the dataframe to this variable.
bmi_life_data = read_csv("bmi_and_life_expectancy.csv")
# select a column from the DataFrame and convert it to a numpy array
bmi = bmi_life_data['BMI'].values.reshape(1, -1)  # a value of -1 let it be inferred from the length of the array
life_expectancy = bmi_life_data['Life expectancy'].values.reshape(1, -1)
# Make and fit the linear regression model
#TODO: Fit the model and Assign it to bmi_life_model
bmi_life_model = LinearRegression()
#bmi_life_model.fit(bmi_life_data['BMI'], bmi_life_data['Life expectancy'])
bmi_life_model.fit(bmi.transpose(), life_expectancy.transpose())
#bmi_life_model.fit(np.array(bmi), np.array(life_expectancy))
#bmi_life_model.fit(bmi_life_data['BMI'].values, bmi_life_data['Life expectancy'].values)
# Mak a prediction using the model
# TODO: Predict life expectancy for a BMI value of 21.07931
#laos_life_exp = bmi_life_model.predict([[21.07931]])
#laos_life_exp = bmi_life_model.predict(np.array(bmi))
print(np.array([[21.07931 ]]))

laos_life_exp = bmi_life_model.predict(np.array(bmi))
print(laos_life_exp)

plt.figure()
plt.plot(bmi, laos_life_exp, color='black')
plt.scatter(bmi, life_expectancy)
plt.show()