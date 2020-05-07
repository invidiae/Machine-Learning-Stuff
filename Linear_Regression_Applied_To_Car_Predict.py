import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
global X,y,theta
df = pd.read_csv(r"C:/Users/Isabelle/Desktop/Camillo/PythonStuff/car-price-prediction/CarPrice_Assignment.csv")
#Daten Importieren
X1 = df.horsepower.to_numpy()[:,None]
X2 = df.highwaympg.to_numpy()[:,None]
X3 = df.citympg.to_numpy()[:,None]
X4 = df.enginesize.to_numpy()[:,None]
X5 = df.boreratio.to_numpy()[:,None]
X6 = df.citympg.to_numpy()[:,None]
X7 = df.curbweight.to_numpy()[:,None]
y = df.price.to_numpy()[:,None]

X = np.concatenate((np.ones((len(y),1))
										,X1,X2,X3,X4,X5,X6,X7),1)






def cost(X,y,theta):
  n_samples = len(y)
  h = X.dot(theta)
  return (1/(2*n_samples))*np.sum((h-y)**2)

def scale(X):
	for index,c in enumerate(X[0,:]):
		if index != 0:
			X[:,index] = (X[:,index]-min(X[:,index]))/(max(X[:,index])-min(X[:,index]))
	return X

def fit(X,y,theta,n_iter=300,alpha=1):
	temp = theta[:]
	error_hist = []
	for  i in range(n_iter):
		for index,t in enumerate(theta):
			curX = X[:,index]
			curX = curX[:,None]
			(X.dot(theta)-y).T.dot(curX)
			temp[index] = t - ((alpha*(1/len(y)))*np.sum((X.dot(theta)-y).T.dot(curX)))
		theta = temp
		error_hist.append(cost(X,y,theta))
	plt.plot(error_hist)
	print(error_hist[-1])

	return theta

def main(X,y,theta=np.zeros((np.size(X,1),1))):
	X = scale(X)
	theta = fit(X, y, theta)
	#plt.plot(y, "ro")
	#plt.plot(X.dot(theta))
	#plt.show()
main(X,y)

plt.show()
