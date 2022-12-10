from sklearn.linear_model import LinearRegression
model = LinearRegression()
#TODO : Find better example below
model.fit([ [127], [248] ],[ [127], [248] ])
print(model.predict([ [127], [248] ]))