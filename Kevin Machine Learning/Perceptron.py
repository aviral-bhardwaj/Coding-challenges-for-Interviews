import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Extract_data(f_name):
	train_file=f_name
	fd=pd.read_csv(train_file,header=None)

	y=fd.iloc[:,0:1]
	X=fd.iloc[:,1:]
	y=pd.DataFrame([1 if i==3 else -1 for i in y.values])
	X.insert(loc=0, column='', value=[1]*X.shape[0])
	
	return X,y

	
def validate_model(f_name,w_bar):
	X,y=Extract_data(f_name)
	X,y=X.values,y.values
	c=0
	for (i,x) in enumerate(X):
		ut=np.sign(x.dot(w_bar))
		if y[i]*ut <=0:
			continue
		else:
			c+=1
	return c
	

def average_perceptron(m_value,X,y):
	X=X.values
	y=y.values
	max_iters=m_value
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
	X,Y=Extract_data("pa2_train.csv")
	max_iters=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
	res_valid=[]
	res_train=[]
	for i in max_iters:
		w=average_perceptron(i,X,Y)
		res_valid.append(validate_model("pa2_valid.csv",w))
		res_train.append(validate_model("pa2_train.csv",w))
		
	plt.plot(max_iters,res_valid, '-',color='r')
	plt.axis([0, 15, 1530, 1560])
	plt.xlabel('Number of iterations')
	plt.ylabel('Correct predictions')
	plt.show()
	
	print(max_iters)
	print(res_valid)
	print(res_train)
	

	