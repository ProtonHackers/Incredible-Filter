import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score

clf = svm.SVC()


def train(features, labels):
    clf.fit(features, labels)


def pedict(articles):
    return clf.predict(articles)
