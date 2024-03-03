import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np


data_dict = pickle.load(open('data.pickel', 'rb'))


data = np.asarray(data_dict['data'])
lables = np.asarray(data_dict['labels'])

X_train, X_test, y_train, y_test = train_test_split(data, lables, test_size=0.2, shuffle=True, stratify=lables)
model = RandomForestClassifier()

model.fit(X_train, y_train)
y_predict = model.predict(X_test)
score = accuracy_score(y_predict, y_test)
print('{}% of were classified correctly !'.format(score*100))


f = open('model.p', 'wb')
pickle.dump({'model':model}, f)
f.close()
