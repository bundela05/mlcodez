from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1],[2],[3],[12],[5]])
Y = np.array([5,7,9,11,13])

model = LinearRegression()
model.fit(X, Y)
a=model.coef_
b=model.intercept_
print("Slope:", a )
print("Intercept:", b )

def pridiction(a,b,x):
    return a*x+b

k=pridiction(a,b,12)
print(k)
