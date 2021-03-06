import math
import numpy as np  
from download_mnist import load
import operator  
import time
from numpy import linalg as LA

# classify using kNN  
#x_train = np.load('../x_train.npy')
#y_train = np.load('../y_train.npy')
#x_test = np.load('../x_test.npy')
#y_test = np.load('../y_test.npy')
x_train, y_train, x_test, y_test = load()
x_train = x_train.reshape(60000,28,28)
x_test  = x_test.reshape(10000,28,28)


def getKey(item):
    return item[1]


def help_sort(dataset, pt, labels):
    nearest_list = []
    index = 0
    for t in dataset:
        x = (labels[index], LA.norm(pt - t, 2))  # make a pair
        nearest_list.append(x)
        index += 1
    list1 = sorted(nearest_list, key=getKey)
    return list1


# Define knn classifier
def kNNClassify(newInput, dataSet, labels, k):
    result=[]
    for pt in newInput:
        list = help_sort(dataSet, pt, labels)
        list = list[:k]
        out_labels = []
        for t in list:
            out_labels.append(t[0])
        # print("out:" ,out_labels)
        label = max(out_labels, key=out_labels.count)
        result.append(label)
    return result


# for k in range(5,10):
#     start_time = time.time()
#     outputlabels=kNNClassify(x_test[0:20],x_train,y_train,k)
#     result = y_test[0:20] - outputlabels
#     result = (1 - np.count_nonzero(result)/len(outputlabels))
#     print ("---classification accuracy for knn on mnist: %s ---" %result)
#     print ("---execution time: %s seconds ---" % (time.time() - start_time))


start_time = time.time()
outputlabels=kNNClassify(x_test[0:20],x_train,y_train, 4)
result = y_test[0:20] - outputlabels
result = (1 - np.count_nonzero(result)/len(outputlabels))
print ("---classification accuracy for knn on mnist: %s ---" %result)
print ("---execution time: %s seconds ---" % (time.time() - start_time))