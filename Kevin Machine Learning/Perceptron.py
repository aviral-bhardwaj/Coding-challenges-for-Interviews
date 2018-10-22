import pandas as pd

def Extract_traindata():
	train_file="pa2_train.csv"
	fd=pd.read_csv(train_file,header=None)

	y=fd.iloc[:,0:1]
	X=fd.iloc[:,1:]
	y=pd.DataFrame([1 if i==3 else -1 for i in y.values])
	X.insert(loc=0, column='', value=[1]*4888)
	
	return X,y
	
if __name__=="__main__":
	X,Y=Extract_traindata()
	print(X)
	print(Y)
	