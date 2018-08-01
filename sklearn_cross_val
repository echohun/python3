from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.datasets.samples_generator import make_classification
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score


#生成具有2种属性的300笔数据
X, y = make_classification(
    n_samples=300, n_features=2,
    n_redundant=0, n_informative=2,
    n_clusters_per_class=1,scale=100)

#可视化数据
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()

X = preprocessing.scale(X)

clf = SVC()


scores=cross_val_score(clf,X,y,cv=10,scoring='accuracy')

print(scores)
print(scores.mean())
