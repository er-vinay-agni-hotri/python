from math import log2, log


def addboost(correct, incorrect):
    return log(correct/incorrect)


print(addboost(7,1))
print(addboost(4,4))
print(addboost(2,6))
# from sklearn.ensemble import AdaBoostClassifier
# model = AdaBoostClassifier()
# model.fit(x_train, y_train)
# model.predict(x_test)
#from sklearn.tree import DecisionTreeClassifier
#model = AdaBoostClassifier(base_estimator = DecisionTreeClassifier(max_depth=2), n_estimators = 4)