import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


#loading a dataset to a pandas dataframe
sonar_data = pd.read_csv('sonar data.csv',header = None)

sonar_data.head()

#no of rows and cols
# print(sonar_data.shape)

#statistical measures for data
sonar_data.describe()

sonar_data[60].value_counts()

sonar_data.groupby(60).mean()

#seperating data and labels
x=sonar_data.drop(columns = 60, axis = 1)
y=sonar_data[60]
#
# print(x)
# print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.1, stratify = y, random_state = 1)

# print(x.shape, x_train.shape, x_test.shape)
#
# print(x_train, y_train)


model = LogisticRegression()

#training model with training data
model.fit(x_train, y_train)



#accuracy on training data
x_train_prediction=model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)

print('Accuracy on training Data = ', (100*training_data_accuracy))

x_test_prediction = model.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction, y_test)

print('Accuracy on Test Data = ', (100*test_data_accuracy))

input_data =(0.02246,0.0019,0.0075,0.0097,0.0445,0.0906,0.01000,0.0655,0.1624,0.1452,0.1442,0.0948,0.0618,0.1641,0.0708,0.0844,0.2590,0.2679,0.3094,0.4678,0.5958,0.7245,0.8773,0.9214,0.9282,0.9942,1.0000,0.9071,0.8545,0.7293,0.6499,0.6071,0.5588,0.5967,0.6275,0.5459,0.4786,0.3965,0.2087,0.1651,0.1836,0.0652,0.0758,0.0486,0.0353,0.0297,0.0241,0.0379,0.0119,0.0073,0.0051,0.0034,0.0129,0.0100,0.0044,0.0057,0.0030,0.0035,0.0021,0.0027)


#input_data as numpy array
input_data_numpy = np.asarray(input_data)

input_data_reshaped = input_data_numpy.reshape(1,-1)
prediction = model.predict(input_data_reshaped)

if(prediction[0] == 'R'):
  print('The object is a Rock')
else:
  print('The object is a Mine')