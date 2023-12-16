from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

url = "https://raw.githubusercontent.com/ozlerhakan/mongodb-json-files/master/datasets/grades.json"
req = requests.get(url)

soup = BeautifulSoup(req.content,'html.parser')
df = pd.read_json("https://raw.githubusercontent.com/ozlerhakan/mongodb-json-files/master/datasets/grades.json", lines=True)
print(df)
exam_score=[]
quiz_score=[]
homework_score=[]
#for i in range(len(df._id)):
    #df._id[i]=re.sub("^{'.*: '|'}","",str(df._id[i]))
for i in range(len(df._id)):
    df.at[i, '_id'] = re.sub("^{'.*: '|'}", "", str(df._id[i]))
    
    #print(df.scores[0])

    """[{'score': 57.92947112575566, 'type': 'exam'},
        {'score': 21.24542588206755, 'type': 'quiz'},
        {'score': 68.1956781058743, 'type': 'homework'},
        {'score': 67.95019716560351, 'type': 'homework'},
        {'score': 18.81037253352722, 'type': 'homework'}]"""


    """3 Columns -> exam_score, quiz_score, homework_score
        ._ _

        Final output -> id, student_id, class id, exam_score, quiz_score, homework_score"""
    

    exam_score.append(round(df.scores[i][0]['score'],2))#roundoff to 2 deci point
    quiz_score.append(round(df.scores[i][1]['score'],2))

    arr=df.scores[i][2:]


    sum=0
    
    for j in range(len(arr)):  
        sum+=arr[j]['score']
    avg=sum/len(arr)

    homework_score.append(round(avg,2))

new_df = pd.DataFrame({"id":df['_id'], "student_id":df['student_id'], "class_id":df['class_id'],
                       "exam_score":exam_score,"quiz_score":quiz_score, "homework_score":homework_score})
print(new_df)
print(new_df.describe())


x = new_df.exam_score
y = new_df.homework_score
plt.scatter(x,y)
plt.xlabel('Exam Score')
plt.ylabel('Homework Score')
plt.title('Exam Score V/S Homework Score')
plt.show() 
    







