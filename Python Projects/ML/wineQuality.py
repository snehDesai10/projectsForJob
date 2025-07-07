import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#data loaded to wine_data
wine_data = pd.read_csv('WineQT.csv', header = 0)

# print(wine_data.head())

a = wine_data.iloc[:, :-1]
x= a.iloc[:, :-1]
y = a.iloc[:, -1]

# print(x)
# print(y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.1, stratify = y, random_state = 1)

model = LogisticRegression(max_iter=10000);
model.fit(x_train,y_train)

x_train_prediction=model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)

print('Accuracy on training Data = ', (100*training_data_accuracy))

x_test_prediction = model.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction, y_test)

print('Accuracy on Test Data = ', (100*test_data_accuracy))

# print(wine_data.iloc[:, -1].value_counts())
input = (7.8,0.76,0.04,2.3,0.092,15.0,54.0,0.9970,3.26,0.65,9.8)

input_np = np.asarray(input)

input_data_reshaped = input_np.reshape(1,-1)
prediction = model.predict(input_data_reshaped)

print('Rating of WINE:', prediction)
