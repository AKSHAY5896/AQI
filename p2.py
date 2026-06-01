import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

data=pd.read_csv("pm25_data.csv")
features=data[["pm25"]]

mns=MinMaxScaler()
new_features=mns.fit_transform(features)
#print(new_features)

model=KMeans(n_clusters=6,random_state=2)
result=model.fit_predict(new_features)
data['cluster']=result
print(data)

d0=data[data.cluster==0]
d1=data[data.cluster==1]
d2=data[data.cluster==2]
d3=data[data.cluster==3]
d4=data[data.cluster==4]
d5=data[data.cluster==5]

plt.scatter(d0["city"],d0["pm25"],color="red",label="c1")
plt.scatter(d1["city"],d1["pm25"],color="green",label="c2")
plt.scatter(d2["city"],d2["pm25"],color="blue",label="c3")
plt.scatter(d3["city"],d3["pm25"],color="black",label="c4")
plt.scatter(d4["city"],d4["pm25"],color="purple",label="c5")
plt.scatter(d5["city"],d5["pm25"],color="lime",label="c6")
plt.xlabel("CITY")
plt.ylabel("Air Pollutants")
plt.title("cluster diagram")
plt.legend()
plt.show()