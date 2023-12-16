# Numpy
import numpy as np
# Pandas
import pandas as pd
# Matplotlib
import matplotlib.pyplot as plt
# Seaborn
import seaborn as sns
# RegEx
import re



df = pd.read_json('https://raw.githubusercontent.com/ozlerhakan/mongodb-json-files/master/datasets/books.json',lines = True)
print(df.head())
print(df.columns)
# Total number of null values in each columns
print(df.isnull().sum())
print(df.info())
print(df.tail())

#data cleaning

#clean isbn no
re.sub('[A-Za-z]*|\n+|-+|,+|:+','',str(df['isbn']))
print(df.info())

# List all those rows in the isbn column where the isbn value is null
print(df[df.isbn.isna()])

df.drop('isbn',axis = 1,inplace = True)
print(df)

# Getting the total number of title ()Unique
len(df.title.unique())

# Show the duplicated rows w.r.t. the title
df[df.title.duplicated()]

# Delete all the duplicate values
df.drop_duplicates('title',inplace=True)

print(df.info())

# Rearrange the values of the _id column
df['_id']= np.arange(1,428)
 
df = df.reset_index(drop=True)

print(df[df['pageCount']==0])
# Replace the values in the pageCount column where the value == 0 with the mean of the 
# mean (rounded off & dtype=int) of pageCount column elements

mean = round(np.mean(df.pageCount))
df['pageCount']=df['pageCount'].replace(0,mean)
print(df[df['pageCount']==mean])
data = df.copy()
data.publishedDate.fillna(0,inplace=True)
#if v have converted the values of publishedDate a s string somewhere it wont fill it with 0 , at that time v should use replace()
print("this is ",data[data['publishedDate']==0])

for i in range(len(data.publishedDate)):
  data.publishedDate[i] = re.sub("^{.*: '|-.*}","",str(df['publishedDate'][i]))

print( data[data.publishedDate.isna()])

data.publishedDate = data.publishedDate.replace('nan','0')
print(data.publishedDate.loc[[96]])
data.publishedDate = data.publishedDate.astype(int)
print(data.info())

mean = round(np.mean(data.publishedDate))
data['publishedDate']=data['publishedDate'].replace(0,mean)

data.drop(['thumbnailUrl','shortDescription','longDescription'],axis = 1,inplace = True)
print(data.status.unique())

print(data['status'].value_counts())
data['status']=data['status'].replace('MEAP','UNPUBLISH')

print(data['status'].value_counts())
data.drop(['_id','authors','categories'],axis = 1,inplace = True)

print(data.head(5))
data['status'].value_counts().plot.bar(figsize=(10,5))
plt.grid()
plt.show()





