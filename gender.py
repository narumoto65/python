from sklearn import tree
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
x = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[170,70,40],[159,55,37],[171,75,42]]
y = ['male','female','female','female','male','male','male','female','male','female']
#clf = tree.DecisionTreeClassifier()
clf = SVC()
test_x = [[187,76,45],[176,70,43],[167,60,47],[154,54,37]]
test_y = ['male','female','male','female']
clf = clf.fit(x,y)
prediction = clf.predict(test_x)
print prediction
print(accuracy_score(test_y,prediction))

