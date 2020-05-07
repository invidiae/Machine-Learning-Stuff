import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


URL = "https://college.cengage.com/mathematics/brase/understandable_statistics/7e/students/datasets/mlr/excel/mlr06.xls"
df = pd.read_excel(URL)
df = df.to_csv(df, index=False)
df = np.delete(df)
y = df["X1"].to_numpy()
X = np.delete(df,0,axis=1)
X = X.to_numpy()

global X,y,theta


X = np.arange(1,11)[:,None]
y = X[:,0]**2 + np.random.normal(0,3,10)
y = y[:,None]
X = np.insert(X,0,1,1)
X = np.c_[X,X[:,1]**2].astype(float)
theta = np.zeros((np.size(X,1),1))


def cost(X,y,theta):
  n_samples = len(y)
  h = X.dot(theta)
  return (1/(2*n_samples))*np.sum((h-y)**2)

def scale(X):
	for index,c in enumerate(X[0,:]):
		if index != 0:
			X[:,index] = (X[:,index]-min(X[:,index]))/(max(X[:,index])-min(X[:,index]))
	return X

def fit(X,y,theta,n_iter=600,alpha=1):
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
	#plt.plot(error_hist)
	print(error_hist[-1])

	return theta

def main(X,y,theta):
	X = scale(X)
	theta = fit(X, y, theta)
	plt.plot(y, "ro")
	plt.plot(X.dot(theta))
	plt.show()
main(X,y,theta)

plt.show()
