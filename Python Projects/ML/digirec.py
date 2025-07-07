import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv('digits.csv',header = None)

# print(data.head())

x = data.iloc[:, :-1]  # all columns except last (features)
y = data.iloc[:, -1]   # last column (target)


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.1, stratify = y, random_state = 1)
model = LogisticRegression()
# print(x_train)

model.fit(x_train, y_train)

x_train_prediction=model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)
x_test_prediction = model.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction, y_test)
# print('Accuracy on training Data = ', (100*training_data_accuracy))
# print('Accuracy on Test Data = ', (100*test_data_accuracy))

x = int(input())
input_data =(x)


#input_data as numpy array
input_data_numpy = np.asarray(input_data)

input_data_reshaped = input_data_numpy.reshape(1,-1)
prediction = model.predict(input_data_reshaped)

if(prediction[0] == 's'):
  print('Single Digit')
elif(prediction[0] == 'd'):
  print('Double Digit')
else:
  print('Triple Digit')