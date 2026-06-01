import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import pickle
from pickle import dump

data=pd.read_csv("pm25_data.csv")
#print(data)
#print(data.head(3))
#print(data.isna().sum())
#print(data.info())
#print(data.describe())
#print(data["city"].dtype)
#print(data["pm25"].dtype)
#print(type('O'))
#print(data.shape)
#data.drop(['city'], axis=1, inplace=True)
#df_num = data.select_dtypes(include=np.number)
#print(df_num)
#df_num.hist()
#plt.show()
#data.groupby('city')['pm25'].mean().plot(kind='bar')
#plt.show()

features=data[["pm25"]]
#print(features)

#mns=MinMaxScaler()
#new_features=mns.fit_transform(features)
#print(new_features)

model=KMeans(n_clusters=6,random_state=2)
result=model.fit_predict(features)
data['cluster']=result
print(data)

#b=float(input("enter PM2.5"))
#d=[[b]]
#new_d=mns.transform(d)
#res=model.predict(new_d)
#print(res)

#plt.scatter(data["city"],data["pm25"],c=data['cluster'])
#plt.xlabel("CITY")
#plt.ylabel("Air Pollutants")
#plt.show()

#d0=data[data.cluster==0]
#d1=data[data.cluster==1]
#d4=data[data.cluster==4]

#plt.scatter(d0["city"],d0["pm25"],color="red",label="c1")
#plt.scatter(d1["city"],d1["pm25"],color="blue",label="c2")
#plt.scatter(d4["city"],d4["pm25"],color="pink",label="c5")
#plt.xlabel("CITY")
#plt.ylabel("Air Pollutants")
#plt.title("cluster diagram")
#plt.legend()
#plt.show()

b=float(input("enter PM2.5"))
d=[[b]]
#new_d=mns.transform(d)
res=model.predict(d)
print(res)


pickle.dump(model, open("model.pkl","wb"))

