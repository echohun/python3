from sklearn.linear_model import LinearRegression
import numpy
import pandas
from sklearn import preprocessing

def traindata():
    train_data=[]
    x_train=[]
    y_train=[]
    file=open(r"traindata.csv","r")
    for line in file.readlines():
        train_data.append(line.strip('\n'))
    for i in train_data:
        serial_number,x_number,y_number = i.split(",")
        x_train.append([float(x_number)])
        y_train.append([float(y_number)])
    X_train=numpy.array(x_train)
    Y_train=numpy.array(y_train)
    linreg = linearRegression()
    linreg.fit(X_train,Y_train)
    return linreg

def predictData(linreg):
    predict_data=[]
    x_test=[]
    serial_list=[]
    file = open(r"predictdata.csv", "r")
    for line in file.readlines():
        predict_data.append(line.strip('\n'))
    for i in predict_data:
        serial_number, x_number = i.split(",")
        serial_list.append(serial_number)
        x_test.append([float(x_number)])
    serial = numpy.array(serial_list)
    X_test = numpy.array(x_test)
    y_pred = linreg.predict(X_test)
    result=numpy.concatenate((serial,X_test,y_pred),axis=1)
    return result

def outPutFile(result):
    data=pandas.DataFrame(result)
    data.to.csv("resultfile.csv",header=False,index=False,sep=",")

def main():
    linreg=traindata()
    result=predictData(linreg)
    print(result)
    outPutFile(result)

main()
