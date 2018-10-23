import pandas as pd
import numpy as np

def Extract_traindata():
	train_file="pa2_train.csv"
	fd=pd.read_csv(train_file,header=None)

	y=fd.iloc[:,0:1]
	X=fd.iloc[:,1:]
	y=pd.DataFrame([1 if i==3 else -1 for i in y.values])
	X.insert(loc=0, column='', value=[1]*4888)
	
	return X,y

def Extract_validdata():
	valid_file="pa2_valid.csv"
	fd=pd.read_csv(valid_file,header=None)

	y=fd.iloc[:,0:1]
	X=fd.iloc[:,1:]
	y=pd.DataFrame([1 if i==3 else -1 for i in y.values])
	X.insert(loc=0, column='', value=[1]*X.shape[0])
	
	return X,y
	
def validate_model(w_bar):
	X,y=Extract_validdata()
	X,y=X.values,y.values
	c=0
	for (i,x) in enumerate(X):
		ut=np.sign(x.dot(w_bar))
		if y[i]*ut <=0:
			continue
		else:
			c+=1
	print("Total number of correct predictions : ",c)
	

def average_perceptron(X,y):
	X=X.values
	y=y.values
	max_iters=15
	w=np.array([0 for i in range(X.shape[1])])
	w_bar=np.array([0 for i in range(X.shape[1])])
	c,s=0,0
	for iter in range(max_iters):
		for (j,x) in enumerate(X):
			ut=np.sign(x.dot(w))
			if y[j]*ut <=0:
				if s+c>0:
					w_bar=((s*w_bar)+(c*w))/(s+c)
				s=s+c
				w=w+y[j]*x
				c=0
			else:
				c+=1
	if c>0:
		w_bar=(s*w_bar)+(c*w)/(s+c)
	return w_bar
		
		
	
if __name__=="__main__":
	X,Y=Extract_traindata()
	w=average_perceptron(X,Y)
	print("w_bar after: ",w)
	validate_model(w)
	

	