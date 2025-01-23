from re import template
from sklearn.naive_bayes import GaussianNB
#WAP in python yo implement Naive Bay's algorithm for following training data.
#Predict class for x=(Overcast,Cool,High,Srong)

weather=    ['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Rainy']
temp=       ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
humidity=   ['High','High','High','High','Normal','Normal','Normal','High','Normal','Normal','Normal','High','Normal','High']
wind=       ['Weak','','Weak','Weak','Weak','Strong','Strong','Weak','Weak','Weak','Strong','Strong','Weak','']
play=       ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

from sklearn import preprocessing

le=preprocessing.LabelEncoder() #Encode target labels with value

#weather data into number

we =le.fit_transform(weather)

#temperature input text data into number
t=le.fit_transform(temp)

#humidity input text data into number
h=le.fit_transform(humidity)

#wind input text data into number
w=le.fit_transform(wind)

#play input text data into number
p=le.fit_transform(play)

print (we,t,h,w,p)

features=zip(we,t,h,w,p)
inp=list(features)
print("Input Data:")
print(inp)
print("Actual")


