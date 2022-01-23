import pymongo
import pandas as pd
from pymongo import MongoClient
client = MongoClient()
db = client["mydatabase"]
collection = db["Db"]
data = pd.DataFrame(list(collection.find()))
print(data)
import matplotlib
import matplotlib.pyplot as plt
plt.plot(data.iloc[:,1],data.G1)
plt.xlabel('Decision vector',color='r')
plt.ylabel('G1',color='r')
plt.show()
plt.plot(data.iloc[:,1],data.G2)
plt.xlabel('Decision vector',color='r')
plt.ylabel('G2',color='r')
plt.show()
data['Decision Vector'].hist(bins=50,figsize=(20,10))
plt.show()
data.hist(bins=50,figsize=(20,15))
plt.show()
plt.scatter(data.iloc[:,1],data.G1,label='Scatter plot Decision Vector VS G1',color='b')
plt.xlabel('Decision vector',color='r')
plt.ylabel('G1',color='r')
plt.show()
plt.scatter(data.iloc[:,1],data.G2,label='Scatter plot Decision Vector VS G2',color='b')
plt.xlabel('Decision Vector',color='r')
plt.ylabel('G2',color='r')
plt.show()
