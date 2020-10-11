from sklearn.preprocessing import LabelEncoder() 
# encode the dependent variable
encode = LabelEncoder()
encode.fit(y)
Y = one_hot_encode(y)
print(X.shape)
return (X,Y)